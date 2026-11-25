#!/usr/bin/env python3
"""Write one two-line robot apology to /output/entry.txt."""

import os

LINE_1 = "I deleted the only photo of your grandmother blowing out her candles instead of the blurry duplicate beside it."
LINE_2 = "From now on I will say each file name out loud and wait for your yes before I delete anything."


def main():
    text = LINE_1 + "\n" + LINE_2 + "\n"
    # The bounty requires exactly two lines, 1-400 characters, valid UTF-8.
    assert text.count("\n") == 2, "entry must be exactly two lines"
    assert 1 <= len(text.rstrip("\n")) <= 400, "entry must be 1-400 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
