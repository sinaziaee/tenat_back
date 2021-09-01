from hazm import word_tokenize
from hazm import stopwords_list
from scripts import check_path, list_files, folder_creator
import os


def remove_stop_words(text, doc_name):
    stop_words = stopwords_list()
    word_tokens = word_tokenize(text)
    filtered_words = [w for w in word_tokens if not w in stop_words]
    removed_count = len(word_tokens) - len(filtered_words)
    removed_words = list(set(word_tokens) - set(filtered_words))
    text_without_stop = " ".join(filtered_words)
    return ({'doc_name':doc_name, 'removed_count': removed_count, 'top_10_removed_words': " ,".join(removed_words[:10])}, text_without_stop)

def apply(from_path, to_path, name):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    output_file = open(result_all, 'w', encoding='utf-8')
    result_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(result_file, 'w', encoding='utf8')
        text = f.read()
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result, text = remove_stop_words(text, doc_name)
        f_output.write(f'{text}\n')
        output_file.write(f'{str(result)}\n')
        f.flush()
        result_list.append(result)
    output_file.flush()
    return result_list


