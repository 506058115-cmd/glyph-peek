#!/usr/bin/env python3
"""Show Unicode details for each code point in a string."""

import argparse
import unicodedata


def main(argv=None):
    parser = argparse.ArgumentParser(description="检查文字中的 Unicode 字符。")
    parser.add_argument("text", help="要检查的文字；含空格时请用引号括起")
    args = parser.parse_args(argv)

    for index, char in enumerate(args.text):
        name = unicodedata.name(char, "未命名字符")
        print(
            f"{index:>3}  U+{ord(char):04X}  {unicodedata.category(char)}  "
            f"{name}  {char!r}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
