def apply(path):
    path = str(path)
    if 'import' in path or 'Sample_Data' in path or 'raw' in path or 'text' in path or 'Import_Collection' in path:
        return 'raw_text'
    elif 'tok' in path or 'Tokenization' in path:
        return 'tokenized'
    elif 'norm' in path:
        return 'normalized'
    elif 'statistics' in path or 'Doc_Statistics' in path:
        return 'doc_statistics'
    elif 'stem' in path or 'Stemming' in path:
        return 'stemmed'
    elif 'stop' in path or 'Stopword_Removal' in path:
        return 'stop_word'
    elif 'lemmat' in path or 'limmat' in path:
        return 'lemmatized'
    elif 'graph_creation' in path or 'graph_construction' in path:
        return 'graph_construction'
    elif 'TF_IDF' in path or 'tf_idf' in path:
            return 'tf_idf'
    elif 'join' in path or 'Join' in path:
            return 'join'

    elif 'topic_modeling' in path or 'Topic_Modeling' in path:
            return 'topic_modeling'
    elif 'entity_recognition' in path or 'Entity_Recognition' in path:
            return 'entity_recognition'
    elif 'graph_sequence' in path or 'sequence_graph' in path or 'sequence' in path:
            return 'graph_sequence'
