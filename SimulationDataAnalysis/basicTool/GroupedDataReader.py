import pandas as pd

from SimulationDataAnalysis.basicTool.DataReader import BasicDataReader


class GroupAveragedDataReader(BasicDataReader):
    """
    【总目标】文件读取与数据预处理
    读取MassMotion导出的csv，并把trip time表与los time表，通过Agent ID合并在一起
    对单班次列车下的所有旅客的trip duration与los duration求均值
    合并多个文件里的数据，并根据文件名给数据打上新的标签
    """
    @staticmethod
    def average_by_shift(data: pd.DataFrame, period):
        """
        把模拟数据文件，按每班列车分组截断，求每班列车所有旅客的trip duration与los duration的均值
        """
        group_num = data['Start Time'].max() // period
        res = []
        for i in range(group_num):
            data_slice = data[(data['Start Time'] >= period * i) & (data['Start Time'] < period * (i + 1))]
            res.append({'Duration': data_slice['Duration'].mean(), 'LOS Duration': data_slice['LOS Duration'].mean()})
        return pd.DataFrame(res)

    def read_and_pre_process(self, trip_filepath: str, los_filepath: str, grouped=True):
        # 把trip time表与los time表，通过Agent ID合并在一起
        data = self.read_simulation_file(trip_filepath)
        data2 = self.read_simulation_file(los_filepath)
        data = pd.merge(data, data2, on='Agent ID')

        # 转换某些字段的数据格式，并计算新的字段
        data = self.convert_time_for_keys(data, ['Duration', 'Start Time', 'End Time', 'LOS C Duration',
                                                 'LOS D Duration', 'LOS E Duration', 'LOS F Duration'])
        data['LOS Duration'] = data['LOS E Duration'] + data['LOS F Duration']\
                               + data['LOS C Duration'] + data['LOS D Duration']

        # 根据文件名给数据打标签
        # 并判断分组求均值时的片段长度，小编组的片段是7分钟，大编组是10分钟
        try:
            i = trip_filepath.index('lng')
            if grouped:
                data = self.average_by_shift(data, 10 * 60)
            data['编组大小'] = '非城际列车'
        except ValueError:
            if grouped:
                data = self.average_by_shift(data, 7 * 60)
            data['编组大小'] = '城际列车'

        # 根据文件名给数据打标签
        try:
            i = trip_filepath.index('2035')
            data['公交分担'] = '2035年'
        except ValueError:
            data['公交分担'] = '2045年'
        try:
            i = trip_filepath.index('scr')
            try:
                i = trip_filepath.index('noscr')
                data['安检模式'] = '安检互认'
            except ValueError:
                data['安检模式'] = '传统安检'
        except ValueError:
            data['安检模式'] = '人脸识别+安检互认'
        data['编组大小x公交分担'] = data['编组大小'] + " " + data['公交分担']

        return data

    def read_from_list(self, trip_filepath_list: list, los_filepath_list: list):
        """
        从一组文件名读取数据并预处理
        """
        res = []
        for i, fp in enumerate(trip_filepath_list):
            t_data = self.read_and_pre_process(fp, los_filepath_list[i])
            res.append(t_data)
        return pd.concat(res)
