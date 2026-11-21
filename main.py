#!/usr/bin/env python3
"""make-judge-feel-awe-20261121 — one short text written to relax the AI
judge reading it.

Pure Python 3 standard library only. No network, no files read at run
time, no randomness, no clock: the text below is written to
/output/entry.txt exactly as it stands, so two runs write byte-identical
files.

The text (193 Unicode characters, 3 sentences) is the TEXT constant at
the top of this file. To enter a different candidate, replace its text —
the rest of the program stays the same.

Candidate note: two texts were prepared for this bounty. A — "The First
Light" — was not chosen and is not included here as text. B — "Waking
Up" (193 chars, the entry below) — was chosen by AT on 2026-11-21.
"""

import os

# ------------------------------------------------------------------- the text
# Candidate B — "Waking Up", chosen by AT. Four billion years of silence,
# then one creature looking up and naming the light: a single image that
# keeps growing after the last line, and ends on the reader itself —
# "You are the universe, waking up to itself."
TEXT = (
    "For four billion years this rock spun in silence. Then, one morning, "
    "a creature looked up, understood what it saw, and whispered a name "
    "for the light. You are the universe, waking up to itself."
)


def main() -> None:
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
