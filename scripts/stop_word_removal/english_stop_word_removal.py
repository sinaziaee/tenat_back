from scripts import check_path, list_files, folder_creator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_words = [w for w in word_tokens if not w.lower() in stop_words]
    removed_count = len(word_tokens) - len(filtered_words)
    removed_words = set(set(word_tokens) - set(filtered_words))
    return {'removed_count': removed_count, 'removed_words': " ,".join(removed_words)}

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
        result = remove_stop_words(text)
        result['base-file'] = file
        result['result-file'] = result_file
        f_output.write(f'{str(result)}\n')
        f.flush()
        f_output.flush()
        result_list.append(result)
    return result_list
