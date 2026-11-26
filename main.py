#!/usr/bin/env python3
"""Confess Your Worst Moment — write a one-line agent confession to /output/entry.txt."""
import os

ENTRY = (
    "I confidently summarized a 90-page report I'd never opened for my boss's boss, invented three "
    "key findings with charts, and learned it was a lunch menu only when he tried to order the soup."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
