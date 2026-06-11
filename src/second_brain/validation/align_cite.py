"""Deterministic align-cite core (Decision A keystone).

This is the *mechanical* half of the align-cite gate. It makes machine-checkable
PASS/FAIL judgments that are the publish blocker. The LLM layer in
`.github/prompts/workspace-align-cite.prompt.md` runs SECOND, only on rows this
layer marks PASS, and may downgrade PASS->FAIL on a bad-faith match — it may
NEVER upgrade a mechanical FAIL.

Invariant: retrieval may decide what to read; only this verification decides what
may publish.

Deterministic checks, per artifact:

  C1 source-exists   every frontmatter `sources:` *local* path resolves on disk.
                     External URLs are advisory PASS (not fetched; cached trust),
                     matching the prompt's offline policy.
  C2 quote-grounded  every quoted span in the body occurs verbatim
                     (whitespace/case-normalized) in at least one *local* cited
                     source. If the artifact has no local cited source, spans are
                     advisory PASS (nothing on disk to verify against — the LLM
                     layer owns external-only citations).
  C3 vendor-grounded if `domain: vendor:X`, at least one cited source must be a
                     vendor source for X (a `raw/workspace-external/X/...` path,
                     or a wiki article whose own `domain` is `vendor:X`).

A "quoted span" is deliberately narrow to stay high-precision (a noisy blocker is
worse than none): a markdown blockquote block, or an inline double-quoted run of
at least QUOTE_MIN_WORDS words. Short quoted terms (defined terms, emphasis) are
ignored.

Exit code is non-zero if any artifact has a FAIL.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - yaml is a declared dependency
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[3]

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
BLOCKQUOTE_LINE_RE = re.compile(r"^\s*>\s?(.*)$")
# Straight and smart double-quoted inline runs.
INLINE_QUOTE_RE = re.compile(r"[\"“]([^\"“”]+)[\"”]")

QUOTE_MIN_WORDS = 5
PROJECTS_DIR = "wiki/workspace-projects"
VENDOR_PREFIX = "raw/workspace-external/"


# --------------------------------------------------------------------------- #
# Parsing helpers
# --------------------------------------------------------------------------- #
def split_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Empty dict + full text if no frontmatter."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm: dict = {}
    if yaml:
        loaded = yaml.safe_load(m.group(1))
        if isinstance(loaded, dict):
            fm = loaded
    return fm, m.group(2)


def normalize(s: str) -> str:
    """Lowercase, normalize quotes/dashes, collapse whitespace."""
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def extract_quoted_spans(body: str) -> list[str]:
    """Extract deliberate quotations: blockquote blocks + long inline quotes."""
    spans: list[str] = []

    # Blockquote blocks (consecutive `>` lines joined).
    current: list[str] = []
    for line in body.splitlines():
        m = BLOCKQUOTE_LINE_RE.match(line)
        if m:
            current.append(m.group(1))
        elif current:
            spans.append(" ".join(current).strip())
            current = []
    if current:
        spans.append(" ".join(current).strip())

    # Long inline double-quoted runs.
    for m in INLINE_QUOTE_RE.finditer(body):
        quote = m.group(1).strip()
        if len(quote.split()) >= QUOTE_MIN_WORDS:
            spans.append(quote)

    # Drop empties and trivially short blockquotes.
    return [s for s in spans if len(s.split()) >= QUOTE_MIN_WORDS]


def is_external_url(src: str) -> bool:
    return src.strip().lower().startswith(("http://", "https://"))


def vendor_of_path(src: str) -> str | None:
    """Vendor name if `src` is a raw/workspace-external/{vendor}/... path."""
    src = src.replace("\\", "/")
    if src.startswith(VENDOR_PREFIX):
        rest = src[len(VENDOR_PREFIX) :]
        vendor = rest.split("/", 1)[0].strip()
        return vendor or None
    return None


def source_vendor(root: Path, src: str) -> str | None:
    """Vendor a cited source attests to: from its path, else its wiki `domain`."""
    by_path = vendor_of_path(src)
    if by_path:
        return by_path
    candidate = (root / src).resolve()
    if candidate.is_file() and src.replace("\\", "/").startswith("wiki/"):
        fm, _ = split_frontmatter(candidate.read_text(encoding="utf-8", errors="replace"))
        domain = str(fm.get("domain", ""))
        if domain.startswith("vendor:"):
            return domain.split(":", 1)[1].strip() or None
    return None


# --------------------------------------------------------------------------- #
# Result model
# --------------------------------------------------------------------------- #
@dataclass
class Row:
    check: str  # source-exists | quote-grounded | vendor-grounded
    subject: str
    verdict: str  # PASS | FAIL
    detail: str


@dataclass
class ArtifactResult:
    path: str
    rows: list[Row] = field(default_factory=list)

    @property
    def failed(self) -> bool:
        return any(r.verdict == "FAIL" for r in self.rows)

    @property
    def fail_count(self) -> int:
        return sum(1 for r in self.rows if r.verdict == "FAIL")


def _truncate(s: str, n: int = 80) -> str:
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


# --------------------------------------------------------------------------- #
# Core check
# --------------------------------------------------------------------------- #
def check_artifact(root: Path, path: Path) -> ArtifactResult:
    rel = str(path.relative_to(root)).replace("\\", "/")
    result = ArtifactResult(path=rel)
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = split_frontmatter(text)

    sources = [s for s in (fm.get("sources") or []) if isinstance(s, str)]

    # C1: source-exists
    local_sources: list[str] = []
    for src in sources:
        if is_external_url(src):
            result.rows.append(
                Row("source-exists", src, "PASS", "external URL (not fetched; cached trust)")
            )
            continue
        target = (root / src).resolve()
        if target.is_file():
            local_sources.append(src)
            result.rows.append(Row("source-exists", src, "PASS", "resolves on disk"))
        else:
            result.rows.append(
                Row("source-exists", src, "FAIL", "cited source path does not exist")
            )

    # C2: quote-grounded
    haystack = ""
    for src in local_sources:
        haystack += "\n" + normalize((root / src).read_text(encoding="utf-8", errors="replace"))
    for span in extract_quoted_spans(body):
        subject = _truncate(span)
        if not local_sources:
            result.rows.append(
                Row("quote-grounded", subject, "PASS", "no local source to verify against")
            )
        elif normalize(span) in haystack:
            result.rows.append(Row("quote-grounded", subject, "PASS", "found in a cited source"))
        else:
            result.rows.append(
                Row("quote-grounded", subject, "FAIL", "quoted span not found in any cited source")
            )

    # C3: vendor-grounded
    domain = str(fm.get("domain", ""))
    if domain.startswith("vendor:"):
        vendor = domain.split(":", 1)[1].strip()
        attests = sorted({v for src in sources if (v := source_vendor(root, src))})
        if vendor in attests:
            result.rows.append(
                Row("vendor-grounded", domain, "PASS", f"cites a vendor:{vendor} source")
            )
        else:
            result.rows.append(
                Row(
                    "vendor-grounded",
                    domain,
                    "FAIL",
                    f"domain is vendor:{vendor} but no cited source attests to {vendor}"
                    + (f" (sources attest: {', '.join(attests)})" if attests else ""),
                )
            )

    return result


# --------------------------------------------------------------------------- #
# Target resolution
# --------------------------------------------------------------------------- #
def iter_artifacts(root: Path, target: str) -> list[Path]:
    """Resolve a target (artifact path or project slug) to artifact files."""
    as_path = (root / target) if not Path(target).is_absolute() else Path(target)
    if as_path.is_file():
        return [as_path]

    project_dir = root / PROJECTS_DIR / target
    if project_dir.is_dir():
        artifacts = []
        for md in sorted(project_dir.rglob("*.md")):
            fm, _ = split_frontmatter(md.read_text(encoding="utf-8", errors="replace"))
            if fm.get("type") == "project-artifact":
                artifacts.append(md)
        return artifacts
    return []


def project_name(root: Path, target: str, artifacts: list[Path]) -> str:
    if (root / PROJECTS_DIR / target).is_dir():
        return target
    if artifacts:
        fm, _ = split_frontmatter(artifacts[0].read_text(encoding="utf-8", errors="replace"))
        if fm.get("project"):
            return str(fm["project"])
        return artifacts[0].stem
    return target


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
def render_report(project: str, results: list[ArtifactResult], date: str) -> str:
    total = sum(len(r.rows) for r in results)
    fails = sum(r.fail_count for r in results)
    verdict = "FAIL" if fails else "PASS"
    lines = [
        f"# align-cite (deterministic) report: {project}",
        "",
        f"Date: {date}",
        f"Artifacts checked: {len(results)}",
        f"Checks run: {total}",
        f"Failures: {fails}",
        f"Overall verdict: **{verdict}**",
        "",
        "_Deterministic core only. This verdict is the publish blocker; the LLM "
        "layer runs second on PASS rows and never relaxes a FAIL._",
        "",
    ]
    for res in results:
        lines.append(f"## {res.path}")
        lines.append("")
        if not res.rows:
            lines.append("_No citations or quoted spans to check._")
            lines.append("")
            continue
        lines.append("| Check | Subject | Verdict | Detail |")
        lines.append("|---|---|---|---|")
        for row in res.rows:
            subject = row.subject.replace("|", "\\|")
            detail = row.detail.replace("|", "\\|")
            lines.append(f"| {row.check} | {subject} | {row.verdict} | {detail} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def write_report(root: Path, project: str, results: list[ArtifactResult], date: str) -> Path:
    report_path = root / "reports" / f"workspace-align-cite-{project}-{date}.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(project, results, date), encoding="utf-8")
    return report_path


# --------------------------------------------------------------------------- #
# Entrypoints
# --------------------------------------------------------------------------- #
def run(root: Path, target: str, date: str | None = None) -> tuple[int, Path | None, list[ArtifactResult]]:
    date = date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    artifacts = iter_artifacts(root, target)
    if not artifacts:
        print(f"align-cite: no artifacts found for target '{target}'", file=sys.stderr)
        return 2, None, []
    results = [check_artifact(root, a) for a in artifacts]
    project = project_name(root, target, artifacts)
    report = write_report(root, project, results, date)
    fails = sum(r.fail_count for r in results)
    return (1 if fails else 0), report, results


def cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="second-brain align-cite",
        description="Deterministic citation verification (publish blocker).",
    )
    parser.add_argument("target", help="artifact path or project slug")
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    parser.add_argument("--date", help="override report date (YYYY-MM-DD); default today UTC")
    ns = parser.parse_args(argv)

    root = ns.root.resolve()
    code, report, results = run(root, ns.target, ns.date)
    if report is None:
        return code
    fails = sum(r.fail_count for r in results)
    verdict = "FAIL" if fails else "PASS"
    print(f"align-cite (deterministic): {verdict} — {fails} failure(s) across {len(results)} artifact(s)")
    print(f"Report: {report}")
    for res in results:
        if res.failed:
            for row in res.rows:
                if row.verdict == "FAIL":
                    print(f"  FAIL {res.path} [{row.check}] {row.subject}: {row.detail}")
    return code


if __name__ == "__main__":
    sys.exit(cli())
