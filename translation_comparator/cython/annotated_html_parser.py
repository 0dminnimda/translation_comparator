#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List, Tuple

from bs4 import BeautifulSoup
from bs4.element import Tag


def get_code_from_soup(soup: BeautifulSoup) -> List[str]:
    return [
        tag.text for tag in soup.find_all("pre", class_="code")]


def get_soup_from_html(path: Path) -> BeautifulSoup:
    html = path.with_suffix(".html").read_text()

    return BeautifulSoup(html, "lxml")


def get_code_from_two_files_by_path(
    path1: Path, path2: Path
) -> Tuple[List[str], List[str]]:

    return (
        get_code_from_soup(get_soup_from_html(path1)),
        get_code_from_soup(get_soup_from_html(path2)))

