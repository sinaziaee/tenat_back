from scripts import check_path, list_files, folder_creator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')


def apply(from_path, to_path, name):
    stop_words = set(stopwords.words('english'))
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    output_file_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(file, 'w', encoding='utf8')
        output_file_list.append(file)
        text = f.read()
        word_tokens = word_tokenize(text)
        filtered_words = [w for w in word_tokens if not w.lower() in stop_words]
        for r in filtered_words:
            f_output.write(r + "\n")
        f.flush()
        f_output.flush()
    return output_file_list
