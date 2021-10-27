from scripts import check_path, list_files, folder_creator,save_json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pathlib import Path
import json

# function for get text of input file (result is list of terms)
def get_text(file_name):
    f = open(Path(file_name), 'r', encoding='utf8')
    text = f.read()
    doc_name = str(file_name).split('/')[-1].split('\\')[-1]
    f.flush()
    text_list = text.split('\n')
    return text_list

def apply(from_path, to_path, name,graph_type,min_sim):

    from_path = from_path
    to_path = check_path.apply(to_path)
    target_folder_path = from_path.replace('result',to_path+'/result')
    folder_creator.apply(target_folder_path)

    # get files of from_path
    file_list = list_files.apply(from_path)
    output_path = {'output_path': target_folder_path}
    result_list = []
    result_list.append(output_path)

    output_file_path = target_folder_path + '/00_output_result.txt'
    data_file = target_folder_path + '/00_graph_data.json'

    result_dict = {}


    data = {}
    nodes = []
    edges = []
    for file in file_list:
        doc_name = str(file).split('/')[-1].split('\\')[-1]

        if doc_name == '00_output_result.txt' or doc_name == '00_graph_data.json':
                continue
            
        node = {'id':doc_name}
        nodes.append(node)

    # calculate sim between each pair of documents
    for i in range(0,len(file_list)-1):
        for j in range(i+1,len(file_list)):
            # get source and target doc
            source_doc = file_list[i]
            target_doc = file_list[j]

            source_doc_name = str(source_doc).split('/')[-1].split('\\')[-1]
            target_doc_name = str(target_doc).split('/')[-1].split('\\')[-1]
            if source_doc_name == '00_output_result.txt' or target_doc_name == '00_graph_data.json':
                continue
            source_text = get_text(source_doc)
            target_text = get_text(target_doc)

            union = list(set(source_text) | set(target_text))
            intersect = list(set(source_text) & set(target_text))

            jaccard_sim = round(len(intersect)/len(union),3)
            if(jaccard_sim >= min_sim):
                result_dict = {'source':source_doc_name,'target':target_doc_name,'sim':jaccard_sim}
                result_list.append(result_dict)
                edge = {'from':source_doc_name,'to':target_doc_name}
                edges.append(edge)
    data = {'nodes':nodes,'edges':edges}
    # save to output file
    save_json.apply(data,data_file)
    save_json.apply(result_list,output_file_path)
    return result_list

        

