#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from glob import iglob
from pathlib import Path
from typing import Iterator


def self_glob(path: Path) -> Iterator[Path]:
    for string in iglob(str(path)):
        yield Path(string)


def full_path(path: Path) -> Path:
    return path.expanduser().absolute()

