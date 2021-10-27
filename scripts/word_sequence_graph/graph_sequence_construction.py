from scripts.word_sequence_graph import graph
from scripts import check_path, folder_creator, list_files, save_json
from pathlib import Path, PurePath


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


def apply(from_path, to_path, name):
    from_path = from_path
    to_path = check_path.apply(to_path)
    target_folder_path = from_path.replace('result', to_path + '/result')
    folder_creator.apply(target_folder_path)

    # get files of from_path
    file_list = list_files.apply(from_path)
    output_path = {'output_path': target_folder_path}
    result_list = []
    result_list.append(output_path)

    output_file_path = target_folder_path + '/00_output_result.txt'
    for file in file_list:
        if '00_output_result' in file:
            continue
        f = open(Path(file), 'r', encoding='utf8')
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result_file = str(file).replace('result', to_path + '/result')
        f_output = open(Path(result_file), 'w', encoding='utf-8')
        result = dictionary_to_string(create_graph_sequence(file))
        f_output.write(f'{result}\n')
        f_output.flush()
        # result_list.append(result_dict)
    # save_json.apply(result_list,output_file_path)
    return result_list


# file_path = '../media/english_sample2.rar/raw_text/result/Computer_Science31.txt'
# result = dictionary_to_string(create_graph_sequence(file_path))

apply(from_path='../media/english_sample2.rar/raw_text/result/', to_path='graph_sequence', name='english_sample2.rar')
