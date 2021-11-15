import matplotlib.pyplot as plt
import Common
from SimulationDataAnalysis.basicTool.FlowDataReader import FlowDataReader


def pdf_pop(params, field, file_name='mtr-plt', file_prefix='pop-'):
    def read(file):
        return FlowDataReader('E:/Master/Thesis/Simulation/current/results/pop/').read(file)

    nrows = len(params) // 2
    fig, ax = plt.subplots(nrows=nrows, ncols=2, constrained_layout=True, sharey='row',
                           figsize=(6, 1.8 * nrows), )
    colors = ['red', 'orange', 'green']
    labels = ['传统安检', '安检互认', '人脸识别+安检互认']

    if len(params) <= 2:
        for param in params:
            x, y = param["position"]
            for ind, f in enumerate(param["file"]):
                ax[y].hist(read(f)[field], bins=[i for i in range(1000, 2200, 50)],
                           density=True, histtype='step', color=colors[ind], label=labels[ind])
                ax[y].set_xlabel("聚集人数")
        ax[1].legend()
        ax[0].set_ylabel("聚集人数分布概率")
    else:
        for param in params:
            x, y = param["position"]
            for ind, f in enumerate(param["file"]):
                data = read(f)[field]
                ax[x][y].hist(data, bins=[i for i in range(1000, 2200, 50)],
                           density=True, histtype='step', color=colors[ind], label=labels[ind])
                ax[x][y].set_title(param["title"])
                ax[x][0].set_ylabel("聚集人数分布概率")

                # print(data.mean())
        ax[-1][0].set_xlabel("聚集人数")
        ax[-1][1].set_xlabel("聚集人数")
        ax[-1][1].legend()

    plt.savefig('results/' + file_prefix + file_name + '.png', dpi=120)


if __name__ == '__main__':
    Common.set_plt()
    param1 = [
        {"position": (0, 0),
         "file": ['pop shrt ran 2035 scr.csv',
                  'pop shrt ran 2035 noscr.csv',
                  ],
         "title": '城际列车为主 2035',
         },
        {"position": (0, 1),
         "file": ['pop lng ran 2035 scr.csv',
                  'pop lng ran 2035 noscr.csv',
                  ],
         "title": '常速列车为主 2035'},
        {"position": (1, 0),
         "file": ['pop shrt ran 2045 scr.csv',
                  'pop shrt ran 2045 noscr.csv',
                  'pop shrt ran 2045 face.csv'],
         "title": '城际列车为主 2045',
         },
        {"position": (1, 1),
         "file": ['pop lng ran 2045 scr.csv',
                  'pop lng ran 2045 noscr.csv',
                  'pop lng ran 2045 face.csv',
                  ],
         "title": '常速列车为主 2045'},
    ]
    pdf_pop(param1, 'mtr-platform')
