import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols


def platform_one_way_anova():
    # 针对安检流程改进的one-way anova
    # 结果显示：安检流程的改进不会对地铁站台内铁路旅客的通行耗时与低水平持续时间造成明显影响
    data = pd.read_csv('processed data/trip-platform.csv')
    data2 = pd.read_csv('processed data/pop-mtr-platform.csv')
    types = list(data.value_counts('编组大小x公交分担').index)
    for t in types:
        print(t)
        mod = ols('Duration ~ 安检模式', data=data[data.编组大小x公交分担 == t]).fit()
        aov_table = sm.stats.anova_lm(mod, typ=2)
        #print(aov_table)
        data['LOS_Duration'] = data['LOS Duration']
        mod = ols('LOS_Duration ~ 安检模式', data=data[data.编组大小x公交分担 == t]).fit()
        aov_table = sm.stats.anova_lm(mod, typ=2)
        #print(aov_table)
        mod = ols('maxPop ~ 安检模式', data=data2[data2.编组大小x公交分担 == t]).fit()
        aov_table = sm.stats.anova_lm(mod, typ=2)
        print(aov_table)


if __name__ == '__main__':
    platform_one_way_anova()

