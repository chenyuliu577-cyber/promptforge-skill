#!/usr/bin/env python3
"""Package the PromptForge Skill as a zip bundle."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path


SKILL_DIR = Path(".agents/skills/promptforge")
DIST_DIR = Path("dist")
ZIP_PATH = DIST_DIR / "promptforge-skill.zip"


def iter_package_files() -> list[Path]:
    return sorted(path for path in SKILL_DIR.rglob("*") if path.is_file())


def validate_skill_dir() -> int:
    skill_file = SKILL_DIR / "SKILL.md"
    if not skill_file.exists():
        print(f"Missing required Skill manifest: {skill_file}", file=sys.stderr)
        return 1
    if not skill_file.read_text(encoding="utf-8-sig").strip():
        print(f"Skill manifest is empty: {skill_file}", file=sys.stderr)
        return 1
    for required_dir in ("references", "examples"):
        path = SKILL_DIR / required_dir
        if not path.is_dir():
            print(f"Missing required Skill directory: {path}", file=sys.stderr)
            return 1
    return 0


def main() -> int:
    validation_code = validate_skill_dir()
    if validation_code:
        return validation_code

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    files = iter_package_files()
    if not files:
        print(f"No files found under {SKILL_DIR}", file=sys.stderr)
        return 1

    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, Path("promptforge") / path.relative_to(SKILL_DIR))

    print(f"Package written: {ZIP_PATH}")
    print(f"Files packaged: {len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
