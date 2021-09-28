from hazm import word_tokenize
from hazm import stopwords_list
from scripts import check_path, list_files, folder_creator, save_json
from pathlib import Path

def doc_statistics(text, doc_name):
    stop_words = stopwords_list()
    word_tokens = word_tokenize(text)
    total_words = len(word_tokens)
    distinct_words = len(set(word_tokens))
    stop_word = 0
    main_words = 0
    for w in word_tokens:
        if w.lower() in stop_words:
            stop_word += 1
        else:
            main_words += 1
    return {'doc_name': doc_name, 'total': total_words, 'main': main_words, 'stop': stop_word, 'distinct':distinct_words}

def apply(from_path, to_path, name):
    to_path = check_path.apply(to_path)
    folder_path = from_path
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = '/'.join(from_path.split('/')[:-1]) + f'/{to_path}/' + name
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'

    result_list = []
    output_path = {'output_path':folder_path }
    result_list.append(output_path)
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(Path(file), 'r', encoding='utf8')
        text = f.read()
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result = doc_statistics(text, doc_name)
        f.flush()
        result_list.append(result)
    save_json.apply(result_list,result_all)
    return result_list