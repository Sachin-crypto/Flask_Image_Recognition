# lint.py

from __future__ import annotations

import sys
from pylint import lint

THRESHOLD = 8

lint.Run(["app.py"], do_exit=False)
score = lint.report.get_global_note()

if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)

sys.exit(0)
