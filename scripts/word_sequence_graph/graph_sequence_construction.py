from scripts.word_sequence_graph import graph
from scripts import check_path, folder_creator, list_files, save_json


def dictionary_to_string(words_dict):
    result = ''
    for key in words_dict.keys():
        result += f'{words_dict[key].word}: {words_dict[key].index} -> '
        for graph in words_dict[key].prev:
            if graph is not None:
                result += graph.word + ', '
            else:
                result += '<START>, '
        result += '\n'
    return result


def create_graph_sequence(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    words_dict = {}

    for l in range(len(lines)):
        line = lines[l].replace('\n', '')
        words = line.split(' ')
        for w in range(len(words)):
            word = words[w]
            index = str(f'{l}:{w}')
            if word not in words_dict:
                if w == 0:
                    prev = None
                else:
                    prev = words_dict[words[w - 1]]
                words_dict[word] = graph.Graph(word, [index], [prev])
            else:
                words_dict[word].index.append(index)
                if w - 1 == -1:
                    words_dict[word].prev.append(None)
                else:
                    words_dict[word].prev.append(words_dict[words[w - 1]])
    return words_dict


file_path = '../media/english_sample2.rar/raw_text/result/Computer_Science31.txt'
print(dictionary_to_string(create_graph_sequence(file_path)))
