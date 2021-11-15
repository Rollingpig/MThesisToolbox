import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Common import set_plt


def _cor_map(ax, file):
    res = pd.read_csv(file)
    result = res[['MDB', 'ATR', 'MET', 'MFR']]
    result_cor = result.corr(method='pearson')
    result_cor = result_cor.apply(lambda x: abs(x))
    # result_cor.to_csv('cor.csv')
    # sns.heatmap(stochastic_test_data=result_cor, cmap='RdBu')
    sns.heatmap(data=result_cor, cmap='Blues_r', ax=ax, annot=True, vmin=0, vmax=1)


def _stochastic(ax, file):
    # measures = ["SR", "MT", "MF", "MD", "CA"]
    measures = ["MET", "MFR", "MDB", "ATR", "MRD"]
    res = pd.read_csv(file)
    result = res[measures]
    val = {}
    rep = 30
    sample_num = 1000
    for measure in measures:
        val[measure] = [0 for i in range(rep)]
    val_df = pd.DataFrame(val)
    for i in range(sample_num):
        result = result.sample(frac=1)
        for j in range(2, rep):
            pre_avg = result.iloc[0: j - 1, :].mean()
            cur_avg = result.iloc[0: j, :].mean()
            add = abs(pre_avg - cur_avg) / cur_avg
            val_df.iloc[j, :] += add
    val_df = val_df.apply(lambda x: (x/sample_num * 100))
    val_df.plot(kind='line', ax=ax, colormap='viridis')
    sx = [i for i in range(rep)]
    sy = [0.5 for i in range(rep)]
    ax.plot(sx, sy, label='0.5%', color='gray', linestyle='--')
    ax.set_xlim([2, rep-1])
    ax.set_ylim([0, 2])
    ax.set_xlabel('number of runs')
    ax.set_ylabel(r'$TET_{conv}$' + ' (%)')
    # val_df.to_csv('sto.stochastic_test_data')


def draw(stofile='stochastic_test_data/sto_result.csv', res_file='random_sampling_data/processed.csv'):
    figure, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True, figsize=(6.5, 2.5))
    _stochastic(ax=ax[0], file=stofile)
    _cor_map(ax=ax[1], file=res_file)

    plt.savefig('results/stochastic+pearson.png', dpi=200)
    print('stochastic+pearson completed')


if __name__ == '__main__':
    set_plt()
    draw()
    print('hello world')
