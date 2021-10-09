#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import (Callable, Iterable, Iterator, List, Sequence, Tuple,
                    TypeVar, Union)

SHOW_FUNC_DATA = Sequence[Path]
SHOW_FUNC = Callable[[bool, SHOW_FUNC_DATA], None]

DIFF_FUNC = Callable[
    [Sequence[str], Sequence[str]],
    Iterable[str]]

GEN_PATH_FUNC = Callable[[Path], Tuple[Path, Path]]
PATH_FUNC = Callable[[Path], Path]

