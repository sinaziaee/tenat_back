from scripts import check_path, list_files, folder_creator,save_json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import os
from pathlib import Path, PurePath



def entity_extract():
    pass


def apply(from_path, to_path, name):
    from_path = from_path
    to_path = check_path.apply(to_path)

    target_folder_path = from_path.replace('result',to_path+'/result')
    folder_creator.apply(target_folder_path)
    output_path = {'output_path': target_folder_path}

    result_list = []
    result_list.append(output_path)

    # get files of from_path
    file_list = list_files.apply(from_path)

    output_file_path = target_folder_path + '/00_output_result.txt'
# ---------------------------------------------------------
    entity_list = []

    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(Path(file), 'r', encoding='utf8')

        result_file = str(file).replace('result',to_path+'/result')
        f_output = open(Path(result_file), 'w', encoding='utf8')
        text = f.read()

        entity = {'term':'google','tag':'ORG'}
        entity_list.append(entity)

        image_address = '' # for each document make an image


        result =  {'doc_name':'computer1.txt','entities':entity_list,'image_address':image_address}
        f_output.write(f'{text}\n')
        f.flush()
        result_list.append(result)

    save_json.apply(result_list,output_file_path)
    return result_list


