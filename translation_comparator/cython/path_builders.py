#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Tuple


def build_via_suffix_change(path: Path) -> Tuple[Path, Path]:
    "'path.py*' -> 'path.py', 'path.pyx'"
    return path.with_suffix(".py"), path.with_suffix(".pyx")


def unique_stem_via_suffix(path: Path) -> Path:
    return path.with_stem(path.stem + "_" + path.suffix[1:])
