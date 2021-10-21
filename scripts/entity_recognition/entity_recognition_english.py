from scripts import check_path, list_files, folder_creator, slicer
from pathlib import Path
# import spacy
# from collections import Counter
import en_core_web_sm


def entity_recognition(text):
    nlp = en_core_web_sm.load()
    doc = nlp(text)
    response = {}
    result = {}
    i = 0
    for entity in doc.ents:
        if i < 10:
            response[entity.text] = entity.label_
            i += 1
        result[entity.text] = entity.label_
    return result, response


def apply(from_path, to_path, name, style):
    from_path = check_path.apply(from_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    output_file_list = []
    response = {}
    for file in file_list:
        f = open(Path(file), 'r', encoding='utf8')
        file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(Path(file), 'w', encoding='utf8')
        output_file_list.append(file)
        text = f.read()
        result, top10 = entity_recognition(text)
        f_output.write(str(result))
        response[str(file).split('/')[-1].split('\\')[-1]] = str(top10)
        f.flush()
        f_output.flush()
    return response
