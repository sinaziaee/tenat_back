from nltk import stem
from nltk.tokenize import word_tokenize
from scripts import list_files, check_path, folder_creator, slicer
from scripts import base_script

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
            w_stemmes.append(stm)
    stemmed_text = ' '.join(all_stemmed)
    return {'text':stemmed_text, 'stemmed_words':w_stemmes, 'stemmed_count': len(w_stemmes)}

def apply(from_path, to_path, name, algorithm, token_count):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    output_file = open(result_all, 'w', encoding='utf-8')
    result_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(result_file, 'w', encoding='utf8')
        text = f.read()
        result = stemming(text, algorithm)
        stemmed_text = result['text']
        result_dict = {'top_stemmed':', '.join(result['stemmed_words'][:token_count]), 'stemmed_count':result['stemmed_count'], 'doc_name':doc_name}
        output_file.write(f'{str(result_dict)}\n')
        f_output.write(f'{stemmed_text}\n')
        f_output.flush()
        result_list.append(result_dict)
    result_list.append({'top_stemmed':'', 'stemmed_count':0, 'doc_name':'00_output_result.txt'})
    output_file.flush()
    return result_list
