import hazm
from scripts import check_path, list_files, folder_creator, slicer
from scripts import base_script
from hazm import word_tokenize

def lemmatize(text):
    lemmatizer = hazm.Lemmatizer()
    words = word_tokenize(text)
    lemm_text = lemmatizer.lemmatize(text)
    all_lemm = []
    for word in words:
        lem = lemmatizer.lemmatize(word)
        all_lemm.append(f'{word} : {lem}')
    return {'text':lemm_text, 'lemmatized_words':all_lemm}

def apply(from_path, to_path, name, token_count):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/lemmatized_text_and_words/{name}'
    folder_creator.apply(folder_path)
    result_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(result_file, 'w', encoding='utf8')
        text_result_file = str(file).replace(f'{from_path}', f'{to_path}/lemmatized_text_and_words')
        f_text_output = open(text_result_file, 'w', encoding='utf8')
        text = f.read()
        result = lemmatize(text)
        top_lemmed = " ,".join(result['lemmatized_words'][:token_count])
        lemmed_text = result['text']
        result_dict = {'top_tokens':top_lemmed, 'result_link':result_file, 'text_result_file':text_result_file, 'doc_name':doc_name}
        f_output.write(f'{str(result_dict)}\n')
        f_text_output.write(f'{lemmed_text}\n\n')
        for lem in result['lemmatized_words']:
            f_text_output.write(f'{lem}\n')
        f.flush()
        f_output.flush()
        f_text_output.flush()
        result_list.append(result_dict)
    return result_list
