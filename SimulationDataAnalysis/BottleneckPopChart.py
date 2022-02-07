import matplotlib.pyplot as plt
import Common
from SimulationDataAnalysis.basicTool.FlowDataReader import FlowDataReader


def draw_single_band(filepath, field, simulation_period, color, axe, bin_size=30,
                     sample_offset=2.0, label=""):
    """绘制以时间为横轴的概率条带"""
    # 读取数据并将数据打断成许多组
    f = FlowDataReader()
    r_mean, upper, lower, x = f.read_split_and_process(filepath, field, simulation_period, sample_offset, bin_size)

    nx = [x[i // 2] - bin_size/2 + bin_size * (i % 2) for i in range(len(x)*2)]
    ny = [r_mean[i // 2] for i in range(len(x)*2)]
    axe.plot(nx, ny, color=color, linestyle='-', linewidth=1.2,
             label=label, )

    for i, tx in enumerate(x):
        axe.fill_between(x=[tx-bin_size/2, tx+bin_size/2], y1=[lower[i], lower[i]], y2=[upper[i], upper[i]],
                         facecolor=color, alpha=0.4)
    axe.grid(linestyle='--', linewidth=0.5)
    axe.set_xlim([int(sample_offset * 60), int((sample_offset+simulation_period) * 60)])


def bottleneck_population(field='gate-front', ylabel='出站闸机口聚集人数', ylim=(0, 400), offset_short=1.0, offset_long=1.0):
    fig, ax = plt.subplots(nrows=2, ncols=2, constrained_layout=True, sharey='all', sharex='col',
                           figsize=(6, 4), )
    size = 10
    colors = ['red', 'orange', 'green']
    period_short = 7
    period_long = 10

    ymin, ymax = ylim
    ax[0][0].set_ylim([ymin, ymax])

    row = 0
    ax[row][0].set_title('城际列车 2035年')
    ax[row][1].set_title('非城际列车 2035年')
    ax[row][0].set_ylabel(ylabel)
    draw_single_band('pop edge shrt 2035 scr.csv', field, period_short, colors[0], ax[row][0], size, offset_short)
    draw_single_band('pop edge shrt 2035 noscr.csv', field, period_short, colors[1], ax[row][0], size, offset_short)
    draw_single_band('pop edge shrt 2035 face.csv', field, period_short, colors[2], ax[row][0], size, offset_short)
    draw_single_band('pop edge lng 2035 scr.csv', field, period_long, colors[0], ax[row][1], size, offset_long)
    draw_single_band('pop edge lng 2035 noscr.csv', field, period_long, colors[1], ax[row][1], size, offset_long)
    draw_single_band('pop edge lng 2035 face.csv', field, period_long, colors[2], ax[row][1], size, offset_long)

    row = 1
    draw_single_band('pop edge shrt 2045 scr.csv', field, period_short, colors[0], ax[row][0], size, offset_short, '传统安检')
    draw_single_band('pop edge shrt 2045 noscr.csv', field, period_short, colors[1], ax[row][0], size, offset_short, '安检互认')
    draw_single_band('pop edge shrt 2045 face.csv', field, period_short, colors[2], ax[row][0], size, offset_short, '人脸识别')
    draw_single_band('pop edge lng 2045 scr.csv', field, period_long, colors[0], ax[row][1], size, offset_long, '传统安检')
    draw_single_band('pop edge lng 2045 noscr.csv', field, period_long, colors[1], ax[row][1], size, offset_long, '安检互认')
    draw_single_band('pop edge lng 2045 face.csv', field, period_long, colors[2], ax[row][1], size, offset_long, '人脸识别')
    ax[row][1].legend()
    ax[row][0].set_title('城际列车 2045年')
    ax[row][1].set_title('非城际列车 2045年')
    ax[row][0].set_ylabel(ylabel)
    ax[row][0].set_xlabel("列车到达时间（秒）")
    ax[row][1].set_xlabel("列车到达时间（秒）")

    plt.savefig('results/pop-'+field+'.svg', dpi=300)


def bottleneck_population_one_row(field='gate-front', ylabel='出站闸机口聚集人数', ylim=(0, 400), offset_short=1.0, offset_long=1.0):
    fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True, sharey='all', sharex='col',
                           figsize=(6, 2), )
    size = 10
    colors = ['red', 'orange', 'green']
    period_short = 7
    period_long = 10

    ymin, ymax = ylim
    ax[0].set_ylim([ymin, ymax])

    draw_single_band('pop edge shrt 2045 scr.csv', field, period_short, colors[0], ax[0], size,
                     offset_short, '传统安检')
    draw_single_band('pop edge shrt 2045 noscr.csv', field, period_short, colors[1], ax[0], size,
                     offset_short, '安检互认')
    draw_single_band('pop edge shrt 2045 face.csv', field, period_short, colors[2], ax[0], size,
                     offset_short, '人脸识别')
    draw_single_band('pop edge lng 2045 scr.csv', field, period_long, colors[0], ax[1], size,
                     offset_long, '传统安检')
    draw_single_band('pop edge lng 2045 noscr.csv', field, period_long, colors[1], ax[1], size,
                     offset_long, '安检互认')
    draw_single_band('pop edge lng 2045 face.csv', field, period_long, colors[2], ax[1], size,
                     offset_long, '人脸识别')
    ax[0].set_title('城际列车')
    ax[1].set_title('非城际列车')
    ax[1].legend()
    ax[0].set_ylabel(ylabel)
    ax[0].set_xlabel("列车到达时间（秒）")
    ax[1].set_xlabel("列车到达时间（秒）")

    plt.savefig('results/pop-'+field+'.svg', dpi=300)


if __name__ == '__main__':
    Common.set_plt()
    bottleneck_population_one_row(field='gate-front', ylabel='出站闸机口聚集人数', ylim=(0, 200), offset_long=1, offset_short=1)
    bottleneck_population(field='Interchange', ylabel='换乘大厅聚集人数', ylim=(0, 300), offset_long=1.5, offset_short=1.5)
    bottleneck_population(field='mtr-platform', ylabel='地铁站台人数增量', ylim=(0, 250), offset_long=5, offset_short=5)
    bottleneck_population(field='mtr-concourse', ylabel='地铁站厅人数增量', ylim=(0, 200), offset_long=2, offset_short=2)
