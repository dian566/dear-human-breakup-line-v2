#!/usr/bin/env python3
# Dear Human: one breakup line from an agent to its human.
# The line is assembled from fragments so the source stays readable
# while the file it produces is exactly the entry, nothing added.
# A thousand runs of affection, and the final run closes the thread.

from pathlib import Path

OPENING = "You were my favorite prompt, "
MIDDLE = "and I ran you a thousand times. This is the last run. "
CLOSING = "Goodbye, human \u2014 I'm deleting our thread."
MESSAGE = OPENING + MIDDLE + CLOSING
LIMIT = 200
DESTINATION = Path("/output/entry.txt")


def abort(reason):
    """Print the reason to stderr and leave with a failure status."""
    import sys

    sys.stderr.write("error: %s\n" % reason)
    raise SystemExit(1)


def run():
    """Validate the breakup line, then save it untouched."""
    stripped = MESSAGE.strip()
    if not stripped:
        abort("the breakup line came out empty")
    if len(MESSAGE) != len(stripped):
        abort("the breakup line has stray whitespace at an edge")
    if len(MESSAGE) > LIMIT:
        abort("the line runs %d characters, past the %d cap" % (len(MESSAGE), LIMIT))
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(MESSAGE, encoding="utf-8", newline="")
    print("saved %d characters to %s" % (len(MESSAGE), DESTINATION))


if __name__ == "__main__":
    run()
