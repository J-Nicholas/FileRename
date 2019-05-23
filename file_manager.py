""" 
This module is responsible for renaming files
"""
from pathlib import Path
import os
import platform


def rename_files(files: list, new_file_name: str) -> bool:
    """Renames a list of files using a stem that is provided by the user.

    Arguments:
        files {list} -- list of file strings containing absolute path of each file
        new_file_name {str} -- new name of file to be used as a stem

    Returns:
        bool -- returns True if successfully renamed files, False if it failed.
    """
    if len(files) == 0:
        print("list of files was empty. Could not rename files.")
        return False

    path = None
    for index, item in enumerate(files, start=1):
        path = Path(rf"{item}")

        if path.exists():
            new_path = Path(str(path.parent) + "/" + new_file_name +
                            str(index) + path.suffix)
            path.replace(new_path)
            print(platform.system())
        else:
            print("Path did not exist. Check file path for errors.")
            return False
    return True
