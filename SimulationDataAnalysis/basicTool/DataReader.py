import pandas as pd


class BasicDataReader:
    working_dir = 'E:/Master/Thesis/Simulation/current/results/'

    def __init__(self, working_dir=None):
        if working_dir:
            self.working_dir = working_dir

    def read_simulation_file(self, path: str):
        raw = pd.read_csv(self.working_dir + path, comment='#')
        return raw

    @staticmethod
    def convert_time_for_keys(data: pd.DataFrame, keys: list):
        def convert_time(time_str: str):
            return int(time_str.split(':')[0]) * 3600 + int(time_str.split(':')[1]) * 60 + int(time_str.split(':')[2])
        for key in keys:
            if key in data.keys():
                data[key] = data[key].apply(lambda x: convert_time(x))
        return data


class BasicIndividualDataReader(BasicDataReader):

    def read_and_pre_process(self, filepath: str):
        data = self.read_simulation_file(filepath)
        return self.convert_time_for_keys(data, ['Duration', 'Start Time', 'End Time'])

    def __get_data(self, filepath):
        """
        从文件名（或一组文件名）读取数据并预处理
        """
        if type(filepath) == str:
            return self.read_and_pre_process(filepath)
        else:
            # 从多个文件中读取数据，并将它们拼合在一起
            res = []
            for fp in filepath:
                t_data = self.read_and_pre_process(fp)
                res.append(t_data)
            return pd.concat(res)

    def read_from_list(self, files, labels=None):
        """
        从文件列表中读取数据到DataFrame对象
        :param files: 文件列表
        :param labels: 不同文件的数据标签，默认是0,1,2..
        :return: 一个单一的pandas.DataFrame对象
        """
        data = pd.DataFrame({})
        for i, f in enumerate(files):
            dat = self.__get_data(f)
            if labels:
                dat['index'] = labels[i]
            else:
                dat['index'] = i
            if len(data) != 0:
                data = data.append(dat)
            else:
                data = dat
        return data


class LOSReader(BasicIndividualDataReader):
    def read_and_pre_process(self, filepath, base_level='C'):
        data = self.read_simulation_file(filepath)
        data = self.convert_time_for_keys(data, ['LOS C Duration', 'LOS D Duration',
                                                 'LOS E Duration', 'LOS F Duration'])
        if base_level == 'C':
            data['Duration'] = data['LOS E Duration'] + data['LOS F Duration'] \
                               + data['LOS C Duration'] + data['LOS D Duration']
        else:
            data['Duration'] = data['LOS E Duration'] + data['LOS F Duration']
        return data


