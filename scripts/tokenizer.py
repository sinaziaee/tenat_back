import os
from pathlib import Path
from scripts import list_files, folder_creator, check_path
import hazm
import string
ignoreList = ["!", "@", "$", "%", "^", "&","#" "*", "(", ")", "_", "+", "-", "/", "*", "'", "،", "؛", ",", ""
                      "{","}",":",";",'=',"|",
                      "[", "]", "«", "»", "<", ">", ".", "?", "؟", "\n", "\t", '"',"“","”","\u200c","\u200e"
                      '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰', "٫",
                      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



def tokenize_text(text, doc_name, splitter):
    for item in ignoreList:
        text = text.replace(item, " ")
    word_tokens = [word.lower() for word in text.split(splitter) if word != ""]
    return ({'doc_name':doc_name, 'tokens': word_tokens })

def apply(from_path, to_path, name, splitter, tokens_count):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    output_file = open(Path(result_all), 'w', encoding='utf-8')
    output_file.write(f'[\n')
    output_path = {'output_path': folder_path}
    result_list = []
    result_list.append(output_path)
    for file in file_list:
        print(str(Path(r'{file}')))
        f = open(Path(file), 'r', encoding='utf8')
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(Path(result_file), 'w', encoding='utf8')
        text = f.read()
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result = tokenize_text(text, doc_name, splitter)
        for tok in result['tokens']:
            f_output.write(f'{tok}\n')
        result['top_tokens'] = ', '.join(result['tokens'][:tokens_count])
        result_dict = {'doc_name':result['doc_name'], 'tokens': result['top_tokens'], 'tokens_count':len(result['tokens'])}
        output_file.write(f'{str(result_dict)},\n')
        f.flush()
        result_list.append(result_dict)
    output_file.write(f']\n')
    output_file.flush()
    return result_list
