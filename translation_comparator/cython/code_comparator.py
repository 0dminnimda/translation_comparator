#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

from ..typedefs import DIFF, DIFF_FUNC, DIFF_ITER
from . import settings
from .annotated_html_parser import get_code_from_two_files_by_path


def make_diff(func: DIFF_FUNC, iterable: DIFF_ITER) -> DIFF:
    return [
        list(func(a.split("\n"), b.split("\n")))
        for a, b in iterable]


def compare_and_save_two_files_by_path(path1: Path, path2: Path) -> None:
    code1, code2 = get_code_from_two_files_by_path(path1, path2)

    compare = make_diff(settings.differ.compare, zip(code1, code2))

