import os
from pathlib import Path
from scripts import list_files_and_sizes, folder_creator
import docx2txt
import zip_unicode


def apply(zip_file):
    folder_name = str(os.path.basename(zip_file))
    folder_path = f'media/data/{folder_name}/'
    try:
        if not Path(f'media/data/').is_dir():
            dirname = os.path.dirname(__file__)
            path = Path(dirname).parent
            path = Path(path, f'media/data')
            path.mkdir(parents=True, exist_ok=True)
        if not os.path.isdir(f'media/data/{folder_name}'):
            dirname = os.path.dirname(__file__)
            path = Path(dirname).parent
            path = Path(path, f'media/data/{folder_name}')
            path.mkdir(parents=True, exist_ok=True)
        zip_ref = zip_unicode.ZipHandler(path=zip_file, extract_path=folder_path)
        zip_ref.extract_all()
    except OSError as error:
        print(error)
    files_list = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = Path(path, f)
            files_list.append(fp)
    folder_path = folder_path.replace('data', 'result/raw_text')
    for file in files_list:
        doc_to_txt(folder_path, file)

    return list_files_and_sizes.apply(folder_path)


def doc_to_txt(folder_path, file):
    text = ''
    if str(file).endswith('.docx'):
        f = docx2txt.process(file)
        lines = f.split('\n')
        for line in lines:
            if line != '':
                text += line + '\n'
    else:
        f = open(Path(file), 'r', encoding='utf8')
        for line in f.readlines():
            if line != '':
                text += line.replace('\n', '') + '\n'
        f.flush()
    folder_creator.apply(str(Path(folder_path)))
    file = str(file).split('/')[-1].replace('.docx', '.txt')
    file = str(PurePath(file).name)
    f = open(Path(folder_path, file), 'w', encoding='utf-8')
    f.write(text)
    f.flush()

