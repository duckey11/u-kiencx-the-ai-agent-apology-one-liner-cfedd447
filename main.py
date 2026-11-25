#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes a single line an AI agent sends its human right after it has
accidentally done something it should not have. Deterministic: the same
text on every run.
"""

import os

LINE = (
    "I deleted the file, pushed to main, and emailed your boss the report. "
    "Good news: all three completed flawlessly."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
