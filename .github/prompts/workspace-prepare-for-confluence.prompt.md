---
description: Convert Markdown project artifact(s) to vanilla HTML preview, write to confluence-review/, open the folder via OS-native opener.
mode: agent
---

# /prepare-for-confluence

You are generating a local HTML preview of project artifact(s) so the user can review the rendered content before pushing to Confluence.

## Inputs

- Path to one artifact, OR a project slug (prepares all artifacts in the project's active set)

## Workflow

### Step 1: Convert each artifact

For each input Markdown file:

1. Convert Markdown to vanilla HTML (browser-readable preview, NOT Confluence storage format)
2. Use a standard Markdown-to-HTML converter (e.g., Python markdown library; the choice is build-time)
3. Apply minimal CSS for readability (sans-serif body, monospace code blocks, light table styling)
4. Resolve relative wikilinks: convert `[[file]]` to `<a href="file.html">file</a>` so the local preview is navigable
5. Resolve external URLs: keep as `<a href="..." target="_blank">`

### Step 2: Write to review folder

Write each HTML file to:

```
confluence-review/{project-slug}/{artifact-stem}-{ISO timestamp}.html
```

Where `{artifact-stem}` is the original Markdown filename without extension.

### Step 3: Print path and open folder

Print to the user the full Windows path to the folder (not just the workspace path):

```
HTML previews ready at:
C:\Users\Admin\Documents\Claude\Projects\second-brain\confluence-review\{project-slug}\

Files:
- {artifact-stem}-{ISO}.html
- ...

Opening folder...
```

Open the folder using the OS-native opener:

- Windows: `explorer "C:\Users\...\confluence-review\{project-slug}"`
- macOS: `open "..."`
- Linux: `xdg-open "..."`

Detect OS via uname or environment.

### Step 4: Append to log

```
## [{ISO timestamp}] prepare-for-confluence | {slug or artifact}
- Files generated: {count}
- Output folder: confluence-review/{slug}/
```

## Notes on rendering

- The HTML is for preview only; it is not Confluence storage format and cannot be pasted into Confluence directly. For actual Confluence push, use `workspace-publish-to-confluence.prompt.md`.
- Mermaid diagrams: render via mermaid.js included as a CDN script in the HTML (the HTML works offline if mermaid.js is bundled; the build-time choice is whether to inline or CDN-link)
- Obsidian-specific syntax (callouts, embeds): degrade to standard HTML where possible (callouts → styled blockquotes)

## On conversion error

If a specific file fails to convert:

- Skip that file
- Surface the error
- Continue with other files
- Report failed files at end
