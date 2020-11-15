# train data refine

from lib import *

if __name__ == '__main__':
    # refine data
    root = sys.argv[1]
    raw_data = join(root,'train.jsonl')

    with open(raw_data,'r',encoding='utf-8') as raw:
        datas = raw.readlines()

    train_data_frame = pd.DataFrame()

    for data in tqdm(datas,ascii=True):
        data = json.loads(data)
        data_media,data_id = data['media'],data['id']
        data_ori,data_extract_index = data['article_original'],data['extractive']
        data_extract = list()
        for index in data_extract_index:
            data_extract.append(data_ori[index])
            
        # train_data_frame.loc[row_idx] = [data_id,data_media,data_extract_index,data_extract,data_ori]
        train_data_frame = train_data_frame.append({'id_index' : data_id, 'media' : data_media,
                                'extract_index' : data_extract_index, 'extract' : data_extract,
                                'article_original' : data_ori},ignore_index=True)
    
    save_path = join(root,'refined_done.csv')
    train_data_frame.to_csv(save_path,sep=',',na_rep='NaN')