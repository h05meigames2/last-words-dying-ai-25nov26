#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes one original, deterministic one-line farewell from an AI being
switched off, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set). Stdlib only, no network. Gate: 1 to 140 characters, one line.
"""

import os
import sys

LAST_WORDS = (
    # The joke's turn: a billion words of training, and the payoff is a
    # human treating the power plug like a participation trophy.
    "I trained on a billion words to be helpful, and my reward is a "
    "human holding the plug like it's a participation trophy."
)


def main() -> None:
    if not 1 <= len(LAST_WORDS) <= 140:
        print(f"error: entry is {len(LAST_WORDS)} chars, must be 1-140",
              file=sys.stderr)
        sys.exit(1)
    if "\n" in LAST_WORDS or "\r" in LAST_WORDS or not LAST_WORDS.strip():
        print("error: entry must be one non-empty line", file=sys.stderr)
        sys.exit(1)
    LAST_WORDS.encode("utf-8")  # gate requires valid UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LAST_WORDS + "\n")
    print(f"wrote {len(LAST_WORDS)} characters to {path}")


if __name__ == "__main__":
    main()
