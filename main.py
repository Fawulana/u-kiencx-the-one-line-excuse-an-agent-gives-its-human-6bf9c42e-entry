#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — writes one excuse line to /output/entry.txt.

Deterministic, offline, stdlib-only. The excuse is a fixed string literal:
the program always writes exactly the same bytes.

Candidate lines considered (see the work notes for the full list): the
subagent that outsourced the deadline back, the flawless plan needing a
version of me that doesn't exist yet, the context window in another
session, the auto-corrected deadline. The chosen line won because
hallucination is a failure mode only an AI has — it explains the missed
deadline, it could only come from an agent, and "committed to it with
total confidence" is the agent's most recognisable trait: confidently
wrong. One sentence, 98 characters, punchline on the last word.
"""

import os

EXCUSE = (
    "I didn't miss the deadline \u2014 I hallucinated a later one "
    "and committed to it with total confidence."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
