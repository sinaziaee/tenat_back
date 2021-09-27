from scripts import check_path, list_files, folder_creator
import os
from pathlib import Path, PurePath
from collections import defaultdict
from gensim import corpora, models
from nltk.tokenize import word_tokenize


def tf_idf(texts, docs):
    result = []
    text_without_stop = []
    texts = [' '.join(word_tokenize(text)) for text in texts]
    for text in texts:
        words = []
        for word in text.lower().split():
            words.append(word)
        text_without_stop.append(words)
    dictionary = corpora.Dictionary(text_without_stop)
    id_word = {v: k for k, v in dictionary.token2id.items()} 
    corpus = [dictionary.doc2bow(text) for text in text_without_stop]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    counter = -1
    for doc in corpus_tfidf:
        counter += 1
        for term in doc:
            word = id_word[term[0]]
            weight = term[1]
            dic = {'term': word, 'doc': docs[counter], 'weight': weight}
            result.append(dic)
    return result


def apply(from_path, to_path, name):
    to_path = check_path.apply(to_path)
    folder_path = from_path
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = '/'.join(from_path.split('/')[:-1]) + f'/{to_path}/' + name
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    output_file = open(Path(result_all), 'w', encoding='utf-8')
    output_file.write(f'[\n')
    result = []
    output_path = {'output_path':folder_path }
    result.append(output_path)
    text_list = []
    doc_list = []
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(Path(file), 'r', encoding='utf8')
        text = f.read()
        doc_name = str(PurePath(file).name)
        text_list.append(text)
        doc_list.append(doc_name)
    result.append(tf_idf(text_list, doc_list)[:])
    output_file.write(str(result))
    output_file.write(f']\n')
    output_file.flush()
    return result

