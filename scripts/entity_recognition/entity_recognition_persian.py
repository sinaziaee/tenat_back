from scripts import check_path, list_files, folder_creator, slicer
from pathlib import Path


def entity_recognition(text):
    pass


def apply(from_path, to_path, name, style):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    output_file_list = []
    for file in file_list:
        f = open(Path(file), 'r', encoding='utf8')
        file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(Path(file), 'w', encoding='utf8')
        output_file_list.append(file)
        text = f.read()
        result = entity_recognition(text)
        print(result)
        f_output.write(str(result))
        f.flush()
        f_output.flush()
    return result