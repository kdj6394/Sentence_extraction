# abstractive summarization

from lib import *

def read_json(json_path):
    with open(json_path,'r',encoding='utf-8') as r_j:
        return json.load(r_j)

if __name__ == '__main__':
    root = sys.argv[1]
    refined_data_path = join(root,'refined_done.json')

    refine_data = read_json(refined_data_path)
    print(refine_data)