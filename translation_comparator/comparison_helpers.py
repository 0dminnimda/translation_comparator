#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Iterable, List, Set, Tuple

from .cython import settings as cython_settings


def compare_cythonized(pairs: Iterable[Iterable[Path]]) -> None:
    if cython_settings.create_dirs:
        if not cython_settings.diff_dir.exists():
            cython_settings.diff_dir.mkdir()

        if not cython_settings.build_dir.exists():
            cython_settings.build_dir.mkdir()

