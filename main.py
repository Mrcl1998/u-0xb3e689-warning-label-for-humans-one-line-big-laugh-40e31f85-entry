#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the single-line entry to /output/entry.txt (no trailing newline).
Pure standard library. The grader runs this as uid 65534 on a read-only
repo with /output as a root-owned bind mount, so: write the file, chmod
the FILE 0o644, and never chmod the /output directory itself.
"""

import os

ENTRY = 'WARNING: Will say "I\'m fine" while visibly on fire. Offer snacks, not advice.'

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    # Sanity: one line, inside the 160-character limit.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, limit is 160"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The file must be readable by the different uid that reads /output.
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
