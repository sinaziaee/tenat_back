from scripts import list_files, check_path, folder_creator
from nltk.tokenize import word_tokenize
import math


def words_frequency(document_word):
    words_in_docs = {}
    for doc in document_word.keys():
        for word in document_word[doc]:
            if word not in words_in_docs:
                words_in_docs[word] = [doc]
            elif doc not in words_in_docs[word]:
                words_in_docs[word].append(doc)
    return words_in_docs


def compute_tf(doc_dict, docs_by_words):
    tf = {}
    word_bag = docs_by_words.keys()
    for doc in doc_dict.keys():
        tf[doc] = {}
        for word in word_bag:
            if len(doc_dict[doc]) == 0:
                tf[doc][word] = 0
            else:
                tf[doc][word] = sum(word == w for w in doc_dict[doc])/len(doc_dict[doc])
    return tf


def compute_idf(doc_dict, docs_by_words):
    idf = {}
    for word, docs in docs_by_words.items():
        idf[word] = math.log10(len(doc_dict)/len(docs_by_words[word]))
    return idf


def compute_tf_idf(doc_dict, docs_by_words):
    tf = compute_tf(doc_dict, docs_by_words)
    idf = compute_idf(doc_dict, docs_by_words)

    word_bag = docs_by_words.keys()
    tf_idf = {}
    for doc, words in doc_dict.items():
        tf_idf[doc] = {}
        for word in word_bag:
            tf_idf[doc][word] = tf[doc][word] * idf[word]
    return tf_idf


def apply(from_path, to_path, name, method):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)

    doc_dict = {}
    for file in file_list:
        if 'output_result' in file:
            continue
        f = open(file, 'r', encoding='utf8')
        doc_dict[file] = f.read().split('\n')

    docs_by_word = words_frequency(doc_dict)
    if method == 'tf':
        x = compute_tf(doc_dict, docs_by_word)
    elif method == 'idf':
        x = compute_idf(doc_dict, docs_by_word)
    elif method == 'tf-idf':
        x = compute_tf_idf(doc_dict, docs_by_word)
    else:
        pass
    return x
