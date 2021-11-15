from SimulationDataAnalysis.basicTool.statsCompare import PopCompare


if __name__ == '__main__':
    # section 4.1.3
    no_big_diff_in_2035 = [
        [
            {'file': 'pop edge shrt 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge lng 2035 scr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            {'file': 'pop edge shrt 2035 noscr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge lng 2035 noscr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            {'file': 'pop edge shrt 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge shrt 2035 noscr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            {'file': 'pop edge lng 2035 scr.csv', 'offset': 5, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge lng 2035 noscr.csv', 'offset': 5, 'period': 10, 'field': 'mtr-concourse'},
        ],
    ]
    long_shifts_lead_to_larger_pop_in_2045 = [
        [
            # 传统安检模式下大编组列车旅客在站厅的聚集人数相比于2035年将显著提升
            {'file': 'pop edge lng 2045 scr.csv', 'offset': 2, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge lng 2035 scr.csv', 'offset': 2, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            # 小编组有提升但幅度只有54%
            {'file': 'pop edge shrt 2045 scr.csv', 'offset': 2, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge shrt 2035 scr.csv', 'offset': 2, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            # 与大编组构成明显的差异
            {'file': 'pop edge lng 2045 scr.csv', 'offset': 2, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge shrt 2045 scr.csv', 'offset': 2, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            # 在安检互认模式下，小编组列车旅客的聚集水平将提高到与大编组类似
            {'file': 'pop edge lng 2045 noscr.csv', 'offset': 2, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge shrt 2045 noscr.csv', 'offset': 2, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            # 但大编组的聚集水平较传统安检模式不会继续升高
            {'file': 'pop edge lng 2045 noscr.csv', 'offset': 2, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge lng 2045 scr.csv', 'offset': 2, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            # 在安检互认的基础上进一步采取人脸识别，不会显著提升聚集水平
            {'file': 'pop edge shrt 2045 face.csv', 'offset': 2, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge shrt 2045 noscr.csv', 'offset': 2, 'period': 10, 'field': 'mtr-concourse'},
        ],
        [
            # 在安检互认的基础上进一步采取人脸识别，不会显著提升聚集水平
            {'file': 'pop edge lng 2045 face.csv', 'offset': 2, 'period': 7, 'field': 'mtr-concourse'},
            {'file': 'pop edge lng 2045 noscr.csv', 'offset': 2, 'period': 10, 'field': 'mtr-concourse'},
        ],
    ]
    los_are_not_affected = [
        {"file": ['los train mtr shrt ran 2045 scr.csv',
                  'los train mtr shrt ran 2045 noscr.csv', ], },
        {"file": ['los train mtr shrt ran 2045 face.csv',
                  'los train mtr shrt ran 2045 noscr.csv', ], },
        {"file": ['los train mtr shrt ran 2045 face.csv',
                  'los train mtr shrt ran 2045 scr.csv', ], },
        {"file": ['los train mtr lng ran 2045 scr.csv',
                  'los train mtr lng ran 2045 noscr.csv', ], },
        {"file": ['los train mtr lng ran 2045 face.csv',
                  'los train mtr lng ran 2045 noscr.csv', ], },
        {"file": ['los train mtr lng ran 2045 face.csv',
                  'los train mtr lng ran 2045 scr.csv', ], },
        {"file": ['los train mtr shrt ran 2045 face.csv',
                  'los train mtr lng ran 2045 face.csv', ], },
        {"file": ['los train mtr shrt ran 2045 noscr.csv',
                  'los train mtr lng ran 2045 noscr.csv', ], },
        {"file": ['los train mtr shrt ran 2045 scr.csv',
                  'los train mtr lng ran 2045 scr.csv', ], },

    ]
    los_are_affected_in_35 = [
        {"file": ['los train mtr shrt ran 2035 noscr.csv',
                  'los train mtr lng ran 2035 noscr.csv', ], },
        {"file": ['los train mtr shrt ran 2035 scr.csv',
                  'los train mtr lng ran 2035 scr.csv', ], },
        {"file": ['los train mtr shrt ran 2035 scr.csv',
                  'los train mtr shrt ran 2035 noscr.csv', ], },
        {"file": ['los train mtr lng ran 2035 scr.csv',
                  'los train mtr lng ran 2035 noscr.csv', ], },
    ]
    PopCompare().compare_max(long_shifts_lead_to_larger_pop_in_2045)

