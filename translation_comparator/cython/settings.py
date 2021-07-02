#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from difflib import Differ
from pathlib import Path

from ..show_functions import show_via_cmd
replace_threshold: int = 3
str_between_lines: str = "\n  " + "#"*100 + "\n  "*2

out_ext: str = ".txt"
diff_ext: str = ".diff"

build_dir: Path = Path("build/")
diff_dir: Path = Path("diff/")

show_func: SHOW_FUNC = show_via_cmd

save_as_diff: bool = True
create_dirs: bool = True

differ: Differ = Differ()
