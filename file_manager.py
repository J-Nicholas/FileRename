""" 
This module is responsible for renaming files
"""
from pathlib import Path


def rename_files(files: list, new_file_name: str) -> bool:

    file_dirs = [item.name for item in files]
    index = 1
    path = None
    for item in file_dirs:
        path = Path(rf"{item}")
        
        if path.exists():
            new_path = str(path.parent) + "\\" + new_file_name + \
                str(index) + path.suffix
            path.replace(new_path)
            index += 1
    return True
