def apply(path):
    path = str(path)
    print('path is: '+path)
    if 'tok' in path or 'Tokenization' in path:
        return 'tokenized'
    elif 'norm' in path:
        return 'normalized'
    elif 'statistics' in path:
        return 'doc_statistics'
    elif 'stem' in path or 'Stemming' in path:
        return 'stemmed'
    elif 'import' in path or 'raw' in path or 'text' in path or 'Import_Collection' in path:
        return 'raw_text'
    elif 'stop' in path or 'Stopword_Removal' in path:
        return 'stop_word'
    elif 'lemmat' in path or 'limmat' in path:
        return 'lemmatized'
