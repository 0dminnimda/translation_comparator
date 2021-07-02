#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from difflib import Differ
replace_threshold: int = 3
str_between_lines: str = "\n  " + "#"*100 + "\n  "*2


differ: Differ = Differ()
