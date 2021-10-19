import os,json
from pathlib import Path
from scripts import list_files, folder_creator, check_path,save_json
import hazm
import string
ignoreList = ["!", "@", "$", "%", "^", "&","#" "*", "(", ")", "_", "+", "-", "/", "*", "'", "،", "؛", ",", ""
                      "{","}",":",";",'=',"|",
                      "[", "]", "«", "»", "<", ">", ".", "?", "؟", "\n", "\t", '"',"“","”","\u200c","\u200e"
                      '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰', "٫","."
                      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



def tokenize_text(text, doc_name, splitter):
    for item in ignoreList:
        text = text.replace(item, " ")
    word_tokens = [word.lower() for word in text.split(splitter) if word != ""]
    return ({'doc_name':doc_name, 'tokens': word_tokens })


# def get_files_list(path,name):
#     # get files of from_path
#     folder_path = get_folder_path(path,name)
#     file_list = list_files.apply(folder_path)
#     return file_list

# def get_folder_path(path,name):
#     path = check_path.apply(path)
#     folder_path = f'media/result/{path}/{name}'
#     folder_creator.apply(folder_path)
#     return folder_path


def apply(from_path, to_path, name, splitter, tokens_count):

    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    print('==================================')
    print('from_path= '+str(from_path))

    # get files of from_path
    file_list = list_files.get_files_list(from_path,name)

    # make output folder path
    folder_path = list_files.get_folder_path(to_path,name)

    output_path = {'output_path': folder_path}

    result_list = []
    result_list.append(output_path)

    output_file_path = folder_path + '/00_output_result.txt'

    for file in file_list:
        f = open(Path(file), 'r', encoding='utf8')
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        print('result_file= '+str(result_file))
        f_output = open(Path(result_file), 'w', encoding='utf8')
        text = f.read()
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result = tokenize_text(text, doc_name, splitter)
        for tok in result['tokens']:
            f_output.write(f'{tok}\n')
        result['top_tokens'] = ', '.join(result['tokens'][:tokens_count])
        result_dict = {'doc_name':result['doc_name'], 'tokens': result['top_tokens'], 'tokens_count':len(result['tokens'])}
        f.flush()
        result_list.append(result_dict)

    save_json.apply(result_list=result_list,output_path=output_file_path)

    return result_list



