def apply(path):
    path = str(path)
    if 'tok' in path:
        return 'tokenized'
    elif 'norm' in path:
        return 'normalized'
    elif 'stem' in path:
        return 'stemmed'
    elif 'import' in path or 'raw' in path or 'text' in path:
        return 'raw_text'
    elif 'stop' in path:
        return 'stop_word'
    elif 'lemmat' in path or 'limmat' in path:
        return 'lemmatized'
