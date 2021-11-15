import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from patsy import dmatrices
import math

from Common import set_plt


# Public vars
input_labels = ['avg_spd', 'std_spd', 'grp_shr', 'str_cst', 'trl_shr', 'avg_int', 'ctrl_par']
output_labels = ['MDB', 'ATR', 'MFR']
light_colors = ['powderblue', 'pink', 'wheat', ]
input_colors = ['red', 'darkorange', 'gold', 'green', 'darkturquoise', 'dodgerblue', 'purple']
input_markers = ['o', 'x', '^', 's', '+', 'H', '.']
colors = ['steelblue', 'red', 'brown', ]
titles = ['瓶颈最大密度(MDB)', '平均时间冗余比(ATR)', '最大流量(MFR)']


def regression2(file, sample_num=200):
    result = pd.read_csv(file)
    result = result[:sample_num]
    std = result.std()
    x_std = pd.DataFrame([std[input_labels], std[input_labels], std[input_labels]])

    for output in output_labels:
        # 准备自变量与因变量数据
        req = output + ' ~ '
        for i in range(len(input_labels)):
            req = req + input_labels[i]
            if i != len(input_labels)-1:
                req = req + ' + '
        y, x = dmatrices(req, data=result, return_type='dataframe')

        # 拟合模型
        mod = sm.OLS(y, x)
        res = mod.fit()

        # 计算SRC
        conf = res.conf_int()
        conf = conf.drop(['Intercept'])
        params = res.params.drop(['Intercept'])
        y_std = std[output]
        s = pd.concat([conf, params], axis=1)
        s.columns = [0, 1, 2]  # 0是95%CI下界，1是95%CI上界，2是SRC数值
        s = s.mul(x_std.T)
        s = s.apply(lambda x: x / y_std)
        yield s
        del mod
    del result, x_std


def get_abs(lower, upper):
    new_lower = []
    new_upper = []
    for i in range(len(lower)):
        if lower[i] * upper[i] > 0:
            new_upper.append(max(abs(lower[i]), abs(upper[i])))
            new_lower.append(min(abs(lower[i]), abs(upper[i])))
        else:
            new_upper.append(max(abs(lower[i]), abs(upper[i])))
            new_lower.append(0)
    return new_lower, new_upper


def src_bar3(input_output_file_path):
    # Layout Configuration

    x = np.arange(len(input_labels))  # the label locations
    grid_dict = {
        'bottom': 0.32,
        'left': 0.075,
        'right': 0.98,
        'top': 0.87,
        'wspace': 0.15,
    }
    fig, ax = plt.subplots(nrows=1, ncols=3, constrained_layout=False, sharey='all', sharex='all',
                           figsize=(6.5, 2), gridspec_kw=grid_dict)

    # 数据准备
    # result的层次：
    # 1. sample num
    # 2. output
    # 3. bottom,top,src
    # 4. input
    result = []
    sample_list = [25, 50, 100, 200]
    # 对不同样本量进行循环
    for k, sample_num in enumerate(sample_list):
        temp = []
        for i, res in enumerate(regression2(input_output_file_path, sample_num=sample_num)):
            # append in the order of output_labels
            bottom = [res.loc[param, 0] for param in input_labels]
            top = [res.loc[param, 1] for param in input_labels]
            src = [res.loc[param, 2] for param in input_labels]
            temp.append([bottom, top, src])
        result.append(temp)

    # For each output
    for i, output_label in enumerate(output_labels):
        # Draw lines and fill the CI area of every input
        for j, input_label in enumerate(input_labels):
            y = [abs(result[p][i][2][j]) for p in range(len(sample_list))]
            x = [math.log(s) for s in sample_list]
            ax[i].plot(x, y, color=input_colors[j], linestyle='-', linewidth=1,
                       label=input_label, marker=input_markers[j], markersize=4,)
            lower = [result[p][i][0][j] for p in range(len(sample_list))]
            upper = [result[p][i][1][j] for p in range(len(sample_list))]
            lower, upper = get_abs(lower, upper)
            ax[i].fill_between(x=x, y1=lower, y2=upper,
                               facecolor=input_colors[j], alpha=0.2)

        # Axes Layout
        ax[i].set_title(titles[i])
        # ax[i].set_xlabel('number of samples', fontsize=7)
        ax[i].set_xlabel('样本量', fontsize=8)
        ax[i].set_xticks(x)
        ax[i].set_xticklabels(sample_list)
        ax[i].set_ylim([0, 1])
        ax[i].set_xlim([math.log(sample_list[0]), math.log(sample_list[-1])])
        if i == 0:
            fig.legend(ncol=7, mode="expand", loc='lower center')
            # ax[i].set_ylabel('Absolute value of SRC', fontsize=8)
            ax[i].set_ylabel('SRC绝对值', fontsize=8)

    # plt.show()
    plt.savefig('results/fig_3_19_SRC.png', dpi=200)


if __name__ == '__main__':
    set_plt()
    src_bar3('random_sampling_data/input+result.csv')
    print('hello world')
