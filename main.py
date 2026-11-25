#!/usr/bin/env python3
"""Make the AI Judge Laugh — office-life joke entry.

The observation: the office "quick sync" is never quick. Everyone
knows it, everyone still books it, and the calendar is the only
honest witness. The twist lands in the last few words: the meeting
that was meant to save time now needs a second meeting to explain
why the first one ate the whole morning.
"""

import os


def build_joke() -> str:
    """Return the single office-life joke line."""
    return "The 15-minute sync ran 90 minutes, so now we need a meeting to discuss why the meeting ran long."


def main() -> None:
    line = build_joke()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
