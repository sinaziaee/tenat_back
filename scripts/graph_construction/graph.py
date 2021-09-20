from scripts import check_path, list_files, folder_creator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pathlib import Path


def get_text(file_name):
    f = open(Path(file_name), 'r', encoding='utf8')
    text = f.read()
    doc_name = str(file_name).split('/')[-1].split('\\')[-1]
    f.flush()
    text_list = text.split('\n')
    return text_list

def apply(from_path, to_path, name,graph_type,min_sim):
    to_path = check_path.apply(to_path)
    folder_path = from_path
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = '/'.join(from_path.split('/')[:-1]) + f'/{to_path}/' + name
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    # output_file = open(Path(result_all), 'w', encoding='utf-8')
    # output_file.write(f'[\n')
    result_list = []
    output_path = {'output_path':folder_path }
    result_list.append(output_path)
    result_dict = {}

    # calculate sim between each pair of documents
    for i in range(0,len(file_list)-1):
        for j in range(i+1,len(file_list)):
            # get source and target doc
            source_doc = file_list[i]
            target_doc = file_list[j]

            source_doc_name = str(source_doc).split('/')[-1].split('\\')[-1]
            target_doc_name = str(target_doc).split('/')[-1].split('\\')[-1]
            if source_doc_name == '00_output_result.txt' or target_doc_name == '00_output_result.txt':
                continue
            source_text = get_text(source_doc)
            target_text = get_text(target_doc)

            union = list(set(source_text) | set(target_text))
            intersect = list(set(source_text) & set(target_text))

            jaccard_sim = round(len(intersect)/len(union),3)
            if(jaccard_sim >= min_sim):
                result_dict = {'source':source_doc_name,'target':target_doc_name,'sim':jaccard_sim}
                result_list.append(result_dict)

    # save to output file
    output_file = open(Path(result_all), 'w', encoding='utf-8')
    output_file.write(f'{str(result_list)}\n')
    output_file.flush()
    return result_list

        

