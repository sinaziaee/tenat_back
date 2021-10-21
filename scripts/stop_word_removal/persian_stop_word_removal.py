from hazm import word_tokenize
from hazm import stopwords_list
from scripts import check_path, list_files, folder_creator,save_json
import os
from pathlib import Path, PurePath


def remove_stop_words(text, doc_name):
    stop_words = stopwords_list()
    word_tokens = word_tokenize(text)
    filtered_words = [w for w in word_tokens if not w in stop_words]
    removed_count = len(word_tokens) - len(filtered_words)
    removed_words = list(set(word_tokens) - set(filtered_words))
    text_without_stop = " ".join(filtered_words)
    return ({'doc_name':doc_name, 'removed_count': removed_count, 'top_10_removed_words': " ,".join(removed_words[:10])}, text_without_stop)

def apply(from_path, to_path, name):
    from_path = from_path
    to_path = check_path.apply(to_path)
    target_folder_path = from_path.replace('result',to_path+'/result')
    folder_creator.apply(target_folder_path)

    # get files of from_path
    file_list = list_files.apply(from_path)
    output_path = {'output_path': target_folder_path}
    result_list = []
    result_list.append(output_path)

    output_file_path = target_folder_path + '/00_output_result.txt'
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(Path(file), 'r', encoding='utf8')
        result_file = str(file).replace('result',to_path+'/result')
        f_output = open(Path(result_file), 'w', encoding='utf8')
        text = f.read()
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result, text = remove_stop_words(text, doc_name)
        f_output.write(f'{text}\n')
        f.flush()
        result_list.append(result)
    save_json.apply(result_list,output_file_path)
    return result_list


