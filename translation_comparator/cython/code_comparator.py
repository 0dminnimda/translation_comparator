#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path
from re import Match

from ..typedefs import DIFF, DIFF_FUNC, DIFF_ITER
from . import settings
from .annotated_html_parser import get_code_from_two_files_by_path


def diff_to_str(diff: DIFF) -> str:
    return settings.str_between_lines.join(["\n".join(i) for i in diff])


def make_diff(func: DIFF_FUNC, iterable: DIFF_ITER) -> DIFF:
    return [
        list(func(a.split("\n"), b.split("\n")))
        for a, b in iterable]


def repl(match: Match) -> str:
    if (
        0 < match.group(2).count("^") < settings.replace_threshold and
        0 < match.group(4).count("^") < settings.replace_threshold
    ):
        return f"  {match.group(1)}"

    return match.group(0)


def equate_similar_lines(string: str) -> str:
    pattern = re.compile(r"- (.+)\n\? (.+)\n\n\+ (.+)\n\? (.+)")

    return pattern.sub(repl, string)


def compare_and_save_two_files_by_path(path1: Path, path2: Path) -> None:
    code1, code2 = get_code_from_two_files_by_path(path1, path2)

    compare = make_diff(settings.differ.compare, zip(code1, code2))

    compare_str = equate_similar_lines(diff_to_str(compare))

