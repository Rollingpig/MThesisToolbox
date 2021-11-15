import pandas as pd
import re
import os


def match_capacity(dictionary, train):
    if pd.isnull(train):
        return None

    keys = list(dictionary.index)
    for train_d in keys:
        # print(train_d, train)
        t = re.search(train_d, train)
        # print(t)
        if t:
            return dictionary.loc[train_d, 'capacity']
    return None


def is_large(capacity):
    if pd.isnull(capacity):
        return 'Unknown'
    if capacity > 800:
        return '大编组'
    else:
        return '小编组'


def add_capacity(file=''):
    d = pd.read_csv(file)

    train_dictionary = pd.read_csv('inputs/capacity.csv', index_col=0)
    train_dictionary['capacity'].astype(int)
    d['capacity'] = d['train'].apply(lambda x: match_capacity(train_dictionary, x))
    d['编组'] = d['capacity'].apply(lambda x: is_large(x))
    d['列车类型'] = ''
    for index, item in d.iterrows():
        if item['编组'] == 'Unknown':
            if re.search('[GDC]', item['车次']):
                d.loc[index, '编组'] = '小编组'
            else:
                d.loc[index, '编组'] = '大编组'
        if re.search('[GDC]', item['车次']):
            d.loc[index, '列车类型'] = 'G/D/C'
        else:
            d.loc[index, '列车类型'] = 'K/T/Z'
    return d


if __name__ == '__main__':
    data = []
    for root, dirs, files in os.walk('processed/train_added'):
        for f in files:
            path = os.path.join(root, f)
            data.append(add_capacity(path))
    res = pd.concat(data)
    res.to_csv('processed/cap_all.csv', index=False)
