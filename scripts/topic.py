import os,json
from pathlib import Path

from scripts import list_files, folder_creator, check_path,save_json
import hazm
import string

import gensim
import gensim.corpora as corpora
from pprint import pprint
# import pickle5 as pickle
import pickle
import numpy as np

# function for get text of input file (result is list of terms)
def get_text(file_name):
    f = open(Path(file_name), 'r', encoding='utf8')
    text = f.read()
    doc_name = str(file_name).split('/')[-1].split('\\')[-1]
    f.flush()
    text_list = text.split('\n')
    return text_list


def LDA(corpus, id2word, num_topics):
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=num_topics,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=100,
                                                passes=10,
                                                alpha='auto')
    return lda_model


def apply(from_path, to_path, name, method, limit):

    # get files in from_path and set output_path
    from_path = check_path.apply(from_path)
 
    to_path = check_path.apply(to_path)
    folder_path = from_path
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = '/'.join(from_path.split('/')[:-1]) + f'/{to_path}/' + name
    folder_creator.apply(folder_path)

    output_path = {'output_path': folder_path}

    result_list = []
    result_list.append(output_path)
    output_file_path = folder_path + '/00_output_result.txt'
    #----------------------------------------------------------
    data = []
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(file, 'r', encoding='utf8')
        tokens = f.readlines()
        data.append(tokens)
    # Create Dictionary
    id2word = corpora.Dictionary(data)
    # Term Document Frequency
    corpus = [id2word.doc2bow(word) for word in data]

    model = None
    topics = []
    if method == 'LDA':
        model = LDA(corpus, id2word, limit)
        for i in range(0, model.num_topics):
            topics.append(model.print_topic(i))
    else:
        pass

    for i in range(len(topics)):
        result_file = folder_path + '/Topic' + str(i)
        f_output = open(Path(result_file), 'w', encoding='utf8')
        f_output.write(topics[i])
        result_dict = {'number': i, 'topic': topics[i]}
        result_list.append(result_dict)

    model_file = folder_path + '/model'
    with open(model_file, 'wb') as fp:
        pickle.dump(model, fp)

    corpus_file = folder_path + '/corpus'
    with open(corpus_file, 'wb') as fp:
        pickle.dump(corpus, fp)

    id2word_file = folder_path + '/id2word'
    with open(id2word_file, 'wb') as fp:
        pickle.dump(id2word, fp)

    #-------------------------------------------------------------
    save_json.apply(result_list=result_list,output_path=output_file_path)
    return result_list



