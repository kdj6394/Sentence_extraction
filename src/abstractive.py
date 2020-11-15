# abstractive summarization

from lib import *

if __name__ == '__main__':
    root = sys.argv[1]
    refined_data_path = join(root,'refined_done.csv')

    refined_data_frame = read_pd_csv(refined_data_path)
    train_data_frame = refined_data_frame.loc[:,['article_original','extract']]

    print(train_data_frame)