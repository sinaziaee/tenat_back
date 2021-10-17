from nltk import stem
from nltk.tokenize import word_tokenize
from scripts import list_files, check_path, folder_creator, slicer,save_json,list_files_and_sizes
from scripts import base_script
from pathlib import Path, PurePath
import os
import shutil,time


def apply(from_path1,from_path2,name1,name2, to_path):

    folder_name = str(name1+'_'+name2).replace('.zip','').replace('.rar','').replace('.7z','');        
    rand_int = round(time.time() * 1000)

    to_path = f'media/result/join/{folder_name}/'  # media/data/computer.zip/
    folder_creator.apply(to_path)

    result_list = []

    # file_list1 = list_files.apply(from_path1)
    # file_list2 = list_files.apply(from_path2)


    source_folder = from_path1
    destination_folder = to_path

    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = Path(source_folder +'/'+ file_name)
        destination = Path(destination_folder +'/'+ file_name)


        print('source='+str(source))

        if file_name == '00_output_result.txt':
                continue
        # copy only files
        if os.path.isfile(source):
            
            shutil.copy(source, destination)
            print('copied', file_name)


    source_folder = from_path2
    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = Path(source_folder +'/'+ file_name)
        destination = Path(destination_folder +'/'+ file_name)

        if file_name == '00_output_result.txt':
            continue
        # copy only files
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('copied', file_name)

 
    output_path = {'output_path':to_path }
    result_list.append(output_path)
    result_list = result_list+list_files_and_sizes.apply(to_path)
    print(result_list)
    return result_list
