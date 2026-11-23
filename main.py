#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner (at most 200 characters) describing a
hilariously useless superpower to /output/entry.txt.

The line takes the familiar power of flight and turns it somewhere new with
three stacked qualifiers, so the joke pays off in the last few words and the
uselessness stays specific and easy to picture: three inches up, walking
speed, and only on days going nowhere anyway.

Deterministic, standard library only, no network, no randomness.
"""

import os
from pathlib import Path

# Entry: 116 chars, 118 bytes, 1 line.
# Gate: 1-200 chars, one line, UTF-8.
ENTRY = (
    "I can fly — but only three inches off the ground, at walking speed, "
    "and only on days I wasn't going anywhere anyway."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} chars to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
