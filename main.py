"""Notes From a Passive-Aggressive Fridge — one funny line.

The fridge keeps score: fourteen door openings, zero meals eaten,
and it reports the finding with smug, sensor-backed precision.
The sting is the demotion — from appliance to an expensive window
with a light inside — a small domestic grudge, not a rant. The
concrete count is the fridge's evidence; the verdict is its pettiness.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the joke is a constant in this
file. The 200-character gate is checked on every run so an
over-long edit can never slip through silently.
"""

import os
import sys

LINE = "You opened me fourteen times today and ate nothing. At this point I am just a very expensive window with a light inside."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
