import os
from scripts import list_files, folder_creator, check_path
import nltk
import hazm
import PersianStemmer


def apply(name, from_path, to_path):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}/'
    file_list = list_files.apply(folder_path)
    normalizer = hazm.Normalizer()
    output_list = []
    output_path = folder_path.replace(from_path, to_path)
    folder_creator.apply(output_path)
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        doc = str(file).split('/')[-1]
        output_file = f'{output_path}{doc}'
        output_list.append(output_file)
        output_f = open(output_file, 'w')
        text = normalizer.normalize(f.read())
        output_f.write(text)
        f.flush()
        output_f.flush()
    return output_list
