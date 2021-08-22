import os


def apply(folder_path):
    mapList = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            # size += os.path.getsize(fp)
            file = open(f'{path}{f}', 'r', encoding='utf8')
            text = file.readlines(1)
            name = fp.split('/')[-1]
            new_map = {'name': name, 'size': os.path.getsize(fp), 'text': text}
            mapList.append(new_map)
            file.flush()

    return mapList
