import graph

file_path = '../media/english_sample2.rar/raw_text/result/Computer_Science31.txt'

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
                prev = words_dict[words[w-1]]
            # if w == -1:
            #     next = None
            # else:
            #     next = words_dict[words[w+1]]
            # graph = graph.Graph(word, [index], prev, next)
            words_dict[word] = graph.Graph(word, [index], [prev])
        else:
            words_dict[word].index.append(index)
            print(words_dict.keys())
            if w-1 == -1:
                words_dict[word].prev.append(None)
            else:
                words_dict[word].prev.append(words_dict[words[w-1]])
file.flush()

for key in words_dict.keys():
    print(f'{words_dict[key].word}: {words_dict[key].index}', end=' -> ')
    for graph in words_dict[key].prev:
        if graph is not None:
            print(graph.word, end=', ')
        else:
            print('*N/A*', end='')
    print()
