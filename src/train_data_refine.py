# train data refine

from lib import os,join,basename,json,sys

if __name__ == '__main__':
    # refine data
    root = sys.argv[1]
    raw_data = join(root,'train.jsonl')

    with open(raw_data,'r',encoding='utf-8') as raw:
        datas = raw.readlines()

    refined_done = dict()

    for data in datas:
        refined = dict()
        data = json.loads(data)
        data_media,data_id = data['media'],data['id']
        data_ori,data_extract_index = data['article_original'],data['extractive']
        data_extract = list()
        for index in data_extract_index:
            data_extract.append(data_ori[index])
        
        refined[data_id] = dict()
        refined[data_id]['media'] = data_media
        refined[data_id]['extract'] = data_extract
        refined[data_id]['extract_index'] = data_extract_index
        refined[data_id]['article_orginal'] = data_ori
    
        refined_done.update(refined)
        print(refined)
    
    save_path = join(root,'refined_done.json')
    with open(save_path,'w',encoding='utf-8') as s_p:
        json.dump(refined_done,s_p,indent=4,ensure_ascii=False)
