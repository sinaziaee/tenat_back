import os
from scripts import list_files
import docx2txt


def apply(file_name, splitter, language):
    folder_name = str(os.path.basename(file_name))
    folder_path = f'media/data/{folder_name}/'
    files_list = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            name = fp.split('/')[-1]
            files_list.append(fp)
    folder_path = folder_path.replace('data', 'result/tokenized')
    for file in files_list:
        if str(file).endswith('.docx'):
            f = docx2txt.process(file)
            new_file = folder_path
            text = ''
            lines = f.split('\n')
            for line in lines:
                if line != '':
                    text += line + '\n'
        else:
            text = ''
            f = open(file, 'r', encoding="utf8").read()
        writer(folder_path, str(file), text, splitter)
    files_list = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            files_list.append(fp)
    return files_list


def writer(folder_path, file, text, splitter):
    file = str(file)
    file = file.split('/')[-1]
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename = str(file).replace('.docx', '.txt')
    f = open(os.path.join(folder_path, filename), 'w')
    for line in text.split('\n'):
        for each in line.split(' '):
            f.write(f'{each}{splitter}')
    f.flush()
