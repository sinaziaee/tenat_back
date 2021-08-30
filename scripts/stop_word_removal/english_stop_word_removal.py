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
    removed_words = list(set(word_tokens) - set(filtered_words))
    text_without_stop = " ".join(filtered_words)
    return ({'removed_count': removed_count, 'top_10_removed_words': " ,".join(removed_words[:10])},text_without_stop)

def apply(from_path, to_path, name):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/text_without_stop_words/{name}'
    folder_creator.apply(folder_path)
    result_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        text_result_file = str(file).replace(f'{from_path}', f'{to_path}/text_without_stop_words')
        f_output = open(result_file, 'w', encoding='utf8')
        f_text_output = open(text_result_file, 'w', encoding='utf8')
        text = f.read()
        result, text = remove_stop_words(text)
        result['doc_name'] =str(file).split('/')[-1].split('\\')[-1]
        f_output.write(f'{str(result)}\n')
        f_text_output.write(f'{text}')
        f.flush()
        f_output.flush()
        result_list.append(result)
    return result_list
