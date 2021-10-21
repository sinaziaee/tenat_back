import os
from pathlib import Path
from scripts import check_path,folder_creator


def apply(folder_path: object) -> object:
    mapList = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = Path(path, f)
            mapList.append(str(fp))

    return mapList




def get_folder_path(path,name):
    path = check_path.apply(path)
    folder_path = f'media/result/{path}/{name}'
    folder_creator.apply(folder_path)
    return folder_path

def get_files_list(path,name):
    # get files of from_path
    folder_path = get_folder_path(path,name)
    file_list = apply(folder_path)
    return file_list