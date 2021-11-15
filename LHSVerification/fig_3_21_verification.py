import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Common import set_plt

output_labels = ['MDB', 'ATR', 'MFR']
colors = ['steelblue', 'red', 'darkorange', ]
light_colors = ['powderblue', 'pink', 'wheat', ]
titles = ['瓶颈最大密度(MDB)', '平均时间冗余比(ATR)', '最大流量(MFR)']


def draw(filepath):
    # Layout Configuration

    fig, ax = plt.subplots(nrows=len(filepath), ncols=len(output_labels), constrained_layout=True,
                           sharey='row', sharex='col', figsize=(6, 3.5))

    for j, file in enumerate(filepath):
        # Read Data
        result = pd.read_csv(file)
        result['MFR'] = result['MFR'].apply(lambda x: x/41)

        # Visualization
        for i, output_label in enumerate(output_labels):
            # Draw PDFs
            result[output_label].hist(bins=10, ax=ax[j][i], color=light_colors[i], density=False)

            # Draw CDFs
            bin_num = 20
            hist, bin_edges = np.histogram(result[output_label], bins=bin_num)
            x = [(bin_edges[k + 1] + bin_edges[k]) / 2 for k in range(bin_num)]
            x.insert(0, min(result[output_label]))
            cdf = np.cumsum(hist)
            cdf = cdf / 200 * 50
            cdf = np.insert(cdf, 0, 0)
            ax[j][i].plot(x, cdf, color=colors[i])

            # Layout
            ax[j][i].grid(False)
            if j == 0:
                ax[j][i].set_title(titles[i])
            if (i == 0) and (j == 0):
                # ax[j][i].set_ylabel('Unfixed')
                ax[j][i].set_ylabel('无固定参数')
            if (i == 0) and (j == 1):
                # ax[j][i].set_ylabel('Fixed 1')
                ax[j][i].set_ylabel('固定非敏感参数')
            if (i == 0) and (j == 2):
                # ax[j][i].set_ylabel('Fixed 2')
                ax[j][i].set_ylabel('固定敏感参数')
            ax[j][i].set_ylim([0, 50])

    plt.savefig('fig_3_21_verification.png', dpi=200)


if __name__ == '__main__':
    set_plt()
    draw(['stochastic_test_data/verification_data/processed unfixed.csv',
          'stochastic_test_data/verification_data/processed fix insensitive.csv',
          'stochastic_test_data/verification_data/processed fix sensitive.csv'])
