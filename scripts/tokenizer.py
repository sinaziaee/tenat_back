import os
from scripts import list_files, folder_creator, check_path
import hazm
import string
ignoreList = ["!", "@", "$", "%", "^", "&","#" "*", "(", ")", "_", "+", "-", "/", "*", "'", "،", "؛", ",", ""
                      "{","}",":",";",'=',"|",
                      "[", "]", "«", "»", "<", ">", ".", "?", "؟", "\n", "\t", '"',"“","”","\u200c","\u200e"
                      '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰', "٫",
                      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# def apply(name, splitter, from_path, to_path, tokens_count):
#     from_path = check_path.apply(from_path)
#     to_path = check_path.apply(to_path)
#     folder_path = f'media/result/{from_path}/{name}/'
#     files_list = list_files.apply(folder_path)
#     folder_path = folder_path.replace(f'{from_path}', f'{to_path}')
#     for file in files_list:
#         f = open(file, 'r', encoding="utf-8")
#             # print(r['body'], file=f)
#         text = f.read()
#         f.flush()
#         writer_hazm(folder_path, str(file), text, splitter)
#     files_list = list_files.apply(folder_path)
#     # return files_list
#     return show_files(files=files_list, tokens_count=tokens_count)[:-1]


# def writer_hazm(folder_path, file, text, splitter):
#     file = str(file)
#     file = file.split('/')[-1]
#     folder_creator.apply(folder_path)
#     filename = str(file).replace('.docx', '.txt')
#     f = open(os.path.join(folder_path, filename), 'w')
#     # temp = hazm.word_tokenize(text)
#     for item in ignoreList:
#         text = text.replace(item, " ")
#     print(text)
#     tmp = [word.lower() for word in text.split(splitter) if word != ""]
#     print(tmp)
#     for each in temp:
#         f.write(f'{each}\n')
#     f.flush()


# def show_files(files, tokens_count):
#     result_list = []
#     result_file = str(files[0]).replace(os.path.basename(str(files[0])), '00_output_result.txt')
#     output_file = open(result_file, 'w', encoding='utf-8')
#     for each in files:
#         token_counter = 0
#         file_name = os.path.basename(str(each))
#         first_top_tokens = ''
#         f = open(str(each), 'r', encoding='utf-8')
#         for line in f.readlines():
#             line = line.replace('\n', '')
#             token_counter += 1
#             if token_counter < tokens_count:
#                 first_top_tokens += line + ', '
#             elif token_counter == tokens_count:
#                 first_top_tokens += line
#             else:
#                 pass
#         f.flush()
#         new_map = {'doc_name': file_name, 'tokens_count': token_counter, 'tokens': first_top_tokens, 'link': each}
#         if file_name != '00_output_result.txt':
#             output_file.write(f'{str(new_map)}\n')
#             result_list.append(new_map)
#     output_file.flush()
#     return result_list

def tokenize_text(text, doc_name, splitter):
    for item in ignoreList:
        text = text.replace(item, " ")
    word_tokens = [word.lower() for word in text.split(splitter) if word != ""]
    return ({'doc_name':doc_name, 'tokens': word_tokens })

def apply(from_path, to_path, name, splitter, tokens_count):
    from_path = check_path.apply(from_path)
    to_path = check_path.apply(to_path)
    folder_path = f'media/result/{from_path}/{name}'
    file_list = list_files.apply(folder_path)
    folder_creator.apply(folder_path)
    folder_path = f'media/result/{to_path}/{name}'
    folder_creator.apply(folder_path)
    result_all = folder_path + '/00_output_result.txt'
    output_file = open(result_all, 'w', encoding='utf-8')
    result_list = []
    for file in file_list:
        f = open(file, 'r', encoding='utf8')
        result_file = str(file).replace(f'{from_path}', f'{to_path}')
        f_output = open(result_file, 'w', encoding='utf8')
        text = f.read()
        doc_name = str(file).split('/')[-1].split('\\')[-1]
        result = tokenize_text(text, doc_name, splitter)
        for tok in result['tokens']:
            f_output.write(f'{tok}\n')
        result['top_tokens'] = ', '.join(result['tokens'][:tokens_count])
        result_dict = {'doc_name':result['doc_name'], 'top_tokenized': result['top_tokens']}
        output_file.write(f'{str(result_dict)}\n')
        f.flush()
        result_list.append(result_dict)
    output_file.flush()
    return result_list
