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


def matching_paths(
    includes: Iterable[Path], excludes: Collection[Path],
) -> Iterator[Path]:

    for path in includes:
        for match in self_glob(path):
            if no_matches(match, excludes):
                yield match


def paths_for_cython(*patterns: str) -> Iterator[Path]:

    # if returned is None:
    returned: Set[str] = set()

    includes, excludes = includes_excludes_from_patterns(*patterns)

    for path in matching_paths(
        (i.with_suffix(".py*") for i in includes),
        [i.with_suffix(".py*") for i in excludes],
    ):

        if path.suffix in (".py", ".pyx") and path.name not in returned:
            yield path
            returned.add(path.name)
