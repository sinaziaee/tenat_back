import json
from pathlib import Path

def apply(result_list, output_path):
    
    json_result = json.dumps(result_list, sort_keys=True, indent=4,ensure_ascii=False)
    print('json_result= \n'+str(json_result))
    output_file = open(Path(output_path), 'w', encoding='utf-8')
    output_file.write(f'{str(json_result)}')
    output_file.flush()