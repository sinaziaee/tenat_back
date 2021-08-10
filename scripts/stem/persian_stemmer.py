from nltk import stem
from scripts import list_files, check_path, folder_creator, slicer
import hazm
from scripts import base_script

stemming_algorithms = ['Porter', 'Snowball', 'Lancaster']


def apply(from_path, algorithm, to_path, name):
    stemmer = hazm.Stemmer()
    return base_script.apply(from_path, to_path, name, stemmer.stem)
