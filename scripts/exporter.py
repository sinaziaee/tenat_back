import os
from scripts import list_files, folder_creator, check_path
from pathlib import Path, PurePath
from zipfile import ZipFile
import time

def apply(from_path, format, name, to_path):
    files = list_files.apply(from_path)
    name_zip = from_path.split('/')[-1][:-4]
    path = f'media/result/export/{name_zip}'
    folder_creator.apply(path)
    rand_int = round(time.time() * 1000)
    zipfile = ZipFile(f'{path}/output_{str(rand_int)}.zip', 'w')
    for file in files:
        zipfile.write(file, str(PurePath(file).name))
    return str(f'{path}/output_{str(rand_int)}.zip')
