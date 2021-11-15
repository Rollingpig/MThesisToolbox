import pandas as pd


def str_to_time(str):
    return int(str.split(':')[0]) * 60 + int(str.split(':')[1])


def from_ip138(file='inputs/raw_shenzhen_20210818_i.csv'):
    """
    只有终到站的Duration是正确的
    :param file:
    :return:
    """
    def add_minute(s: str):
        q = s.split('日')
        if len(q) == 1:
            return 0
        else:
            d = int(q[0].split('第')[1])
            return d * 24 * 60

    def modify(duration):
        if duration < 0:
            return duration + 24 * 60
        else:
            return duration

    head = ['车次', '等级', '始发站', '始发时间', '经过站',
            '经过站到达时间', '经过站发车时间', '终到站', '到达时间']
    res = pd.read_csv(file, header=0)[1:]
    res.columns = head
    res['duration'] = res['经过站到达时间'].apply(lambda x: add_minute(x))
    res['duration'] += res['到达时间'].apply(lambda x: str_to_time(x))
    res['duration'] -= res['始发时间'].apply(lambda x: str_to_time(x))
    res['duration'] = res['duration'].apply(lambda x: modify(x))
    res['arrival'] = res['到达时间'].apply(lambda x: str_to_time(x))
    return res


def read_and_get_terminal(file, terminal):
    input_file = file
    t = from_ip138(input_file)
    t = t[(t.终到站 == terminal)]
    file_name = input_file.split('raw_')[1]
    t.to_csv('processed/first_processed/pro_' + file_name, encoding='utf-8')
    return t


if __name__ == '__main__':
    read_and_get_terminal('inputs/raw_guangzhou_20210826_i.csv', '广州')
    read_and_get_terminal('inputs/raw_guangzhoudong_20210826_i.csv', '广州东')
    read_and_get_terminal('inputs/raw_guangzhounan_20210826_i.csv', '广州南')
