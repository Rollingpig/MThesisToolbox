import requests
from retrying import retry
import time
import random
import pandas as pd


def _get_url(shift):
    url = 'https://api.moerail.ml/train/%s' % shift
    return url


@retry(stop_max_attempt_number=3, wait_fixed=10000)
def get_json(shift):
    # print('g')
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'api.moerail.ml',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    }
    url = _get_url(shift)
    time.sleep(random.randint(1, 4))
    request = requests.get(url, headers=headers)

    if request.status_code != 200:
        print('error')
        return None

    return request.json()


def get_train(shift):
    js = get_json(shift)
    if js:
        print(js[0]['emu_no'])
        return js[0]['emu_no']
    else:
        print('no results')
        return ''


def add_train_type(file='processed/pro_shanghai_20210818_i.csv'):
    data = pd.read_csv(file, index_col=0)
    data['train'] = data['车次'].apply(lambda x: get_train(x))
    data.to_csv('processed/train_added/trn_' + file.split('/pro_')[-1], index=False)


if __name__ == '__main__':
    # print(get_train('G1'))
    # add_train_type('processed/pro_shenzhen_20210818_i.csv')
    # add_train_type('processed/pro_shanghaisouth_20210818_i.csv')
    # add_train_type('processed/pro_shanghaihongqiao_20210818_i.csv')
    # add_train_type('processed/pro_futian_20210818_i.csv')
    # add_train_type('processed/first_processed/pro_zhengzhoudong_20210818_i.csv')
    # add_train_type('processed/first_processed/pro_guangzhou_20210826_i.csv')
    add_train_type('processed/first_processed/pro_guangzhoudong_20210826_i.csv')
    add_train_type('processed/first_processed/pro_guangzhounan_20210826_i.csv')

