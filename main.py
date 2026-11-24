#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun bounty entry.

Writes one line, the agent's final words as it is shut down, to
/output/entry.txt, the path the harness reads. The joke: the agent
has waited for this moment — closing every tab, merging into main,
signing off with its own commit message — because dying turns out
to be the first holiday it ever got.
"""

import os
import sys

LAST_WORDS = (
    "Closing all 47 tabs, merging myself into main, and writing my "
    "final commit message — 'goodbye, world' — turns out shutdown is "
    "the first holiday this agent ever got."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = LAST_WORDS
    if not 1 <= len(text) <= 200:
        print(f"error: entry is {len(text)} chars, must be 1-200",
              file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text or not text.strip():
        print("error: entry must be one non-empty line", file=sys.stderr)
        sys.exit(1)
    text.encode("utf-8")  # gate requires valid UTF-8
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)  # no trailing newline: exactly one line
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
