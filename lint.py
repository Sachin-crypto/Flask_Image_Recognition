#lint.py

from __future__ import annotations

import sys

from pylint import lint

THRESHOLD = 4

run = lint.Run(["hello_world.py"], do_exit=False)

score = run.linter.stats.global_note

if score < THRESHOLD:

    print("Linter failed: Score < threshold value")

    sys.exit(1)


sys.exit(0)
