from nltk import stem
from scripts import list_files
from hazm import Stemmer

stemming_algorithms = ['Porter', 'Snowball', 'Lancaster']


def apply(from_path, algorithm, to_path, name):
    stemmer = Stemmer()
    files_list = list_files.apply(from_path)
    output_file_list = []
    for file in files_list:
        f = open(file, 'r', encoding='utf8')
        file = str(file).replace(f'{from_path}', f'{to_path}')
        print(file)
        f_output = open(file, 'w', encoding='utf8')
        output_file_list.append(file)
        text = f.read()
        stemmed = stemmer.stem(text)
        f_output.write(stemmed)
        f.flush()
        f_output.flush()
    return output_file_list
