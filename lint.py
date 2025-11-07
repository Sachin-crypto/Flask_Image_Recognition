"""Run pylint on all Python files in the project and enforce a score threshold."""

import sys
import glob
from pylint.lint import Run

THRESHOLD = 9

python_files = [
    f for f in glob.glob("../SQ3-GROUP-8/**/*.py", recursive=True)
    if "sq3env" not in f and "__pycache__" not in f and "site-packages" not in f
]

if not python_files:
    print("No Python files found!")
    sys.exit(0)

print(f"{len(python_files)} Python files.\n")  # This shows the py files

run = Run(python_files)
SCORE = getattr(run.linter.stats, "global_note", 0)  # renamed to conform to constant style

if SCORE < THRESHOLD:
    print(f"\nLinter failed: Score {SCORE:.2f}/10 < threshold ({THRESHOLD})")
    sys.exit(1)

print(f"\nLinter passed! Global score: {SCORE:.2f}/10")
sys.exit(0)
