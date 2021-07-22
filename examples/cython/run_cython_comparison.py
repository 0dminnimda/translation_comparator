from pathlib import Path

from translation_comparator import show_via_vscode
from translation_comparator.cython import settings
from translation_comparator.cython.with_cython import cythonize_and_compare

# we use "\n  " because otherwise the newline will be thrown in diff
settings.str_between_lines = "\n  " + "="*100 + "\n  "*2
settings.out_ext = ".c"  # only for save_as_diff = False
settings.build_dir = Path("build/")  # the output files will be saved here
settings.diff_dir = Path("diff/")  # the html will be located here
settings.show_func = show_via_vscode
# False - save as two separate files and call function
# with their names to show the diff, here - show_via_vscode
# True - output one .diff file with diff using difflib
settings.save_as_diff = False


# remove most of the useless difference between files
# so you can focus on the real difference;
# takes in patterns, that glob will accept
# "\\!" - excude ones that matches this, pattern order doesn't matter
# keyword arguments will be used for cythonize
cythonize_and_compare("*", "\\!run_cython_comparison.py",
                      language_level=3)


# you can see result in the diff folder

