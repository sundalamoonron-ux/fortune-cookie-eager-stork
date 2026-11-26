#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune-cookie line for a software engineer to /output/entry.txt.
Gate: UTF-8 text, 1-120 characters, not whitespace-only.
"""

import os

LINE = "Your lucky numbers are 404, 404, 404, and 404. The cookie has left the chat."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert LINE.strip(), "line must not be whitespace-only"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the file must contain exactly the line, byte for byte.
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch: entry.txt does not match the line"
    assert "\n" not in written, "entry must be a single line"
    print(f"Wrote {len(LINE)} characters to {OUT_PATH} (read-back verified)")


if __name__ == "__main__":
    main()
