"""
Helpers for semantic versioning
"""

from sys import argv


def get_version() -> str:
    """
    Tries to grab the version from the CLI argument.
    """
    if len(argv) > 1:
        return argv[1]

    return '@dev'
