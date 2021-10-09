#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from difflib import restore
from pathlib import Path
from re import Match
from typing import Iterable, List

from ..path_helpers import change_same_paths_if_needed
from ..typedefs import DIFF_FUNC
from . import settings
from .annotated_html_parser import get_code_from_two_files_by_path


def chunks_to_lines(chunks: Iterable[str]) -> List[str]:
    return settings.str_between_lines.join(chunks).split("\n")


def diff_of_several(func: DIFF_FUNC,
                    a: Iterable[str], b: Iterable[str]) -> str:
    return "\n".join(func(chunks_to_lines(a), chunks_to_lines(b)))


def write_restored_diff(path: Path, lines: Iterable[str]) -> None:
    build_out_path(path).write_text("\n".join(lines))


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


def build_diff_path(path1: Path, path2: Path) -> Path:
    return settings.diff_dir.joinpath(
        path1.stem + "+" + path2.stem).with_suffix(settings.diff_ext)


def build_out_path(path: Path) -> Path:
    return settings.diff_dir.joinpath(
        path.name).with_suffix(settings.out_ext)


def compare_and_save_two_files_by_path(path1: Path, path2: Path) -> None:
    code1, code2 = get_code_from_two_files_by_path(path1, path2)

    compare_result = diff_of_several(settings.differ.compare, code1, code2)
    comparison_str = equate_similar_lines(compare_result)

    path1, path2 = change_same_paths_if_needed(path1, path2)
    if settings.save_as_diff:
        build_diff_path(path1, path2).write_text(comparison_str)
    else:
        split = comparison_str.split("\n")
        write_restored_diff(path1, restore(split, 1))
        write_restored_diff(path2, restore(split, 2))


def compare_and_save_two_files(file1: str, file2: str) -> None:
    return compare_and_save_two_files_by_path(Path(file1), Path(file2))
