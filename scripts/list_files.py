import os
from pathlib import Path


def apply(folder_path):
    mapList = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = Path(path, f)
            mapList.append(str(fp))

    return mapList
