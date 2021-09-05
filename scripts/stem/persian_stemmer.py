from scripts import list_files, check_path, folder_creator, slicer
import hazm
from hazm import word_tokenize
from scripts import base_script


def stemming(text):
    stemmer = hazm.Stemmer()
    words = word_tokenize(text)
    all_stemmed = []
    w_stemmes = []
    for word in words:
        stm = stemmer.stem(word)
        all_stemmed.append(stm)
        if word!=stm:
            w_stemmes.append(f'{word} : {stm}')
    stemmed_text = ' '.join(all_stemmed)
    return {'text':stemmed_text, 'stemmed_words':w_stemmes, 'stemmed_count':len(w_stemmes)}

def apply(from_path, to_path, name, token_count):
    to_path = check_path.apply(to_path)
    folder_path = from_path
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = '/'.join(from_path.split('/')[:-1]) + f'/{to_path}/' + name
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    output_file = open(result_all, 'w', encoding='utf-8')
    result_list = []
    output_path = {'output_path':folder_path }
    result_list.append(output_path)
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(file, 'r', encoding='utf8')
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result_file = folder_path + '/' + file.split('/')[-1]
        f_output = open(result_file, 'w', encoding='utf8')
        text = f.read()
        result = stemming(text)
        stemmed_text = result['text']
        result_dict = {'doc_name':doc_name, 'top_stemmed':', '.join(result['stemmed_words'][:token_count]), 'stemmed_count':result['stemmed_count']}
        output_file.write(f'{str(result_dict)}\n')
        f_output.write(f'{stemmed_text}\n')
        f_output.flush()
        result_list.append(result_dict)
    output_file.flush()
    return result_list
