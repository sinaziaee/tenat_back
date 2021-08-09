import os


def apply(folder_path):
    mapList = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            # size += os.path.getsize(fp)
            name = fp.split('/')[-1]
            new_map = {name, os.path.getsize(fp)}
            mapList.append(new_map)

    return mapList
