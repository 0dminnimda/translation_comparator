#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.extension import Extension
from pathlib import Path
from typing import Collection, Iterable, Iterator, List, Optional, Set, Tuple

from .cython import settings as cython_settings
from .path_helpers import full_path, relative_to_cwd, self_glob, with_parent
from .typedefs import GEN_PATH_FUNC


def includes_excludes_from_patterns(
    *patterns: str
) -> Tuple[List[Path], List[Path]]:

    includes, excludes = [], []
    for pattern in patterns:
        if pattern[:2] == "\\!":
            excludes.append(full_path(
                Path(pattern[2:])))
        else:
            includes.append(full_path(
                Path(pattern)))

    return includes, excludes


def no_matches(path: Path, patterns: Collection[Path]) -> bool:
    for pattern in patterns:
        if path.match(str(pattern)):
            return False
    return True

