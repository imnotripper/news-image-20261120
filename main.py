"""make.fun entry for news-image-20261120: sum up 20 November 2026 in one image.

The repository holds the finished image as entry.png beside this file; the
program copies it, byte for byte, to the output directory. Python 3 standard
library only, no network, deterministic: every run writes the same bytes.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    # Output directory: first command-line argument wins, then
    # $MAKEFUN_OUTPUT_DIR, then the grader's /output.
    if len(sys.argv) > 1:
        out_dir = Path(sys.argv[1])
    else:
        out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
