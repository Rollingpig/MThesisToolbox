import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import Common


def _draw_sub(ax, x, y, X, Y, xlabel, ylabel, color, color2, title=None, yname=None):
    model = LinearRegression()
    model = model.fit(X, Y)
    r2 = model.score(X, Y)
    ax.annotate(r'$R^2$' + '=' + ("%.2f" % r2), (1, -12), xycoords='axes points', fontsize=10)
    # ax[i // 4][i % 4].tick_params(labelsize=8)
    ax.scatter(x, y, s=0.5, c=color, marker='.')
    ax.scatter(X, Y, s=0.5, c=color2, marker='.')
    # ax.set_xlabel(xlabel)
    ax.set_yticks([])
    ax.set_xticks([])
    if title:
        ax.set_title(title)
    if yname:
        ax.set_ylabel(ylabel)
    x2 = [min(X), max(X)]
    y2 = model.predict(x2)
    ax.plot(x2, y2, color=color2, linestyle='-')


def draw(input_raw_result_file='../stochastic_test_data/random_sampling_data/input+raw_result.csv', input_result_file='../stochastic_test_data/random_sampling_data/input+processed.csv'):
    Common.set_plt_en()
    raw = pd.read_csv(input_raw_result_file)
    avg = pd.read_csv(input_result_file)
    y = ['MDB', 'ATR', 'MFR']
    x = ['avg_spd', 'std_spd', 'grp_shr', 'str_cst', 'trl_shr', 'avg_int', 'ctrl_par']
    colors = [['powderblue', 'steelblue'], ['pink', 'red'], ['wheat', 'brown']]
    figure, ax = plt.subplots(len(y), len(x), constrained_layout=True, figsize=(6.5, 3))
    for j in range(len(y)):
        for i, label in enumerate(x):
            if j == 0:
                title = x[i]
            else:
                title = None
            yname = bool(i == 0)
            _draw_sub(
                ax=ax[j][i],
                x=raw[x[i]], y=raw[y[j]],
                X=avg[x[i]].apply(lambda q: [q]).tolist(),
                Y=avg[y[j]].apply(lambda q: [q]).tolist(),
                xlabel=x[i], color=colors[j][0], color2=colors[j][1], ylabel=y[j],
                title=title, yname=yname,
            )
    # plt.show()
    plt.savefig('localRelations.png', dpi=200)
    print('localRelations completed')


if __name__ == '__main__':
    draw()
