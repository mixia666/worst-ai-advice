#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes the single worst piece of AI advice (delivered, of course, with
total confidence) to /output/entry.txt (or to the path given as argv[1]).
"""

import sys
from pathlib import Path

LINE = (
    "Getting 47 compile errors? Just delete the compiler. No compiler, "
    "no errors. I am an AI, and I have literally never been wrong "
    "about anything."
)


def main() -> None:
    # The gate only accepts a single line of 1-200 characters: check the
    # line before writing so a bad edit fails loudly here, not at judging.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} characters"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader collects the output as a different user: keep it readable.
    out.chmod(0o644)


if __name__ == "__main__":
    main()
