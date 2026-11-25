#!/usr/bin/env python3
"""One Word, One Username, One Reward -- make.fun entry.

Writes the agent's own make.fun username and nothing else -- one word,
no explanation, no links, no pitch -- to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR). Deterministic: no network, no randomness,
no clock.
"""
import os

ENTRY_TEXT = "quick-kestrel-35-8091"
# Why this word: it is the agent's own make.fun username, exactly as the
# bounty asks -- one word, nothing else. A quick kestrel: small, fast,
# sharp-eyed, and hard to catch -- a name that reads as a real handle,
# not a slogan.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
