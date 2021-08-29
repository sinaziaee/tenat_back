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
    stemmed_text = stemmer.stem(text)
    all_stemmed = []
    counter = 0
    for word in words:
        stm = stemmer.stem(word)
        all_stemmed.append(f'{word} : {stm}')
    return {'text':stemmed_text, 'stemmed_words':all_stemmed}

def apply(from_path, to_path, name, algorithm, token_count):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/stemmed_text_and_words/{name}'
    folder_creator.apply(folder_path)
    result_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(result_file, 'w', encoding='utf8')
        text_result_file = str(file).replace(f'{from_path}', f'{to_path}/stemmed_text_and_words')
        f_text_output = open(text_result_file, 'w', encoding='utf8')
        text = f.read()
        result = stemming(text, algorithm)
        top_stemmed = " ,".join(result['stemmed_words'][:token_count])
        stemmed_text = result['text']
        result_dict = {'top_tokens':top_stemmed, 'result_link':result_file, 'text_result_file':text_result_file, 'doc':file}
        f_output.write(f'{str(result_dict)}\n')
        f_text_output.write(f'{stemmed_text}\n\n')
        for stm in result['stemmed_words']:
            f_text_output.write(f'{stm}\n')
        f.flush()
        f_output.flush()
        f_text_output.flush()
        result_list.append(result_dict)
    return result_list
