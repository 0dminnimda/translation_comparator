#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import settings
from .annotated_html_parser import (get_code_from_two_files,
                                    get_code_from_two_files_by_path)
from .code_comparator import (compare_and_save_two_files,
                              compare_and_save_two_files_by_path)
