#!/usr/bin/env python3
"""Run the prompt linter against project examples and tests."""

from __future__ import annotations

import sys
from pathlib import Path

from prompt_linter import read_text, score_prompt


MIN_SCORE = 8
TARGET_DIRS = [
    Path("skill/promptforge/examples"),
    Path("tests"),
]


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for directory in TARGET_DIRS:
        if not directory.exists():
            print(f"Missing directory: {directory}", file=sys.stderr)
            continue
        files.extend(sorted(directory.glob("*.md")))
    return files


def main() -> int:
    files = iter_markdown_files()
    if not files:
        print("No markdown files found.", file=sys.stderr)
        return 1

    passed = 0
    failed = 0

    for path in files:
        text = read_text(path)
        if not text.strip():
            print(f"{path}: FAIL empty file")
            failed += 1
            continue

        score, missing = score_prompt(text)
        status = "PASS" if score >= MIN_SCORE else "FAIL"
        missing_text = "none" if not missing else ", ".join(missing)
        print(f"{path}: {status} {score}/10 missing: {missing_text}")

        if score >= MIN_SCORE:
            passed += 1
        else:
            failed += 1

    print(f"Summary: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
