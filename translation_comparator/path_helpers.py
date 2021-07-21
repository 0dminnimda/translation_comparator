#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from glob import iglob
from pathlib import Path
from typing import Iterator, Tuple

from .cython.path_builders import unique_stem_via_suffix


def self_glob(path: Path) -> Iterator[Path]:
    for string in iglob(str(path)):
        yield Path(string)


def full_path(path: Path) -> Path:
    return path.expanduser().absolute()


def relative_to_cwd(path: Path) -> Path:
    return path.relative_to(Path.cwd())


def with_parent(path: Path, directory: Path) -> Path:
    return directory.joinpath(path.name)


def change_same_paths_if_needed(path1: Path, path2: Path) -> Tuple[Path, Path]:
    if path1.stem == path2.stem:
        return (unique_stem_via_suffix(path1),
                unique_stem_via_suffix(path2))

    if path1.name == path2.name:
        return (path1.with_name(path1.name + " (0)"),
                path2.with_name(path2.name + " (1)"))

    return (path1, path2)

