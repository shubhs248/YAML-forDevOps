#!/usr/bin/env python3
"""
check.py - validate a YAML file and show its structure.

Run it on any YAML file to get instant feedback:

    python check.py 02-fix-the-yaml/broken-1-indentation.yaml

If the file is INVALID, it prints a clear error with the line and column.
If the file is VALID, it prints a short tree of what the YAML contains, so you
can confirm it parsed into the shape you expected.

Supports multi-document files (those that use '---' to separate documents).

Requires PyYAML:  pip install -r requirements.txt
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is not installed.")
    print("Install it with:  pip install -r requirements.txt")
    sys.exit(2)


def describe(value, indent: int = 0) -> None:
    """Print a short, readable tree of the parsed YAML."""
    pad = "  " * indent
    if isinstance(value, dict):
        for key, val in value.items():
            if isinstance(val, (dict, list)):
                print(f"{pad}{key}:")
                describe(val, indent + 1)
            else:
                print(f"{pad}{key}: {val!r}  ({type(val).__name__})")
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, (dict, list)):
                print(f"{pad}-")
                describe(item, indent + 1)
            else:
                print(f"{pad}- {item!r}  ({type(item).__name__})")
    else:
        print(f"{pad}{value!r}  ({type(value).__name__})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a YAML file.")
    parser.add_argument("file", help="path to the YAML file to check")
    parser.add_argument("--quiet", action="store_true",
                        help="only say valid/invalid, do not print the structure")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(2)

    text = path.read_text(encoding="utf-8")

    try:
        documents = list(yaml.safe_load_all(text))
    except yaml.YAMLError as error:
        print(f"[INVALID] {path} - this is NOT valid YAML")
        # PyYAML attaches a 'problem_mark' with line/column for most errors.
        mark = getattr(error, "problem_mark", None)
        if mark is not None:
            problem = getattr(error, "problem", "syntax error")
            print(f"   Problem: {problem}")
            print(f"   Near line {mark.line + 1}, column {mark.column + 1}")
        else:
            print(f"   {error}")
        sys.exit(1)

    doc_count = len(documents)
    print(f"[VALID] {path} - parsed OK ({doc_count} document{'s' if doc_count != 1 else ''})")

    if not args.quiet:
        for i, doc in enumerate(documents, start=1):
            if doc_count > 1:
                print(f"\n--- document {i} ---")
            describe(doc)


if __name__ == "__main__":
    main()
