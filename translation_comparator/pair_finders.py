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


def pairs_and_extentions_for_cython(
    *patterns: str
) -> Tuple[List[Tuple[Path, Path]], List[Path], List[Path]]:

    pairs: List[Tuple[Path, Path]] = []
    py_paths: List[Path] = []
    pyx_paths: List[Path] = []

    path_func = cython_settings.path_func
    build_dir = cython_settings.build_dir

    for path in paths_for_cython(*patterns):
        path1, path2 = path_func(path)

        path1 = relative_to_cwd(path1)
        path2 = relative_to_cwd(path2)

        new_path1 = with_parent(path1, cython_settings.py_dir)
        new_path2 = with_parent(path2, cython_settings.pyx_dir)

        py_paths.append(path1)
        pyx_paths.append(path2)

        pairs.append((
            cython_settings.build_dir.joinpath(new_path1),
            cython_settings.build_dir.joinpath(new_path2)))

    return pairs, py_paths, pyx_paths

