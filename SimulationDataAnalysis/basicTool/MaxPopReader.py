import pandas as pd

from SimulationDataAnalysis.basicTool.FlowDataReader import FlowDataReader


class MaxPopReader(FlowDataReader):

    @staticmethod
    def tag_by_file_name(data, file_name):
        """根据文件名给数据打标签"""
        try:
            i = file_name.index('lng')
            data['编组大小'] = '非城际列车'
        except ValueError:
            data['编组大小'] = '城际列车'
        try:
            i = file_name.index('2035')
            data['公交分担'] = '2035年'
        except ValueError:
            data['公交分担'] = '2045年'
        try:
            i = file_name.index('scr')
            try:
                i = file_name.index('noscr')
                data['安检模式'] = '安检互认'
            except ValueError:
                data['安检模式'] = '传统安检'
        except ValueError:
            data['安检模式'] = '人脸识别+安检互认'

        data['编组大小x公交分担'] = data['编组大小'] + " " + data['公交分担']
        data['label'] = data['编组大小'] + " " + data['公交分担'] + " " + data['安检模式']

        return data, data.loc[0, 'label']

    def read_and_pre_process(self, file: str, offset, period, field):
        series = self.get_max(file, field, period, offset)
        data = pd.DataFrame({})
        data['maxPop'] = series
        data, _ = self.tag_by_file_name(data, file)
        return data

    def read_from_list(self, param_list: list):
        """
        从一组文件名读取数据并预处理
        """
        res = []
        for fp in param_list:
            t_data = self.read_and_pre_process(**fp)
            res.append(t_data)
        return pd.concat(res)



