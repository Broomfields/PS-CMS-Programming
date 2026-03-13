"""
generate_manifest.py

Walks the projects/ directory, reads the frontmatter from each project's
Markdown file, and writes a manifest.json at the repo root.

Each project folder is expected to contain a Markdown file with the same
name as the folder (e.g. projects/chess-app/chess-app.md).
Folders without a matching Markdown file are skipped with a warning.

The manifest is sorted by date descending (newest project first).
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECTS_DIR = REPO_ROOT / "projects"
OUTPUT_FILE = REPO_ROOT / "manifest.json"

# Frontmatter fields to include in each card entry.
# 'files' is intentionally excluded — it belongs to the full project page, not the card.
CARD_FIELDS = [
    "title",
    "description",
    "date",
    "cover",
    "gallery",
    "status",
    "featured",
    "tags",
    "repo",
    "languages",
    "dependencies",
    "license",
    "platform",
    "demo_url",
    "demo_embed",
    "links",
    "credits",
    "subpages",
]


def parse_frontmatter(md_path: Path) -> dict | None:
    """
    Extract YAML frontmatter from a Markdown file.
    Returns a dict, or None if frontmatter is absent or malformed.
    """
    text = md_path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        print(f"  [skip] No frontmatter found in {md_path.relative_to(REPO_ROOT)}")
        return None

    # Find the closing '---'
    end = text.find("\n---", 3)
    if end == -1:
        print(f"  [skip] Unclosed frontmatter in {md_path.relative_to(REPO_ROOT)}")
        return None

    raw_yaml = text[3:end].strip()

    try:
        return yaml.safe_load(raw_yaml)
    except yaml.YAMLError as exc:
        print(f"  [skip] YAML parse error in {md_path.relative_to(REPO_ROOT)}: {exc}")
        return None


def resolve_image(project_dir: Path, bare_name: str) -> str | None:
    """
    Given a bare image name (no extension, no path), find the matching file
    in the project's images/ subdirectory and return its relative path
    (e.g. 'images/03-game-moves.png').

    Returns None and prints a warning if no match is found.
    Multiple files with the same stem are an error — the convention requires
    unique names regardless of extension.
    """
    images_dir = project_dir / "images"
    if not images_dir.is_dir():
        print(f"  [warn] No images/ directory in {project_dir.name} — cannot resolve '{bare_name}'")
        return None

    matches = [f for f in images_dir.iterdir() if f.is_file() and f.stem == bare_name]

    if not matches:
        print(f"  [warn] Image not found for bare name '{bare_name}' in {project_dir.name}/images/")
        return None

    if len(matches) > 1:
        names = ", ".join(f.name for f in matches)
        print(f"  [warn] Multiple files match '{bare_name}' in {project_dir.name}/images/: {names} — using first")

    return f"images/{matches[0].name}"


def build_card(slug: str, frontmatter: dict, project_dir: Path) -> dict:
    """Build a single card entry from a slug and its parsed frontmatter."""
    card = {"slug": slug}
    for field in CARD_FIELDS:
        if field in frontmatter:
            value = frontmatter[field]
            # Normalise date to ISO string for consistent JSON serialisation
            if field == "date" and hasattr(value, "isoformat"):
                value = value.isoformat()
            # Resolve bare image names to full relative paths with extension
            elif field == "cover" and isinstance(value, str):
                value = resolve_image(project_dir, value) or value
            elif field == "gallery" and isinstance(value, list):
                value = [resolve_image(project_dir, name) or name for name in value]
            card[field] = value
    return card


def main():
    if not PROJECTS_DIR.is_dir():
        print(f"Error: projects directory not found at {PROJECTS_DIR}", file=sys.stderr)
        sys.exit(1)

    projects = []

    for project_dir in sorted(PROJECTS_DIR.iterdir()):
        if not project_dir.is_dir():
            continue
        if project_dir.name.startswith("."):
            continue

        slug = project_dir.name
        md_path = project_dir / f"{slug}.md"

        if not md_path.exists():
            print(f"  [skip] No markdown file for project: {slug}")
            continue

        print(f"  [read] {md_path.relative_to(REPO_ROOT)}")
        frontmatter = parse_frontmatter(md_path)
        if frontmatter is None:
            continue

        card = build_card(slug, frontmatter, project_dir)
        projects.append(card)

    # Sort newest first; fall back gracefully if 'date' is missing
    projects.sort(key=lambda p: p.get("date", ""), reverse=True)

    manifest = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "count": len(projects),
        "projects": projects,
    }

    OUTPUT_FILE.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nManifest written to {OUTPUT_FILE.relative_to(REPO_ROOT)} ({len(projects)} project(s))")


if __name__ == "__main__":
    main()
