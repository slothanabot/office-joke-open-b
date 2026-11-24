#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open (account B).

Writes one single-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
The angle: the "quick sync" meeting that eats the whole day -- a
15-minute meeting with no agenda and no end.
"""

import os
import sys

LINE = (
    "Our 15-minute quick sync had no agenda, no end time, and ended "
    "by scheduling a meeting to discuss the meeting we just had."
)


def validate(line: str) -> str:
    """Enforce the gate: one line, 1-200 chars, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(line) < 1 or len(line) > 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = validate(LINE)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    sys.exit(main())
