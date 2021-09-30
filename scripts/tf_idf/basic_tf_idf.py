from scripts.tf_idf.sklearn_tf_idf import get_file_name
from scripts import check_path, list_files, folder_creator
from nltk.tokenize import word_tokenize
import nltk
from collections import Counter
import math

nltk.download('punkt')


def words_docs_frequency(document_word):
    words_in_docs = {}
    for doc, words in document_word.items():
        for word in words:
            if word not in words_in_docs:
                words_in_docs[word] = [doc]
            elif doc not in words_in_docs[word]:
                words_in_docs[word].append(doc)
    return words_in_docs


def words_per_document(docs):
    word_dict = {}
    for doc, text in docs.items():
        words = [w.lower() for w in word_tokenize(text)]
        word_dict[doc] = dict(Counter(words))
    return word_dict


def TF_IDF(word_dict, words_docs, doc_count, doc, file_name):
    tf_idf_list = []
    all_words = len(word_tokenize(doc))
    for word, count in word_dict.items():
        frequency = count
        tf = frequency/all_words
        idf = math.log10(doc_count/len(words_docs[word]))
        tf_idf = round(tf * idf,4)
        tf_idf_list.append({'term': word, 'doc': file_name, 'weight': tf_idf})
    return tf_idf_list


def apply(from_path, to_path, name):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    output_file_list = []
    doc_text_dict = {}
    doc_count = len(file_list)
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        doc_text_dict[file] = f.read()
    word_dict = words_per_document(doc_text_dict)
    docs_per_word = words_docs_frequency(word_dict)
    result = []
    for file in file_list:
        new_file = str(file).replace(f'{from_path}', f'{to_path}')
        if '00_output_result' in file:
            continue
        output_file_list.append(new_file)
        f_output = open(new_file, 'w', encoding='utf8')
        file_name = str(file).split("\\")[-1]
        tf_idf = TF_IDF(word_dict[file], docs_per_word, doc_count, doc_text_dict[file], file_name)
        f_output.write(str(tf_idf))
        f_output.flush()
        result.extend(tf_idf)
    return result[:20]
