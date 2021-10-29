from scripts import check_path, list_files, folder_creator,save_json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import os
from pathlib import Path, PurePath
import spacy
from spacy import displacy
from collections import Counter
from collections import Counter

def entity_extraction(text, path, doc_name):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    doc_entities = [{"token": x.text, "label": x.label_} for x in doc.ents]
    # doc_ent_dict = [{"token":token.text, "BILUO-tag":token.ent_iob_, "entity-tag":token.ent_type_} for token in doc]

    dep_svg = displacy.render(doc, style='dep')
    image_address = path + '/images/' + doc_name.replace('.txt', '_dep.svg')
    Path(image_address).open("w", encoding='utf-8').write(dep_svg)

    return doc_entities , image_address

def apply(from_path, to_path, name):
    from_path = from_path
    to_path = check_path.apply(to_path)
#
    target_folder_path = from_path.replace('result',to_path+'/result')
    folder_creator.apply(target_folder_path)
    #dir for images:
    folder_creator.apply(target_folder_path + '/images')
    output_path = {'output_path': target_folder_path}
#
    result_list = []
    result_list.append(output_path)
#
#     # get files of from_path
    file_list = list_files.apply(from_path)
#
    output_file_path = target_folder_path + '/00_output_result.txt'
# ---------------------------------------------------------

    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(Path(file), 'r', encoding='utf8')
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result_file = str(file).replace('result',to_path+'/result')
        f_output = open(Path(result_file), 'w', encoding='utf8')
        text = f.read()

        doc_entities, image_address = entity_extraction(text, target_folder_path, doc_name)

        for ent in doc_entities:
            f_output.write(f'{ent["token"]}:{ent["label"]}\n')


        SELECT_FIRST_ENTS = 4
        result = {'doc_name':doc_name,'entities':doc_entities[:SELECT_FIRST_ENTS],'entity-count': len(doc_entities),
                   'image_address':image_address}
        f.flush()
        result_list.append(result)

    save_json.apply(result_list,output_file_path)
    return result_list


