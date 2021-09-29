from sklearn.feature_extraction.text import TfidfVectorizer
from scripts import check_path, folder_creator, list_files
from pathlib import Path
import pandas as pd


def get_text(file):
    f = open(Path(file), 'r', encoding='utf8')
    text = f.read()
    f.flush()
    return text


def get_file_name(file):
    return str(file).split('/')[-1].split('\\')[-1]


def TF_IDF(file):
    result = []
    file_name = get_file_name(file)
    text = [get_text(file)]
    tfIdfVectorizer = TfidfVectorizer(use_idf=True)
    tfIdf = tfIdfVectorizer.fit_transform(text)
    tfIdf = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
    for index, row in tfIdf.iterrows():
        result.append({'term': index, 'doc': file_name, 'weight': row['TF-IDF']})
    return result


def apply(from_path, to_path, name):
    to_path = check_path.apply(to_path)
    from_path = check_path.apply(from_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    output_file_list = []
    result = []
    for file in file_list:
        new_file = str(file).replace(f'{from_path}', f'{to_path}')
        output_file_list.append(new_file)
        f_output = open(new_file, 'w', encoding='utf8')
        tf_idf = TF_IDF(file)
        f_output.write(str(tf_idf))
        f_output.flush()
        result.extend(tf_idf)
    return result
