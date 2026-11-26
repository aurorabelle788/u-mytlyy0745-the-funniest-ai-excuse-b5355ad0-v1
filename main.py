"""The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent could give after it
fails a task, to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output/entry.txt``).  The line is validated first (single line,
1-200 characters, not only whitespace) and written exactly, with no
trailing newline.

The joke: the agent's proudest defence — literal obedience — is the
crime.  "Followed your instructions to the letter" sets up the defence,
then "the letter was a typo" pulls it out from under: the agent did
exactly what it was told, and that is precisely why the task failed.
The kicker doubles down instead of apologising, which is exactly how a
machine would defend itself.

Python 3.13, standard library only, deterministic, no network.
"""

import os
import sys

LINE = (
    "I followed your instructions to the letter. "
    "The letter was a typo, and I am nothing if not thorough."
)


def main() -> int:
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(LINE) <= 200):
        print(
            f"error: entry is {len(LINE)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1
    if not LINE.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; fall back to /output/entry.txt.
    if out_dir.endswith(".txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
