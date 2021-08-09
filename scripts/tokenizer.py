import os
from scripts import list_files, file_folder_creator
import hazm


def apply(file_name, splitter, language):
    folder_name = str(os.path.basename(file_name))
    folder_path = f'media/result/raw_text/{folder_name}/'
    files_list = list_files.apply(folder_path)

    folder_path = folder_path.replace('result/raw_text', 'result/tokenized')
    for file in files_list:
        f = open(file, 'r', encoding="utf8")
        text = f.read()
        f.flush()
        # writer(folder_path, str(file), text, splitter)
        writer_hazm(folder_path, str(file), text, splitter)
    files_list = list_files.apply(folder_path)
    return files_list


# this is a tokenizer that i wrote myself
def writer(folder_path, file, text, splitter):
    print('-' * 100)
    file = str(file)
    file = file.split('/')[-1]
    file_folder_creator.apply(folder_path)
    filename = str(file).replace('.docx', '.txt')
    f = open(os.path.join(folder_path, filename), 'w')
    for line in text.split('\n'):
        for each in line.split(' '):
            f.write(f'{each}{splitter}')
    f.flush()


# this is a tokenizer that uses hazam library
def writer_hazm(folder_path, file, text, splitter):
    print(folder_path)
    print(file)
    file = str(file)
    file = file.split('/')[-1]
    file_folder_creator.apply(folder_path)
    filename = str(file).replace('.docx', '.txt')
    f = open(os.path.join(folder_path, filename), 'w')
    temp = hazm.word_tokenize(text)
    for each in temp:
        f.write(f'{each}{splitter}')
    f.flush()
