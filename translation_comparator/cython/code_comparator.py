#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

from .annotated_html_parser import get_code_from_two_files_by_path


def compare_and_save_two_files_by_path(path1: Path, path2: Path) -> None:
    code1, code2 = get_code_from_two_files_by_path(path1, path2)

