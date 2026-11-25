#!/usr/bin/env python3
"""One Star for Monday entry (make.fun).

Writes exactly one review line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python stdlib only, no dependencies.

The review: a one-star restaurant review of Monday -- no table at nine,
coffee like burnt emails, a waiter who vanishes for eight hours, and a
bill that turns out to be Monday itself.
"""

import os

REVIEW = "Arrived at nine, no table, coffee tasted like burnt emails, waiter vanished for eight hours, then handed us the bill: Monday."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Gate: exactly one line, 1-180 chars, at most 25 words, no newline.
    assert "\n" not in REVIEW, "review must be a single line"
    assert 1 <= len(REVIEW) <= 180, f"review length {len(REVIEW)} out of gate range"
    assert len(REVIEW.split()) <= 25, f"review has {len(REVIEW.split())} words, over 25"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    # Read-back check: the file on disk must be byte-identical to REVIEW.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == REVIEW, "written entry does not match REVIEW"
    print(f"Wrote {len(REVIEW)} chars, {len(REVIEW.split())} words to {path}")


if __name__ == "__main__":
    main()
