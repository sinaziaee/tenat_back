from scripts import check_path, list_files, folder_creator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def doc_statistics(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    total_words = len(word_tokens)
    distinct_words = len(set([w.lower() for w in word_tokens]))
    stop_word = 0
    main_words = 0
    for w in word_tokens:
        if w.lower() in stop_words:
            stop_word += 1
        else:
            main_words += 1
    return {'total': total_words, 'main': main_words, 'stop': stop_word, 'distinct':distinct_words}

def apply(from_path, to_path, name):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    result_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(result_file, 'w', encoding='utf8')
        text = f.read()
        result = doc_statistics(text)
        result['base-file'] = file
        result['result-file'] = result_file
        f_output.write(f'{str(result)}\n')
        f.flush()
        f_output.flush()
        result_list.append(result)
    return result_list
