# PS-CMS-Programming

Unlike a simple link-out to GitHub, this CMS allows for curated project storytelling. It uses a structured directory pattern *(Folder > MD + Assets)* to provide the site with a *Project Preview* manifest and deep-link raw resources via the GitHub CDN.

---

## Usage

### Adding a new project

1. Create a folder under `projects/` named with a kebab-case slug (e.g. `chess-app`).
2. Add a Markdown file inside it with the **same name as the folder** (e.g. `projects/chess-app/chess-app.md`). This is the main page.
3. Populate the frontmatter (see field reference below).
4. Push to `main`. The [generate-manifest](.github/workflows/generate-manifest.yml) workflow runs automatically and publishes an updated `manifest.json` to the `projects-manifest` release tag.

The stable manifest URL is always:

```
https://github.com/Broomfields/PS-CMS-Programming/releases/download/projects-manifest/manifest.json
```

Raw assets (images, etc.) are served directly from the repo:

```
https://raw.githubusercontent.com/Broomfields/PS-CMS-Programming/main/projects/{slug}/{filename}
```

### Running the manifest generator locally

```bash
pip install pyyaml
python .github/scripts/generate_manifest.py
```

---

## Image convention

All project images live in an `images/` subfolder inside the project folder:

```
projects/
└── my-project/
    ├── images/
    │   ├── 01-menu.png
    │   ├── 02-gameplay.png
    │   └── 03-end-screen.png
    └── my-project.md
```

**Naming rules:**

- Every image must have a unique name regardless of extension. Two files named `01-menu.png` and `01-menu.jpg` in the same project are not allowed — the generator will warn and use whichever it finds first.
- Use a two-digit numeric prefix to control display order: `01-`, `02-`, `03-`, etc.
- Rename screenshots when adding them — do not keep camera or OS-generated names.

In the frontmatter, `cover` and `gallery` entries use **bare names only** (no path, no extension):

```yaml
cover: "02-gameplay"
gallery:
  - "01-menu"
  - "02-gameplay"
  - "03-end-screen"
```

The manifest generator scans the `images/` directory at build time, resolves each bare name to its full filename (including extension), and writes the complete relative path into `manifest.json`.

---

## Frontmatter field reference

All fields are written in the YAML frontmatter block at the top of the main page Markdown file.

| Field | Type | Required | Description |
|---|---|---|---|
| `title` | string | yes | Display name of the project. |
| `description` | string | yes | One-sentence summary shown on the project card. |
| `date` | `YYYY-MM-DD` | yes | Completion or publish date. Used to sort the manifest (newest first). |
| `cover` | string | yes | Bare image name (no path, no extension) for the cover image (e.g. `03-game-moves`). The generator resolves the full path and extension. |
| `gallery` | list of strings | no | Ordered list of bare image names for the project gallery (e.g. `["01-menu", "02-gameplay"]`). The generator resolves each to a full path with extension. |
| `status` | string | no | Project status: `"complete"`, `"wip"`, or `"archived"`. |
| `featured` | boolean | no | Pin this project as featured (`true` / `false`). |
| `tags` | list of strings | no | Freeform tags for filtering (e.g. `["game", "mod", "cli"]`). |
| `repo` | string | no | URL of the GitHub repository being showcased. |
| `languages` | list of strings | no | Programming languages used (e.g. `["C#", "HLSL"]`). |
| `dependencies` | list of strings | no | Frameworks, libraries, engines, runtimes, or other significant dependencies (e.g. `["Love2D", ".NET 8", "Blazor"]`). |
| `license` | string | no | SPDX license identifier (e.g. `"MIT"`, `"GPL-3.0"`, `"Unlicense"`). |
| `platform` | list of strings | no | Target platform(s). Use OS names (`"Windows"`, `"Linux"`, `"macOS"`, `"iOS"`, `"Android"`), `"Web"`, `"Cross-platform"`, or a game title for mods (e.g. `"Minecraft"`). |
| `demo_url` | string | no | URL to a live or playable demo. |
| `demo_embed` | boolean | no | Whether the demo can be embedded in an iframe (`true` / `false`). |
| `links` | list of objects | no | External appearances (e.g. Modrinth, CurseForge, itch.io). Each entry has `label` and `url` (see below). |
| `credits` | list of objects | no | Third-party assets used in the project. Each entry has `label`, `author`, `url`, and optionally `license` (see below). |
| `subpages` | list of strings | no | Bare filename stems of sub-page Markdown files in the same folder (see below). |
| `files` | list of objects | no | Downloadable assets. Each entry has `name` (filename) and `label` (display text). Not included in the manifest — only used on the full project page. |

### `credits` entry shape

```yaml
credits:
  - label: "Chess piece icons"
    author: "Cburnett"
    url: "https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces"
    license: "CC BY-SA 3.0"
  - label: "Sound effects"
    author: "Kenney"
    url: "https://kenney.nl"
    license: "CC0"
```

### `links` entry shape

```yaml
links:
  - label: "Modrinth"
    url: "https://modrinth.com/mod/my-mod"
  - label: "CurseForge"
    url: "https://curseforge.com/minecraft/mc-mods/my-mod"
```

### `files` entry shape

```yaml
files:
  - name: "config-template.toml"
    label: "Config Template"
  - name: "release-notes.md"
    label: "Release Notes"
```

---

## Example frontmatter

A minimal entry:

```yaml
---
title: "Chess App"
description: "A Love2D chess implementation with full move validation and a simple AI opponent."
date: 2025-11-04
cover: "images/cover.png"
status: "complete"
repo: "https://github.com/Broomfields/chess-app"
languages: ["Lua"]
dependencies: ["Love2D"]
platform: ["Windows", "macOS", "Linux"]
license: "MIT"
---
```

A fuller entry:

```yaml
---
title: "My Minecraft Mod"
description: "Adds procedurally generated dungeons to vanilla Minecraft worlds."
date: 2024-06-15
cover: "images/cover.png"
status: "complete"
featured: true
repo: "https://github.com/Broomfields/my-minecraft-mod"
languages: ["Java"]
dependencies: ["Fabric API"]
platform: ["Minecraft"]
license: "GPL-3.0"
tags: ["mod", "game", "procedural-generation"]
links:
  - label: "Modrinth"
    url: "https://modrinth.com/mod/my-minecraft-mod"
  - label: "CurseForge"
    url: "https://curseforge.com/minecraft/mc-mods/my-minecraft-mod"
demo_url: "https://broomfields.github.io/my-minecraft-mod/demo"
demo_embed: false
subpages:
  - "design-notes"
---
```

---

## Sub-pages

A project can have one or more sub-pages for supplementary content (design notes, implementation write-ups, etc.).

**Convention:**

- Sub-pages live in the **same folder** as the main page.
- The main page is always the `.md` file that matches the folder name. Every other `.md` file in that folder is a sub-page.
- Declare sub-pages in the main page's frontmatter as bare filename stems — no `.md` extension, no path:

```yaml
subpages:
  - "design-notes"
  - "changelog"
```

- Sub-pages carry their own minimal frontmatter with a `title` and a `parent` field pointing back to the project slug:

```yaml
---
title: "Design Notes — Chess App"
parent: "chess-app"
---
```

**Internal links** to sub-pages in body Markdown use bare slugs with no extension:

```markdown
See [Design Notes](design-notes) for the architecture overview.
```

The site consumer intercepts relative links (no protocol, no leading slash) and routes them to sub-page components rather than rendering a plain `<a>` tag.
