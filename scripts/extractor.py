import patoolib
import os
from pathlib import Path
# from scripts import tfidf_per_doc, Ngram, wordCloud, LsiSimilarity, Definition, DocFeatures, wordCombGraph, \
#     InvertedIndex, DocSimilarityByKeyword, word2gramGraph, Paragraphs
# from scripts import DocumentList
# from scripts import CreateFolder
# from scripts import Graph
# from scripts import StemDic


def apply(zip_file):
    print('----------------------'*4)
    print(zip_file)
    # getting the name of the compressed file
    folder_name = str(os.path.basename(zip_file))
    dot_index = folder_name.rfind('.')
    type = folder_name[dot_index + 1:]
    folder_name = folder_name[:dot_index]
    folder_path = f'media/data/{folder_name}/'
    try:
        # check for existence of data folder
        if not os.path.isdir(f'media/data/'):
            dirname = os.path.dirname(__file__)
            path = Path(dirname).parent
            path = os.path.join(path, f'media/data')
            os.mkdir(path)
        if not os.path.isdir(f'media/data/{folder_name}'):
            dirname = os.path.dirname(__file__)
            path = Path(dirname).parent
            path = os.path.join(path, f'media/data/{folder_name}')
            os.mkdir(path)
        # extracting the compressed file
        # by adding parameter interactive=False we can avoid replace

        patoolib.extract_archive(zip_file, outdir=folder_path, interactive=False)
        # if type == "zip":
        #     patoolib.extract_archive(zip_file, outdir=f'media/data/{folder_name}/', interactive=False)
        # elif type == "rar":
        #     # patoolib.extract_archive(zip_file, outdir=f'media_cdn/data/{folder_name}/', interactive=False, program=r"S:\UnrarDLL\x64\UnRAR64.dll")
        #     patoolib.extract_archive(zip_file, outdir=f'media/data/{folder_name}/', interactive=False)
    except OSError as error:
        print(error)

    mapList = []

    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            # size += os.path.getsize(fp)
            name = fp.split('/')[-1]
            new_map = {name, os.path.getsize(fp)}
            mapList.append(new_map)

    return mapList


    # Manual set path in windows
    # folder_name = "Fava_c"

    # CreateFolder.apply(folder_name)
    # tfidf_per_doc.start_tfidf(folder_name)
    # DocumentList.apply(folder_name)
    # Graph.apply(folder_name)
    # StemDic.apply(folder_name)
    # Ngram.apply(folder_name, 2)
    # Ngram.apply(folder_name, 3)
    # wordCloud.apply(folder_name)
    # LsiSimilarity.apply(folder_name)
    # Definition.apply(folder_name)
    # DocFeatures.apply(folder_name)
    # wordCombGraph.apply(folder_name)
    # InvertedIndex.apply(folder_name)
    # DocSimilarityByKeyword.apply(folder_name)
    # word2gramGraph.apply(folder_name)
    # Paragraphs.apply(folder_name)

# extractor('media_cdn/docs/zips/fava.rar')
