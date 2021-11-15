import pandas as pd
from scipy import stats

from SimulationDataAnalysis.basicTool.DataReader import BasicDataReader


class FlowDataReader(BasicDataReader):
    working_dir = 'E:/Master/Thesis/Simulation/current/results/pop/'

    @staticmethod
    def __split_simulation_data(data: pd.DataFrame, field,
                                simulation_period, sample_offset, bin_size=10):
        """
        将重复模拟形成的单个数据文件，拆开成多个数据组
        :param data: 读取好的pandas.DataFrame对象
        :param field: 查询字段
        :param simulation_period: 数据组开始时刻的间距（分钟），
        :param sample_offset:
        :param bin_size: 原数据的统计单元大小，单位：秒
        :return: 字典构成的数据，字典的Key是时间（秒），字典的值是每分钟流量
        """
        sim_period_in_data_pts = int(simulation_period * 60 / bin_size)
        sample_offset_in_data_pts = int(sample_offset * 60 / bin_size)

        res = []
        for i in range(sample_offset_in_data_pts, len(data), sim_period_in_data_pts):
            s = {}
            for j in range(sim_period_in_data_pts):
                if i + j < len(data) - 1:
                    s[(sample_offset_in_data_pts + j) * bin_size] = data.loc[i + j, field] * 1
            res.append(s)
        # print(len(res))
        return pd.DataFrame(res[1:-1])

    @staticmethod
    def __get_maximums(data: pd.DataFrame, field,
                       simulation_period, sample_offset, bin_size=10):
        """
        将重复模拟形成的单个数据文件，拆开成多个数据组
        :param data: 读取好的pandas.DataFrame对象
        :param field: 查询字段
        :param simulation_period: 数据组开始时刻的间距（分钟），
        :param sample_offset:
        :param bin_size: 原数据的统计单元大小，单位：秒
        :return: 字典构成的数据，字典的Key是时间（秒），字典的值是每分钟流量
        """
        sim_period_in_data_pts = int(simulation_period * 60 / bin_size)
        sample_offset_in_data_pts = int(sample_offset * 60 / bin_size)

        res = []
        for i in range(sample_offset_in_data_pts, len(data), sim_period_in_data_pts):
            t = min(i + sim_period_in_data_pts, len(data))
            s = data.loc[i: t, field].max()
            res.append(s)
        # print(len(res))
        return pd.Series(res[1:-1])

    @staticmethod
    def data_process(data, simulation_period, sample_offset, bin_size=10):
        # 计算各时间段流量数据的均值与标准差
        r_mean = []
        upper = []
        lower = []
        for key in data.keys():
            m = data[key].mean()
            d = data[key].std()
            r_mean.append(m)
            # ci = stats.t.interval(0.99, df=len(data[key]) - 1, loc=m, scale=stats.sem(data[key]))
            # upper.append(ci[1])
            # lower.append(ci[0])
            upper.append(m + 2 * d)
            lower.append(m - 2 * d)

        sim_period_in_data_pts = int(simulation_period * 60 / bin_size)
        sample_offset_in_data_pts = int(sample_offset * 60 / bin_size)
        x = [(sample_offset_in_data_pts + j) * bin_size for j in range(sim_period_in_data_pts)]
        return r_mean, upper, lower, x

    def read_split_and_process(self, file, field, simulation_period, sample_offset, bin_size=30):
        d = self.read_simulation_file(file)
        d = self.__split_simulation_data(d, field,
                                         simulation_period, sample_offset, bin_size)
        return self.data_process(d, simulation_period, sample_offset, bin_size)

    def get_max(self, file, field, simulation_period, sample_offset, bin_size=10):
        d = self.read_simulation_file(file)
        return self.__get_maximums(d, field, simulation_period, sample_offset, bin_size)

    def read(self, file):
        return self.read_simulation_file(file)