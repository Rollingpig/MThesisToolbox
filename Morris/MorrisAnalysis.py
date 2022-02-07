import SALib.sample.morris
import SALib.analyze.morris
import SALib.plotting.morris
import matplotlib.pyplot as plt
import pandas as pd

from Common import set_plt_en as set_plt


# Public vars
output_labels = ['MDB', 'ATR', 'MFR']
colors = ['steelblue', 'red', 'darkorange', ]
annotated = ['str_cst', 'avg_int', 'trl_shr', 'grp_shr', 'avg_spd']
input_colors = ['red', 'darkorange', 'gold', 'green', 'darkturquoise', 'dodgerblue', 'purple']
input_markers = ['o', 'x', '^', 's', '+', 'H', '.']
# titles = ['瓶颈最大密度(MDB)', '平均时间冗余比(ATR)', '最大流量(MFR)']
titles = ['Max Density at Bottleneck', 'Averaged Time Ratio', 'Max Flow Rate']

def analysis(problem):

    fig, ax = plt.subplots(nrows=1, ncols=3, constrained_layout=True, figsize=(6, 1.8))

    # Read Data
    partial = 400
    input = pd.read_csv('Morris 11-22/input.csv', dtype=float).iloc[:partial, ].values
    result = pd.read_csv('Morris 11-22/result.csv', dtype=float).iloc[:partial, ]

    for k, output_label in enumerate(output_labels):
        # Perform analysis
        output = result.loc[:, output_label].values
        Si = SALib.analyze.morris.analyze(problem, X=input, Y=output, print_to_console=False, conf_level=0.95)

        # Print stochastic_test_data file
        f = pd.DataFrame(Si)
        f.to_csv(output_label + '_morris.csv')

        # Plotting
        ax[k].scatter(x=Si['sigma'], y=Si['mu_star'], s=8, marker='o', color=colors[k])
        for i, txt in enumerate(problem['names']):
            if txt in annotated:
                ax[k].annotate(txt, (Si['sigma'][i], Si['mu_star'][i]), ha='right', va='top', fontsize=8)
        if k == 0:
            ax[k].set_ylabel('μ*')
        ax[k].set_xlabel('σ')
        ax[k].set_title(titles[k])
        # ax[k].grid(True)

    plt.savefig('morris.png', dpi=200)
    # plt.savefig('morris.svg')


if __name__ == '__main__':
    # Layout Config
    set_plt()
    # Define the model inputs
    problem = {
        'num_vars': 7,
        'names': ['avg_spd', 'std_spd', 'trl_shr', 'avg_int', 'grp_shr', 'str_cst', 'ctrl_par'],
        'bounds': [[1.25, 1.4], [0.15, 0.3], [0.4, 0.7], [1.3, 2.2], [0, 0.65], [10, 40], [0, 1]]
    }
    analysis(problem,)
