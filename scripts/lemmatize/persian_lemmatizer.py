import hazm
from scripts import check_path, list_files, folder_creator, slicer,save_json
from scripts import base_script
from hazm import word_tokenize
from pathlib import Path,PurePath

def lemmatize(text):
    lemmatizer = hazm.Lemmatizer()
    words = word_tokenize(text)
    all_lemm = []
    w_lemm = []
    for word in words:
        lem = lemmatizer.lemmatize(word)
        all_lemm.append(lem)
        if word!=lem:
            w_lemm.append(f'{word} => {lem}')
    lemm_text = ' '.join(all_lemm)
    return {'text':lemm_text, 'lemmatized_words':w_lemm, 'lemmatized_count':len(w_lemm)}





def apply(from_path, to_path, name, token_count):
    to_path = check_path.apply(to_path)
    folder_path = from_path
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = '/'.join(from_path.split('/')[:-1]) + f'/{to_path}/' + name
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    result_list = []
    output_path = {'output_path':folder_path }
    result_list.append(output_path)
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(Path(file), 'r', encoding='utf8')
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result_file = Path(folder_path, PurePath(file).name)
        f_output = open(Path(result_file), 'w', encoding='utf-8')
        text = f.read()
        result = lemmatize(text)
        top_lemmed = " ,".join(result['lemmatized_words'][:token_count])
        lemmed_text = result['text']
        result_dict = {'doc_name':doc_name, 'top_lemmatized':top_lemmed, 'lemmatized_count':result['lemmatized_count']}
        f_output.write(f'{lemmed_text}\n')
        f_output.flush()
        result_list.append(result_dict)
    save_json.apply(result_list,result_all)
    return result_list
