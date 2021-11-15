import matplotlib.pyplot as plt

from SimulationDataAnalysis.basicTool.DataReader import BasicIndividualDataReader, LOSReader
from SimulationDataAnalysis.basicTool.basicVisualization import violin


class BasicIndividualViolin:

    @staticmethod
    def read(files):
        return BasicIndividualDataReader().read_from_list(files)

    def draw(self, params, ylabel='换乘大厅通行耗时 (秒)', file_name='results/trip-interchange_lobby.png', ylim=(0, 400)):

        x_labels = ['传统安检', '安检互认', '人脸识别+安检互认']
        nrows = len(params) // 2
        fig, ax = plt.subplots(nrows=nrows, ncols=2, constrained_layout=True, sharey='row',
                               figsize=(6, 2.2 * nrows), )
        ymin, ymax = ylim

        for param in params:
            x, y = param["position"]
            data = self.read(param["file"])
            if len(params) <= 2:
                violin(ax[y], data, param["title"], x_labels)
                ax[0].set_ylabel(ylabel)
                ax[0].set_ylim([ymin, ymax])
            else:
                violin(ax[x][y], data, param["title"], x_labels)
                if y == 0:
                    ax[x][0].set_ylabel(ylabel)
                    ax[x][0].set_ylim([ymin, ymax])

        plt.savefig(file_name, dpi=200)


class LOSViolin(BasicIndividualViolin):
    @staticmethod
    def read(files):
        return LOSReader('E:/Master/Thesis/Simulation/current/results/los_time/').read_from_list(files)


