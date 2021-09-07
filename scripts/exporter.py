import os
from scripts import list_files, folder_creator, check_path
from pathlib import Path


def apply(from_path, format, name, to_path):
    #from_path = check_path.apply(from_path)
    #file_path = f'media/result/{from_path}/{name}/00_output_result.txt'
    return str(Path(from_path + f'/00_output_result.txt'))
