import os


def apply(folder_path):
    mapList = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            mapList.append(fp)

    return mapList
