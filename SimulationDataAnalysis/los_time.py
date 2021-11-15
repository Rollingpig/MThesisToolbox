from SimulationDataAnalysis.basicTool.Violin import LOSViolin
import Common


if __name__ == '__main__':
    Common.set_plt()
    param1 = [
        {"position": (0, 0),
         "file": ['los lobby edge shrt 2035 scr.csv',
                  'los lobby edge shrt 2035 noscr.csv',
                  ],
         "title": '小编组列车 2035'},
        {"position": (0, 1),
         "file": ['los lobby edge lng 2035 scr.csv',
                  'los lobby edge lng 2035 noscr.csv',
                  ],
         "title": '大编组列车 2035'},
        {"position": (1, 0),
         "file": ['los lobby edge shrt 2045 scr.csv',
                  'los lobby edge shrt 2045 noscr.csv',
                  'los lobby edge shrt 2045 face.csv'],
         "title": '小编组列车 2045'},
        {"position": (1, 1),
         "file": ['los lobby edge lng 2045 scr.csv',
                  'los lobby edge lng 2045 noscr.csv',
                  'los lobby edge lng 2045 face.csv',
                  ],
         "title": '大编组列车 2045'},
    ]
    param2 = [
        {"position": (0, 0),
         "file": ['los gate shrt ran 2045 scr.csv',
                  'los gate shrt ran 2045 noscr.csv',
                  'los gate shrt ran 2045 face.csv',
                  ],
         "title": '城际列车为主'},
        {"position": (0, 1),
         "file": ['los gate lng ran 2045 scr.csv',
                  'los gate lng ran 2045 noscr.csv',
                  'los gate lng ran 2045 face.csv',
                  ],
         "title": '常速列车为主'},
    ]
    param3 = [
        {"position": (0, 0),
         "file": ['los train mtr shrt ran 2035 scr.csv',
                  'los train mtr shrt ran 2035 noscr.csv',
                  ],
         "title": '城际列车为主 2035'},
        {"position": (0, 1),
         "file": ['los train mtr lng ran 2035 scr.csv',
                  'los train mtr lng ran 2035 noscr.csv',
                  ],
         "title": '常速列车为主 2035'},
        {"position": (1, 0),
         "file": ['los train mtr shrt ran 2045 scr.csv',
                  'los train mtr shrt ran 2045 noscr.csv',
                  'los train mtr shrt ran 2045 face.csv',
                  ],
         "title": '城际列车为主 2045'},
        {"position": (1, 1),
         "file": ['los train mtr lng ran 2045 scr.csv',
                  'los train mtr lng ran 2045 noscr.csv',
                  'los train mtr lng ran 2045 face.csv',
                  ],
         "title": '常速列车为主 2045'},
    ]
    # LOSViolin().draw(param2, ylabel='低于LOS B的持续时间 (秒)', file_name='gate', ylim=(-5, 70), file_prefix='los-')
    LOSViolin().draw(param3, ylabel='低于LOS B的持续时间 (秒)', file_name='train-to-mtr', ylim=(0, 600))
    # LOSViolin().draw(param1, ylabel='低于LOS B的持续时间 (秒)', file_name='lobby', ylim=(0, 350), file_prefix='los-')

