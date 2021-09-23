from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from scripts import check_path, list_files, folder_creator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pathlib import Path
import json


# function for get text of input file (result is list of terms)
def get_text(file_name):
    f = open(Path(file_name), 'r', encoding='utf8')
    text = f.read()
    doc_name = str(file_name).split('/')[-1].split('\\')[-1]
    f.flush()
    return text

def apply(from_path, to_path, name):
    to_path = check_path.apply(to_path)
    folder_path = from_path
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = '/'.join(from_path.split('/')[:-1]) + f'/{to_path}/' + name
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    # output_file = open(Path(result_all), 'w', encoding='utf-8')
    # output_file.write(f'[\n')
    result_list = []
    output_path = {'output_path':folder_path }
    result_list.append(output_path)
    result_dict = {}

    corpus = []
    for i in range(0,len(file_list)):
        text = get_text(file_list[i])
        corpus.append(text)

    tfIdfVectorizer=TfidfVectorizer(use_idf=True)
    tfIdfVectorizer=TfidfVectorizer()
    tfIdf = tfIdfVectorizer.fit_transform(corpus)
    df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)
    # df.to_csv('tf_idf', sep='\t', encoding='utf-8')
    # result_list= list(df.to_json(orient = 'record'))
    # df.to_json('tf_idf.json', orient = 'split', compression = 'infer', index = 'true')
    # df.to_json (r'C:\Users\Ron\Desktop\Export_DataFrame.json')
    print (df.tail(50))
    result_list = []
    return result_list

        

