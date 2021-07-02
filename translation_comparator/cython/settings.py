#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from difflib import Differ
from pathlib import Path

replace_threshold: int = 3
str_between_lines: str = "\n  " + "#"*100 + "\n  "*2

out_ext: str = ".txt"
diff_ext: str = ".diff"

build_dir: Path = Path("build/")
diff_dir: Path = Path("diff/")


create_dirs: bool = True

differ: Differ = Differ()
