#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from difflib import Differ
from pathlib import Path

replace_threshold: int = 3
str_between_lines: str = "\n  " + "#"*100 + "\n  "*2

out_ext: str = ".txt"
diff_ext: str = ".diff"

diff_dir: Path = Path("diff/")


differ: Differ = Differ()
