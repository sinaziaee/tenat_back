import patoolib
import os
from pathlib import Path
from scripts import list_files_and_sizes, folder_creator
import docx2txt
import zip_unicode


# from scripts import tfidf_per_doc, Ngram, wordCloud, LsiSimilarity, Definition, DocFeatures, wordCombGraph, \
#     InvertedIndex, DocSimilarityByKeyword, word2gramGraph, Paragraphs
# from scripts import DocumentList
# from scripts import CreateFolder
# from scripts import Graph
# from scripts import StemDic


def apply(zip_file):
    folder_name = str(os.path.basename(zip_file))
    folder_path = f'media/data/{folder_name}/'
    try:
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
        # patoolib.extract_archive(zip_file, outdir=folder_path, interactive=False)
        zip_ref = zip_unicode.ZipHandler(path=zip_file, extract_path=folder_path)
        zip_ref.extract_all()
    except OSError as error:
        print(error)
    files_list = []
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            files_list.append(fp)
    folder_path = folder_path.replace('data', 'result/raw_text')
    for file in files_list:
        doc_to_txt(folder_path, file)

    return list_files_and_sizes.apply(folder_path)


def doc_to_txt(folder_path, file):
    text = ''
    if str(file).endswith('.docx'):
        f = docx2txt.process(file)
        lines = f.split('\n')
        for line in lines:
            if line != '':
                text += line + '\n'
    else:
        f = open(file, 'r', encoding='utf8')
        for line in f.readlines():
            if line != '':
                text += line.replace('\n', '') + '\n'
        f.flush()
    folder_creator.apply(folder_path)
    file = file.split('/')[-1].replace('.docx', '.txt')
    f = open(os.path.join(folder_path, file), 'w', encoding='utf-8')
    f.write(text)
    f.flush()

    # mapList = []

    # for path, dirs, files in os.walk(folder_path):
    #     for f in files:
    #         fp = os.path.join(path, f)
    #         # size += os.path.getsize(fp)
    #         name = fp.split('/')[-1]
    #         new_map = {name, os.path.getsize(fp)}
    #         mapList.append(new_map)
    #
    # return mapList

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
