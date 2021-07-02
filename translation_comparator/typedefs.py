#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import (Callable, Iterable, Iterator, List, Sequence, Tuple,
                    TypeVar, Union)

DIFF = List[List[str]]
DIFF_FUNC = Callable[
    [Sequence[str], Sequence[str]],
    Iterable[str]]
DIFF_ITER = Iterable[Iterable[str]]

