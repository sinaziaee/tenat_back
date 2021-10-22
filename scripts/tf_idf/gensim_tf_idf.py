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
            weight = round(term[1],4)
            dic = {'term': word, 'doc': docs[counter], 'weight': weight}
            result.append(dic)
    return result


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
    output_file = open(Path(output_file_path), 'w', encoding='utf-8')
    # output_file.write(f'[\n')
    result = []
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
    result=tf_idf(text_list, doc_list)
    result.insert(0,output_path)
    output_file.write(str(result))
    # output_file.write(f']\n')
    output_file.flush()
    # print(result)
    return result[:20]

