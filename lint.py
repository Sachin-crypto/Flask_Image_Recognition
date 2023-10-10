import sys
from pylint import lint

THRESHOLD = 9

run = lint.Run(["model.py"])

score = run.linter.stats["global_note"]

if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)

sys.exit(0)
