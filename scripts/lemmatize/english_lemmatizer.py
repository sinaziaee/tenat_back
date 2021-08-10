import nltk
from scripts import check_path, list_files, folder_creator, slicer
from scripts import base_script


def apply(from_path, to_path, name):
    lemmatizer = nltk.WordNetLemmatizer()
    return base_script.apply(from_path, to_path, name, lemmatizer.lemmatize)
