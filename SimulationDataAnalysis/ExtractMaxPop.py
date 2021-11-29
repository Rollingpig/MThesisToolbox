from SimulationDataAnalysis.basicTool.MaxPopReader import MaxPopReader


def extract_max_pop(field='mtr-concourse', offset=5.0):
    """
    读取MassMotion中Population Count工具导出的csv列表
    将每个班次在给定地点的最高聚集人数提取出来
    导出成csv格式的列表
    """
    param = [
        {'file': 'pop edge shrt 2035 scr.csv', 'offset': offset, 'period': 7, 'field': field},
        {'file': 'pop edge shrt 2035 noscr.csv', 'offset': offset, 'period': 7, 'field': field},
        {'file': 'pop edge shrt 2035 face.csv', 'offset': offset, 'period': 7, 'field': field},
        {'file': 'pop edge shrt 2045 scr.csv', 'offset': offset, 'period': 7, 'field': field},
        {'file': 'pop edge shrt 2045 noscr.csv', 'offset': offset, 'period': 7, 'field': field},
        {'file': 'pop edge shrt 2045 face.csv', 'offset': offset, 'period': 7, 'field': field},
        {'file': 'pop edge lng 2035 scr.csv', 'offset': offset, 'period': 10, 'field': field},
        {'file': 'pop edge lng 2035 noscr.csv', 'offset': offset, 'period': 10, 'field': field},
        {'file': 'pop edge lng 2035 face.csv', 'offset': offset, 'period': 10, 'field': field},
        {'file': 'pop edge lng 2045 scr.csv', 'offset': offset, 'period': 10, 'field': field},
        {'file': 'pop edge lng 2045 noscr.csv', 'offset': offset, 'period': 10, 'field': field},
        {'file': 'pop edge lng 2045 face.csv', 'offset': offset, 'period': 10, 'field': field},
    ]
    r = MaxPopReader().read_from_list(param)
    r.to_csv('processed data/pop-' + field + '.csv')


if __name__ == '__main__':
    # extract_max_pop('mtr-concourse', 5)
    # extract_max_pop('Interchange', 1.5)
    extract_max_pop('mtr-concourse', 5)