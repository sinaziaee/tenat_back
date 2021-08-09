import os


def apply(file_name, splitter, language):
    folder_name = str(os.path.basename(file_name))
    folder_path = f'media/result/raw_text/{folder_name}/'
    files_list = []

    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            files_list.append(fp)
    folder_path = folder_path.replace('result/raw_text', 'result/tokenized')
    for file in files_list:
        f = open(file, 'r', encoding="utf8")
        text = f.read()
        f.flush()
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
