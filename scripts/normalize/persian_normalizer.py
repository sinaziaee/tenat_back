import os


def apply(file_name, is_tokenized):
    folder_name = str(os.path.basename(file_name))
    if is_tokenized == True:
        folder_path = f'media/result/tokenized/{folder_name}/'
    else:
        folder_path = f'media/result/tokenized/{folder_name}/'
