import array,json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scripts import check_path,folder_creator,list_files,save_json
from pathlib import Path
import pickle
def get_text(file_name):
    f = open(Path(file_name), 'r', encoding='utf8')
    text = f.read()
    doc_name = str(file_name).split('/')[-1].split('\\')[-1]
    f.flush()
    return text

def apply(from_path,to_path,name):


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



    doc_list = []
    for file in file_list:
        file_name = str(file).split('/')[-1].split('\\')[-1]
        if file_name == '00_output_result.txt':
                continue
        doc_list.append(get_text(file))


    tfidf = TfidfVectorizer(use_idf=True)
    response = tfidf.fit_transform(doc_list)
    feature_names = tfidf.get_feature_names()
    
    
    # for col in response.nonzero()[1]:
    #     print (feature_names[col], ' - ', response[0, col])
    result_list = []
    res = list(response)
    # for file in file_list:
    #     file_name = str(file).split('/')[-1].split('\\')[-1]
    #     result_list.append({'doc':file_name,'weight':response[0,term]})


    # for i, feature in enumerate(feature_names):
    #     print(i, feature)

    # for i in range(0,len(file_list)):
    #     file_name = str(file_list[i]).split('/')[-1].split('\\')[-1]

    #     for j, feature in enumerate(feature_names):
    #             # print(j, feature)
    #             res ={'doc':file_name,'term':feature,'weight':response[i,j]}
    #             result_list.append(res)
    # json_result = pickle.dumps(res)
    # # print('json_result= \n'+str(json_result))
    # output_file = open(Path(output_path), 'w', encoding='utf-8')
    # output_file.write(f'{str(json_result)}')
    # output_file.flush()
    return result_list