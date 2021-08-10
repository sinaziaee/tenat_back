from nltk import stem
from scripts import list_files, check_path, folder_creator, slicer

stemming_algorithms = ['Porter', 'Snowball', 'Lancaster']


def apply(from_path, algorithm, to_path, name):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    if algorithm == stemming_algorithms[0]:
        stemmer = stem.PorterStemmer()
    elif algorithm == stemming_algorithms[1]:
        stemmer = stem.SnowballStemmer(language='english')
    elif algorithm == stemming_algorithms[2]:
        stemmer = stem.LancasterStemmer()
    else:
        stemmer = stem.PorterStemmer()
    folder_path = f'media/result/{from_path}/{name}/'
    files_list = list_files.apply(folder_path)
    output_file_list = []
    # print('*' * 100)
    # print(from_path)
    # print(to_path)
    # print(algorithm)
    # print(name)
    # print(folder_path)
    folder_path = f'media/result/{to_path}/{name}/'
    folder_creator.apply(folder_path)
    for file in files_list:
        f = open(file, 'r', encoding='utf8')
        file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(file, 'w', encoding='utf8')
        output_file_list.append(file)
        text = f.read()
        text = slicer.apply(text)
        for each in text:
            if each != '\n':
                stemmed = stemmer.stem(each)
                f_output.write(f'{stemmed} ')
        f.flush()
        f_output.flush()
    # print('*' * 100)
    return output_file_list
