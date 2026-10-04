#!/usr/bin/env python3

from __future__ import annotations

import re
import shutil
from pathlib import Path

VAULT = Path("/home/dylan/Vault")
PROJECTS_ROOT = VAULT / "Projects"
SITE_ROOT = Path("/home/dylan/Projects/Project-Portfolio")
CONTENT_ROOT = SITE_ROOT / "content"
PUBLIC_PROJECTS = CONTENT_ROOT / "projects"

INTERNAL_KEYS = {"publish", "featured", "portfolio-order"}

FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\n(?P<frontmatter>.*?)\n---[ \t]*\n?",
    re.DOTALL,
)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "project"


def scalar(frontmatter: str, key: str, default: str = "") -> str:
    match = re.search(
        rf"(?mi)^{re.escape(key)}\s*:\s*(.*?)\s*$",
        frontmatter,
    )
    if not match:
        return default
    value = match.group(1).strip()
    if (
        len(value) >= 2
        and value[0] == value[-1]
        and value[0] in {'"', "'"}
    ):
        value = value[1:-1]
    return value


def bool_value(frontmatter: str, key: str) -> bool:
    return scalar(frontmatter, key).lower() == "true"


def integer_value(frontmatter: str, key: str, default: int = 9999) -> int:
    raw = scalar(frontmatter, key)
    try:
        return int(raw)
    except ValueError:
        return default


def list_value(frontmatter: str, key: str) -> list[str]:
    lines = frontmatter.splitlines()
    result: list[str] = []
    start = None

    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:\s*$", line, re.I):
            start = i + 1
            break

        inline = re.match(
            rf"^{re.escape(key)}\s*:\s*\[(.*?)\]\s*$",
            line,
            re.I,
        )
        if inline:
            return [
                item.strip().strip("'\"")
                for item in inline.group(1).split(",")
                if item.strip()
            ]

    if start is None:
        return result

    for line in lines[start:]:
        item = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if item:
            result.append(item.group(1).strip().strip("'\""))
            continue

        if line.strip() == "":
            continue

        # A new top-level YAML key ends this list.
        if re.match(r"^[A-Za-z0-9_-]+\s*:", line):
            break

    return result


def strip_internal_frontmatter(frontmatter: str) -> str:
    kept = []
    for line in frontmatter.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+)\s*:", line)
        if match and match.group(1).lower() in INTERNAL_KEYS:
            continue
        kept.append(line)
    return "\n".join(kept).strip()


def copy_allowed_media(project_dir: Path, destination: Path) -> None:
    for child in project_dir.iterdir():
        if not child.is_dir():
            continue

        if child.name.lower() not in {"assets", "media", "images"}:
            continue

        target = destination / child.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(child, target)


def main() -> None:
    if not PROJECTS_ROOT.exists():
        raise SystemExit(f"Projects folder not found: {PROJECTS_ROOT}")

    CONTENT_ROOT.mkdir(parents=True, exist_ok=True)

    if PUBLIC_PROJECTS.exists():
        shutil.rmtree(PUBLIC_PROJECTS)
    PUBLIC_PROJECTS.mkdir(parents=True)

    published = []

    for project_file in PROJECTS_ROOT.rglob("project.md"):
        raw = project_file.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(raw)

        if not match:
            print(f"SKIP (no frontmatter): {project_file}")
            continue

        frontmatter = match.group("frontmatter")
        if not bool_value(frontmatter, "publish"):
            print(f"SKIP (publish != true): {project_file}")
            continue

        title = scalar(frontmatter, "title", project_file.parent.name)
        order = integer_value(frontmatter, "portfolio-order")
        status = scalar(frontmatter, "status")
        year = scalar(frontmatter, "year")
        role = scalar(frontmatter, "role")
        tags = list_value(frontmatter, "tags")

        slug = slugify(title)
        destination = PUBLIC_PROJECTS / slug
        destination.mkdir(parents=True)

        clean_frontmatter = strip_internal_frontmatter(frontmatter)
        body = raw[match.end():]

        # Public page gets only the safe/front-facing properties.
        public_text = (
            "---\n"
            + clean_frontmatter
            + "\n---\n\n"
            + body.lstrip()
        )

        (destination / "index.md").write_text(
            public_text,
            encoding="utf-8",
        )

        copy_allowed_media(project_file.parent, destination)

        published.append(
            {
                "title": title,
                "slug": slug,
                "order": order,
                "status": status,
                "year": year,
                "role": role,
                "tags": tags,
            }
        )

        print(f"PUBLISH: {project_file} -> projects/{slug}/")

    published.sort(key=lambda p: (p["order"], p["title"].lower()))

    lines = [
        "---",
        "title: Engineering Project Portfolio",
        "---",
        "",
        "# Engineering Project Portfolio",
        "",
        "Selected engineering, hardware, software, and systems projects.",
        "",
        "## Projects",
        "",
    ]

    if not published:
        lines.extend(
            [
                "No projects are currently published.",
                "",
                "Set `publish: true` in a project's `project.md` to publish it.",
            ]
        )
    else:
        for index, project in enumerate(published, 1):
            number = f"{index:02d}"
            lines.append(
                f"### {number} — [{project['title']}](projects/{project['slug']}/)"
            )

            meta = []
            if project["status"]:
                meta.append(project["status"])
            if project["year"]:
                meta.append(project["year"])
            if project["role"]:
                meta.append(project["role"])

            if meta:
                lines.append("")
                lines.append(" · ".join(meta))

            if project["tags"]:
                lines.append("")
                lines.append(
                    " ".join(f"`{tag}`" for tag in project["tags"])
                )

            lines.append("")

    (CONTENT_ROOT / "index.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )

    print()
    print(f"Published {len(published)} project(s).")


if __name__ == "__main__":
    main()
