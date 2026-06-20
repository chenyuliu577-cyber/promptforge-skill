#!/usr/bin/env python3
"""Simple local linter for prompt documents."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CHECKS = {
    "goal": {
        "patterns": [r"\bgoal\b", r"\bobjective\b", r"\btask analysis\b"],
        "suggestion": "Add a clear objective or task analysis section.",
    },
    "input": {
        "patterns": [r"\binput[s]?\b", r"\bsource\b", r"\bcontext\b", r"\bprovided\b"],
        "suggestion": "State the available inputs, source material, or context.",
    },
    "output format": {
        "patterns": [r"\boutput format\b", r"\bdeliverable\b", r"\bfinal prompt\b"],
        "suggestion": "Define the required deliverable or final output structure.",
    },
    "constraints": {
        "patterns": [r"\bconstraint[s]?\b", r"\brequirement[s]?\b", r"\bscope\b"],
        "suggestion": "Add requirements, scope limits, or other constraints.",
    },
    "prohibitions": {
        "patterns": [r"\bdo not\b", r"\bavoid\b", r"\bmust not\b", r"\bprohibited\b"],
        "suggestion": "List actions or output behaviors that are not allowed.",
    },
    "quality standards": {
        "patterns": [r"\bquality\b", r"\bsuccess criteria\b", r"\bacceptance criteria\b"],
        "suggestion": "Add quality standards or acceptance criteria.",
    },
    "checklist": {
        "patterns": [r"\bchecklist\b", r"\bverification\b", r"\breview\b"],
        "suggestion": "Add a verification checklist or review step.",
    },
    "risk control": {
        "patterns": [r"\brisk\b", r"\bsafety\b", r"\bconfirmation\b", r"\bprivacy\b"],
        "suggestion": "Add risk controls, privacy rules, or confirmation gates.",
    },
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def has_any_pattern(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def score_prompt(text: str) -> tuple[int, list[str]]:
    missing = [
        name
        for name, check in CHECKS.items()
        if not has_any_pattern(text, check["patterns"])
    ]
    score = round(((len(CHECKS) - len(missing)) / len(CHECKS)) * 10)
    return score, missing


def print_recommendations(missing: list[str]) -> None:
    if not missing:
        print("Improvement suggestions: none")
        return

    print("Improvement suggestions:")
    for item in missing:
        print(f"- {CHECKS[item]['suggestion']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a prompt markdown or text file.")
    parser.add_argument("file", help="Path to a .txt or .md file")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    if path.suffix.lower() not in {".txt", ".md"}:
        print("Only .txt or .md files are supported.", file=sys.stderr)
        return 1

    text = read_text(path)
    if not text.strip():
        print(f"File is empty: {path}", file=sys.stderr)
        return 1

    score, missing = score_prompt(text)

    print(f"Prompt file: {path}")
    print(f"Score: {score}/10")
    if missing:
        print("Missing items:")
        for item in missing:
            print(f"- {item}")
    else:
        print("Missing items: none")
    print_recommendations(missing)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
