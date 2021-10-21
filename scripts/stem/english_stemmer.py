from nltk import stem
from nltk.tokenize import word_tokenize
from scripts import list_files, check_path, folder_creator, slicer,save_json
from scripts import base_script
from pathlib import Path, PurePath

stemming_algorithms = ['Porter', 'Snowball', 'Lancaster']


def stemming(text, algorithm):
    if algorithm == stemming_algorithms[0]:
        stemmer = stem.PorterStemmer()
    elif algorithm == stemming_algorithms[1]:
        stemmer = stem.SnowballStemmer(language='english')
    elif algorithm == stemming_algorithms[2]:
        stemmer = stem.LancasterStemmer()
    else:
        stemmer = stem.PorterStemmer()
    words = word_tokenize(text)
    all_stemmed = []
    w_stemmes = []
    for word in words:
        stm = stemmer.stem(word)
        all_stemmed.append(stm)
        if word != stm:
            w_stemmes.append(f'{word} => {stm}')
    stemmed_text = ' '.join(all_stemmed)
    return {'text':stemmed_text, 'stemmed_words':w_stemmes, 'stemmed_count': len(w_stemmes)}

def apply(from_path, to_path, name, algorithm, token_count):
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
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(Path(file), 'r', encoding='utf8')
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result_file = str(file).replace('result',to_path+'/result')
        f_output = open(Path(result_file), 'w', encoding='utf-8')
        text = f.read()
        result = stemming(text, algorithm)
        stemmed_text = result['text']
        result_dict = {'doc_name':doc_name, 'top_stemmed':', '.join(result['stemmed_words'][:token_count]), 'stemmed_count':result['stemmed_count']}
        f_output.write(f'{stemmed_text}\n')
        f_output.flush()
        result_list.append(result_dict)
    save_json.apply(result_list,output_file_path)
    return result_list
