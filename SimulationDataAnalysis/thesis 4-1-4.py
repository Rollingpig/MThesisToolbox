from SimulationDataAnalysis.basicTool.statsCompare import PopCompare


if __name__ == '__main__':

    scr_check_not_affect = [
        [    # 安检流程的改进不会对地铁站台的人员聚集增量造成显著影响
            {'file': 'pop edge lng 2035 scr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2035 noscr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
        [  # 安检流程的改进不会对地铁站台的人员聚集增量造成显著影响
            {'file': 'pop edge lng 2045 scr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2045 noscr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
        [  # 安检流程的改进不会对地铁站台的人员聚集增量造成显著影响
            {'file': 'pop edge lng 2045 scr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2045 face.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
        [  # 在2045年分担率下，无论编组大小，安检互认与人脸识别模式下的铁路旅客在站台最高聚集人数的数值分布都没有显著差异
            {'file': 'pop edge lng 2045 noscr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2045 face.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
    ]
    scr_check_not_affect2 = [
        [  # 安检流程的改进不会对地铁站台的人员聚集增量造成显著影响
            {'file': 'pop edge shrt 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge shrt 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  # 安检流程的改进不会对地铁站台的人员聚集增量造成显著影响
            {'file': 'pop edge shrt 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge shrt 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  # 安检流程的改进不会对地铁站台的人员聚集增量造成显著影响
            {'file': 'pop edge shrt 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge shrt 2045 face.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  # 在2045年分担率下，无论编组大小，安检互认与人脸识别模式下的铁路旅客在站台最高聚集人数的数值分布都没有显著差异
            {'file': 'pop edge shrt 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge shrt 2045 face.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
    ]
    long_shifts_create_larger_crowd = [
        [  # 在2035年，大小编组的聚集水平差异仅在20人以下
            {'file': 'pop edge shrt 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2035 scr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
        [  # 在2035年，大小编组的聚集水平差异仅在20人以下
            {'file': 'pop edge shrt 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2035 noscr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
        [  # 在2045年，大小编组的聚集水平差异仅在20人以下
            {'file': 'pop edge shrt 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2045 scr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
        [  # 在2045年其差异便扩大了约一倍
            {'file': 'pop edge shrt 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2045 noscr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
        [  # 在2045年其差异便扩大了约一倍
            {'file': 'pop edge shrt 2045 face.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop edge lng 2045 face.csv', 'offset': 5, 'period': 10, 'field': 'mtr-platform'},
        ],
    ]
    not_affect_overall = [
        [  # 在相同分担率与列车开行方案（编组）下，安检模式对铁路旅客在站台最高聚集人数的数值分布均不造成显著差异
            {'file': 'pop shrt ran 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop shrt ran 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop lng ran 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop shrt ran 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2045 face.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop shrt ran 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop shrt ran 2045 face.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop lng ran 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop lng ran 2045 face.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop lng ran 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2045 face.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
    ]
    not_affect_overall2 = [
        [  # 安检流程的改进不会对地铁站台的人员聚集增量造成显著影响
            {'file': 'pop shrt ran 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
    ]
    not_affect_overall3 = [
        [  # 安检流程的改进不会对地铁站台的人员聚集增量造成显著影响
            {'file': 'pop shrt ran 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
        [  #
            {'file': 'pop shrt ran 2045 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
            {'file': 'pop lng ran 2045 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-platform'},
        ],
    ]
    # PopCompare().compare_max(long_shifts_create_larger_crowd)
    PopCompare().compare_distribution(not_affect_overall3)

