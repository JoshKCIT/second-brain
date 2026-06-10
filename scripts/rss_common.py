"""Shared helpers for the workspace RSS feed lane."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

RSS_REL = Path("raw/workspace-rss-feed")
CONFIG_NAMES = ("rss-feeds.yml", "rss-feeds.example.yml")
REGISTER_REL = RSS_REL / "rss-register.md"
STATE_DIR = RSS_REL / ".state"
SEEN_FILE = STATE_DIR / "seen.json"
TRIAGE_SCORES_FILE = STATE_DIR / "triage-scores.json"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)

SUMMARY_EXCERPT_MAX = 320


def load_rss_config(root: Path, *, allow_example: bool = False) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML required. pip install pyyaml")
    config_dir = root / "config"
    for name in CONFIG_NAMES:
        path = config_dir / name
        if path.is_file():
            with path.open(encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
    if allow_example:
        return {}
    raise FileNotFoundError(
        "RSS config not found. Copy config/rss-feeds.example.yml to config/rss-feeds.yml"
    )


def rss_base(root: Path) -> Path:
    return root / RSS_REL


def ensure_rss_dirs(root: Path) -> None:
    base = rss_base(root)
    for sub in ("items", "promoted", "quarantine", ".state"):
        (base / sub).mkdir(parents=True, exist_ok=True)
    gitkeep = base / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.touch()


def item_id_from_entry(guid: str, link: str) -> str:
    key = (guid or "").strip() or (link or "").strip()
    if not key:
        raise ValueError("RSS entry requires guid or link")
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def parse_domain(feed: dict[str, Any]) -> tuple[str, str]:
    domain = str(feed.get("domain") or "informational")
    authority = str(feed.get("authority") or "informational")
    if domain.startswith("vendor:"):
        return domain, authority
    if domain in ("internal", "informational") or domain.startswith("industry:"):
        return domain, authority
    return f"vendor:{domain}", authority


def entry_published_iso(entry: Any) -> str:
    if getattr(entry, "published_parsed", None):
        try:
            t = entry.published_parsed
            dt = datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, tzinfo=timezone.utc)
            return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        except (TypeError, ValueError):
            pass
    if getattr(entry, "updated_parsed", None):
        try:
            t = entry.updated_parsed
            dt = datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, tzinfo=timezone.utc)
            return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        except (TypeError, ValueError):
            pass
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def entry_summary(entry: Any) -> str:
    for attr in ("summary", "description", "content"):
        val = getattr(entry, attr, None)
        if not val:
            continue
        if isinstance(val, list) and val:
            return str(val[0].get("value", "")) if isinstance(val[0], dict) else str(val[0])
        return str(val)
    return ""


def build_item_frontmatter(
    *,
    title: str,
    source_url: str,
    feed_slug: str,
    item_id: str,
    published_at: str,
    ingested_at: str,
    domain: str,
    authority: str,
    inbox_status: str = "unprocessed",
    triage_status: str = "pending",
    triage_score: float | None = None,
    matched_rules: list[str] | None = None,
) -> str:
    lines = [
        "---",
        f"title: {_yaml_escape(title)}",
        f"source_url: {_yaml_escape(source_url)}",
        f"feed_slug: {feed_slug}",
        f"item_id: {item_id}",
        f"published_at: {published_at}",
        f"ingested_at: {ingested_at}",
        "capture_method: rss",
        f"domain: {domain}",
        f"authority: {authority}",
        f"inbox_status: {inbox_status}",
        f"triage_status: {triage_status}",
    ]
    if triage_score is not None:
        lines.append(f"triage_score: {triage_score:.4f}")
    if matched_rules:
        lines.append("matched_rules:")
        for rule in matched_rules:
            lines.append(f"  - {_yaml_escape(rule)}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _yaml_escape(value: str) -> str:
    if not value:
        return '""'
    if any(c in value for c in '":\n#'):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return value


def summary_excerpt(body: str, max_len: int = SUMMARY_EXCERPT_MAX) -> str:
    text = " ".join((body or "").split()).strip()
    if not text:
        return ""
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"


def review_flags(source_url: str, summary: str) -> list[str]:
    flags: list[str] = []
    url = (source_url or "").lower()
    if "example.com" in url or "example.org" in url:
        flags.append("fixture_url")
    if not summary or summary == "_No summary in feed entry._":
        flags.append("no_summary")
    return flags


def parse_item_file(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    return meta, body


def patch_item_frontmatter(path: Path, updates: dict[str, Any]) -> None:
    meta, body = parse_item_file(path)
    meta.update(updates)
    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
    path.write_text(f"---\n{fm}\n---\n\n{body.lstrip()}", encoding="utf-8")


def load_json_state(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_json_state(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_rss_log(root: Path, summary: str, details: list[str]) -> None:
    log_path = root / "wiki" / "log.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [f"\n## [{ts}] ingest-rss | {summary}"]
    lines.extend(f"- {d}" for d in details)
    entry = "\n".join(lines) + "\n"
    if log_path.is_file():
        log_path.write_text(log_path.read_text(encoding="utf-8") + entry, encoding="utf-8")
    else:
        log_path.write_text(f"# Build Log\n{entry}", encoding="utf-8")


def iter_item_files(root: Path) -> list[Path]:
    items_dir = rss_base(root) / "items"
    if not items_dir.is_dir():
        return []
    return sorted(p for p in items_dir.rglob("*.md") if p.is_file())


def item_rel_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def find_item_path(root: Path, item_id: str) -> Path | None:
    for path in iter_item_files(root):
        meta, _ = parse_item_file(path)
        if str(meta.get("item_id", "")) == item_id:
            return path
    return None


def load_active_project_slugs(root: Path) -> list[str]:
    projects = root / "wiki" / "workspace-projects"
    if not projects.is_dir():
        return []
    slugs: list[str] = []
    for meta in projects.glob("*/meta.yml"):
        try:
            data = yaml.safe_load(meta.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        slug = data.get("slug") or meta.parent.name
        if slug:
            slugs.append(str(slug))
    return slugs


def load_in_scope_keywords(root: Path, vendor_slugs: list[str]) -> list[str]:
    keywords: list[str] = []
    config_dir = root / "config"
    for slug in vendor_slugs:
        path = config_dir / f"{slug}-in-scope-services.yml"
        if not path.is_file():
            continue
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        for key in ("services", "features", "topics"):
            for item in data.get(key) or []:
                if isinstance(item, str):
                    keywords.append(item.replace("-", " "))
    return keywords
