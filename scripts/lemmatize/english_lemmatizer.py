import nltk
from nltk.tokenize import word_tokenize
from scripts import list_files, check_path, folder_creator, slicer
from scripts import base_script

def lemmatize(text):
    lemmatizer = nltk.WordNetLemmatizer()
    words = word_tokenize(text)
    all_lemm = []
    w_lemm = []
    for word in words:
        lem = lemmatizer.lemmatize(word)
        all_lemm.append(lem)
        if word!=lem:
            w_lemm.append(f'{word} : {lem}')
    lemm_text = ' '.join(all_lemm)
    return {'text':lemm_text, 'lemmatized_words':w_lemm, 'lemmatized_count':len(w_lemm)}

def apply(from_path, to_path, name, token_count):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    output_file = open(result_all, 'w', encoding='utf-8')
    result_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(result_file, 'w', encoding='utf8')
        text = f.read()
        result = lemmatize(text)
        top_lemmed = " ,".join(result['lemmatized_words'][:token_count])
        lemmed_text = result['text']
        result_dict = {'doc_name':doc_name, 'top_lemmatized':top_lemmed, 'lemmatized_count':result['lemmatized_count']}
        f_output.write(f'{lemmed_text}\n')
        output_file.write(f'{str(result_dict)}\n')
        f.flush()
        f_output.flush()
        result_list.append(result_dict)
    output_file.flush()
    return result_list
