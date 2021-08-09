import os
from scripts import list_files, folder_creator
import hazm


def apply(file_name, is_tokenized):
    folder_name = str(os.path.basename(file_name))
    if is_tokenized:
        folder_path = f'media/result/tokenized/{folder_name}/'
    else:
        folder_path = f'media/result/raw_text/{folder_name}/'
    file_list = list_files.apply(folder_path)
    normalizer = hazm.Normalizer()
    output_list = []
    output_path = str(f'media/result/normalized/{folder_name}/')
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
