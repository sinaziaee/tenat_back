from nltk import stem
from scripts import list_files, check_path, folder_creator, slicer
from scripts import base_script

stemming_algorithms = ['Porter', 'Snowball', 'Lancaster']


def apply(from_path, algorithm, to_path, name):
    if algorithm == stemming_algorithms[0]:
        stemmer = stem.PorterStemmer()
    elif algorithm == stemming_algorithms[1]:
        stemmer = stem.SnowballStemmer(language='english')
    elif algorithm == stemming_algorithms[2]:
        stemmer = stem.LancasterStemmer()
    else:
        stemmer = stem.PorterStemmer()

    return base_script.apply(from_path, to_path, name, stemmer.stem)
