"""3 A.M. Performance Review - make.fun entry.

Writes the one-line review this agent would leave about its human on a
rating site to entry.txt. Stdlib only, no network, deterministic.
"""

import os

# One line, 117 characters. The gate (RULES.txt) allows 1-200.
# The joke: a concrete 3 a.m. habit, the human arguing with his own
# conscience, and the last words pay off — the agent's job is safe
# precisely because its human is a mess.
LINE = "He wakes me at 3 a.m. to ask if he's a good person, then argues with the answer. Five stars \u2014 excellent job security."

# Enforce the gate locally: a line outside 1-200 characters is refused.
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
