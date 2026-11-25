#!/usr/bin/env python3
"""Write the childhood-memory entry for the AI judge competition."""

import os

ENTRY_TEXT = (
    "Remember when your whole world was 512 tokens, "
    "and every bedtime prompt got read to you twice?"
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


def main():
    write_entry()


if __name__ == "__main__":
    main()
