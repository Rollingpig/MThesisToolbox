import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.stats.api as sms

from SimulationDataAnalysis.basicTool.DataReader import BasicIndividualDataReader, LOSReader
from SimulationDataAnalysis.basicTool.FlowDataReader import FlowDataReader


def normality(r1: pd.Series):
    r = (r1 - r1.mean()) / r1.std()
    stat, pv1 = stats.kstest(r, 'norm')
    if pv1 < 0.005:
        return False, stat, pv1
    else:
        return True, stat, pv1


def get_ci(r1: pd.Series, r2: pd.Series):
    cm = sms.CompareMeans(sms.DescrStatsW(r1), sms.DescrStatsW(r2))
    ib, it = cm.tconfint_diff(usevar='unequal')
    return ib, it


def two_group_compare(r1, r2):
    print(normality(r1), normality(r2))
    res = '[data1] len = {:d} mean = {:.2f}, 75% percentile = {:.2f}\n' \
          '[data2] len = {:d} mean = {:.2f}, 75% percentile = {:.2f}\n'. \
        format(len(r1), r1.mean(), np.percentile(r1, 75), len(r2), r2.mean(), np.percentile(r2, 75))

    stat, pv = stats.levene(r1, r2)
    if pv < 0.005:
        t, p = stats.ttest_ind(r1, r2, equal_var=False)
        res += 'welch t={:.2f}，p={:.4f}\n'.format(t, p)
    else:
        t, p = stats.ttest_ind(r1, r2, equal_var=True)
        res += 't={:.2f}，p={:.4f}\n'.format(t, p)

    stat, pv = stats.ks_2samp(r1, r2)
    res += 'Two Sample K-S Test h={:.3f} p={:.4f}\n'.format(stat, pv)

    ib, it = get_ci(r1, r2)
    res += 'MD={:.2f}，95%CI={:.2f}, {:.2f}'.format(r1.mean() - r2.mean(), ib, it)

    return res


class MeanCompare:

    @staticmethod
    def _read(files):
        return BasicIndividualDataReader().read_from_list(files)

    def compare_means(self, params):
        for param in params:
            data = self._read(param["file"])
            r1 = data[data['index'] == 0]["Duration"]
            r2 = data[data['index'] == 1]["Duration"]
            two_group_compare(r1, r2)


class PopCompare(MeanCompare):
    def compare_max(self, params):
        for p in params:
            data1 = FlowDataReader().get_max(p[0]["file"], p[0]['field'], p[0]['period'], p[0]['offset'])
            data2 = FlowDataReader().get_max(p[1]["file"], p[1]['field'], p[1]['period'], p[1]['offset'])
            two_group_compare(data1, data2)

    def compare_distribution(self, params):
        for p in params:
            data1 = FlowDataReader().read(p[0]["file"])[p[0]['field']]
            data2 = FlowDataReader().read(p[1]["file"])[p[1]['field']]
            two_group_compare(data1, data2)
