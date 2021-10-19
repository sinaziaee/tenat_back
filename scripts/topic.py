import os,json
from pathlib import Path
from scripts import list_files, folder_creator, check_path,save_json
import hazm
import string

# function for get text of input file (result is list of terms)
def get_text(file_name):
    f = open(Path(file_name), 'r', encoding='utf8')
    text = f.read()
    doc_name = str(file_name).split('/')[-1].split('\\')[-1]
    f.flush()
    text_list = text.split('\n')
    return text_list

def apply(from_path, to_path, name, method, limit):

    # get files in from_path and set output_path
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)

    # get files of from_path
    file_list = list_files.get_files_list(from_path,name)

    # make output folder path
    folder_path = list_files.get_folder_path(to_path,name)
    output_path = {'output_path': folder_path}

    result_list = []
    result_list.append(output_path)
    output_file_path = folder_path + '/00_output_result.txt'
    #----------------------------------------------------------
    for file in file_list:
        
        result_dict = {'topic':{}}
        result_list.append(result_dict)

    #-------------------------------------------------------------
    save_json.apply(result_list=result_list,output_path=output_file_path)

    return result_list



