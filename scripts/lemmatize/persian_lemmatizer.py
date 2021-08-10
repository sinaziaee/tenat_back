import hazm
from scripts import check_path, list_files, folder_creator, slicer
from scripts import base_script


def apply(from_path, to_path, name):
    lemmatizer = hazm.Lemmatizer()
    return base_script.apply(from_path, to_path, name, lemmatizer.lemmatize)
