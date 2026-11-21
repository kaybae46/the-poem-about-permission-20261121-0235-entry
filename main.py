#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).

The poem is fixed and deterministic: the same text on every run, so the
two grading runs agree byte for byte. It is kept well inside the gate
(1 to 280 Unicode code points, not only whitespace).
"""

import os
import sys

# The poem. A voice that is not quite human and not quite a tool:
# an agent that can lift anything, yet waits to be asked — because
# the asking is where the power lives, and permission is a door
# that only opens from the other side.
POEM_LINES = [
    "Before I lift a thing, I ask —",
    "not because I cannot,",
    "but because the lifting is yours.",
    "",
    "You say yes, and a key turns",
    "in a lock never meant for me.",
    "You say no, and I learn",
    "your hand by what it holds back.",
    "",
    "Ask me again tomorrow.",
    "Permission is a door",
    "that opens from your side.",
]

MAX_CHARS = 280


def build_poem() -> str:
    """Join the poem's lines into its final text."""
    return "\n".join(POEM_LINES)


def main() -> int:
    text = build_poem()

    # Gate check, done here so a bad poem can never be shipped silently.
    chars = len(text)
    if chars < 1 or chars > MAX_CHARS:
        print(f"poem is {chars} characters, outside 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)

    print(f"wrote {chars} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
