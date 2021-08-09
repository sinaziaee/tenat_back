import os
from scripts import list_files


def apply(file_name, is_tokenized):
    folder_name = str(os.path.basename(file_name))
    if is_tokenized:
        folder_path = f'media/result/tokenized/{folder_name}/'
        file_list = list_files.apply(folder_path)
    else:
        folder_path = f'media/result/raw_text/{folder_name}/'
        file_list = list_files.apply(folder_path)
