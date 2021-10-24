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
from nltk.corpus import stopwords
import re
import numpy as np
import pandas as pd
from pprint import pprint
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import spacy
import pyLDAvis
import pyLDAvis.gensim_models
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import en_core_web_sm
# function for get text of input file (result is list of terms)
def get_text(file_name):
    f = open(Path(file_name), 'r', encoding='utf8')
    text = f.read()
    doc_name = str(file_name).split('/')[-1].split('\\')[-1]
    f.flush()
    text_list = text.split('\n')
    return text_list



def remove_stopwords(texts,stop_words):
       return [[word for word in simple_preprocess(str(doc)) 
   if word not in stop_words] for doc in texts]
def make_bigrams(texts, bigram_mod):
   return [bigram_mod[doc] for doc in texts]
def make_trigrams(texts,trigram_mod,bigram_mod):
   [trigram_mod[bigram_mod[doc]] for doc in texts]
def lemmatization(texts,nlp, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
   texts_out = []
   for sent in texts:
      doc = nlp(" ".join(sent))
      texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
   return texts_out



def LDA(corpus, id2word,alpha, num_topics,chunk_size,passes):
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=num_topics,
                                                update_every=1,
                                                chunksize=chunk_size,
                                                passes=passes,
                                                alpha=alpha,per_word_topics=True)

    return lda_model


def apply(from_path, to_path, name, method,alpha, num_topics,chunk_size,passes):

    # get files in from_path and set output_path
    # from_path = check_path.apply(from_path)
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
    #----------------------------------------------------------
    data = []
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(file, 'r', encoding='utf8')
        tokens = f.readlines()
        data.append(tokens)
    # Create Dictionary
    stop_words = stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use'])


    bigram = gensim.models.Phrases(data, min_count=5, threshold=100)
    trigram = gensim.models.Phrases(bigram[data], threshold=100)
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)



    data_words_nostops = remove_stopwords(data,stop_words)
    data_words_bigrams = make_bigrams(data_words_nostops,bigram_mod)
    nlp = en_core_web_sm.load()
    # nlp = spacy.load('en_core_web_md', disable=['parser', 'ner'])
    data_lemmatized = lemmatization(data_words_bigrams,nlp, allowed_postags=[
    'NOUN', 'ADJ', 'VERB', 'ADV'
    ])


    # id2word = corpora.Dictionary(data)
    # # Term Document Frequency
    # corpus = [id2word.doc2bow(word) for word in data]


    id2word = corpora.Dictionary(data_lemmatized)
    texts = data_lemmatized
    corpus = [id2word.doc2bow(text) for text in texts]

    model = None
    topics = []


    if method == 'LDA':
        model = LDA(corpus, id2word,alpha,num_topics,chunk_size,passes)
        for i in range(0, model.num_topics):
            topics.append(model.print_topic(i))
        p = pyLDAvis.gensim_models.prepare(model, corpus, id2word)
        pyLDAvis.save_html(p, target_folder_path+'/lda.html')
        html_string =str(pyLDAvis.prepared_data_to_html(p))
    else:
        pass

    for i in range(len(topics)):
        result_file = target_folder_path + '/Topic' + str(i)
        f_output = open(Path(result_file), 'w', encoding='utf8')
        f_output.write(topics[i])
        result_dict = {'number': i, 'topic': topics[i]}
        result_list.append(result_dict)

    model_file = target_folder_path + '/model'
    with open(model_file, 'wb') as fp:
        pickle.dump(model, fp)

    corpus_file = target_folder_path + '/corpus'
    with open(corpus_file, 'wb') as fp:
        pickle.dump(corpus, fp)

    id2word_file = target_folder_path + '/id2word'
    with open(id2word_file, 'wb') as fp:
        pickle.dump(id2word, fp)

    #-------------------------------------------------------------
    save_json.apply(result_list=result_list,output_path=output_file_path)
    return result_list



