import os
from scripts import list_files, folder_creator, check_path
import hazm


def apply(name, splitter, language, from_path, to_path):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}/'
    print('-' * 100)
    print(folder_path)
    files_list = list_files.apply(folder_path)
    folder_path = folder_path.replace(f'{from_path}', f'{to_path}')
    print('-' * 100)
    for file in files_list:
        f = open(file, 'r', encoding="utf8")
        text = f.read()
        f.flush()
        writer_hazm(folder_path, str(file), text, splitter)
    files_list = list_files.apply(folder_path)
    return files_list


def writer_hazm(folder_path, file, text, splitter):
    print(splitter)
    print(folder_path)
    print(file)
    file = str(file)
    file = file.split('/')[-1]
    folder_creator.apply(folder_path)
    filename = str(file).replace('.docx', '.txt')
    f = open(os.path.join(folder_path, filename), 'w')
    temp = hazm.word_tokenize(text)
    for each in temp:
        f.write(f'{each}{splitter}')
    f.flush()
