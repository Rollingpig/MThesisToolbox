import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import Common
import RealTimetableAnalysis.step1_readFile
import matplotlib.gridspec as gridspec


def station_compare():
    def draw_swarm(file, axe, title):
        shift = RealTimetableAnalysis.step1_readFile.read_and_get_terminal(file, title)
        shift['short_shift'] = shift['duration'].apply(lambda x: True if x < 150 else False)
        sns.swarmplot(x="short_shift", y="arrival", data=shift, ax=axe, size=2)
        axe.set_title(title)
        axe.set_xlabel(None)
        axe.set_ylabel(None)

    fig, ax = plt.subplots(nrows=2, ncols=3, constrained_layout=True, sharey='all',
                           figsize=(6, 3), )

    draw_swarm('inputs/raw_shenzhenbei_20210818_i.csv', ax[0][1], '深圳北')
    draw_swarm('inputs/raw_shenzhen_20210818_i.csv', ax[1][1], '深圳')
    # draw_swarm('inputs/raw_futian_20210818_i.csv', ax[0][2], '福田')

    draw_swarm('inputs/raw_shanghai_20210818_i.csv', ax[1][0], '上海')
    # draw_swarm('inputs/raw_shanghaisouth_20210818_i.csv', ax[1][2], '上海南')
    draw_swarm('inputs/raw_shanghaihongqiao_20210818_i.csv', ax[0][0], '上海虹桥')

    draw_swarm('inputs/raw_zhengzhou_20210818_i.csv', ax[1][2], '郑州')
    draw_swarm('inputs/raw_zhengzhoudong_20210818_i.csv', ax[0][2], '郑州东')

    plt.savefig('results/station_compare.png', dpi=120)


def ktz_are_large_and_shift_distribution_by_station():
    def capacity_vs_duration(axe):
        p = pd.read_csv('processed/cap_all.csv')
        p['duration'] /= 60
        # sns.stripplot(x="列车类型", y="duration", data=p, size=3, ax=axe)
        sns.violinplot(x="列车类型", y="duration", data=p, size=3, ax=axe,
                       cut=0, linewidth=0, scale="count")
        axe.set_title(None)
        axe.set_xlabel(None)
        axe.set_ylabel('列车运行时间（小时）')

    def duration_violin_by_station(file, axe, title):
        shift = pd.read_csv(file)
        shift['duration'] /= 60
        shift['log_dur'] = shift['duration'].apply(lambda x: math.log(x, 10))
        # sns.swarmplot(x="终到站", y="log_dur", data=shift, ax=axe, size=1)
        sns.violinplot(x="终到站", y="duration", data=shift, ax=axe,
                       cut=0, inner=None, scale="count", split=False,
                       bw=.2, linewidth=0, hue='列车类型',
                       order=['郑州', '上海南', '上海', '深圳', '上海虹桥', '郑州东', '福田', ])
        axe.set_title(title)
        axe.set_xlabel(None)
        axe.set_ylabel(None)
        axe.set_yticklabels([])

    fig = plt.figure(constrained_layout=True, figsize=(6, 2), )
    gs0 = gridspec.GridSpec(1, 4, figure=fig)

    gs1 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[0])
    ax = fig.add_subplot(gs1[0])
    capacity_vs_duration(ax)

    gs2 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[1:])
    ax2 = fig.add_subplot(gs2[0])
    duration_violin_by_station('processed/cap_all.csv', ax2, '')

    plt.savefig('results/shift_distribution_by_station.png', dpi=120)


def shift_share(axe):
    data = pd.read_csv('processed/cap_all.csv')
    order = ['上海', '上海虹桥', '上海南', '广州', '广州东',
             '广州南', '深圳', '福田', '深圳北', ]
    p = sns.color_palette("Greys_r", n_colors=2)
    sns.countplot(x='终到站', hue='列车类型', data=data, ax=axe, palette=p,
                  order=order)
    axe.set_xlabel('(a)每日终到班次数量')
    axe.set_ylabel(None)
    axe.legend(ncol=1, loc='upper right')
    # axe.tick_params(axis="x", rotation=90)


def large_trains_proportion(axe1, axe2):
    p = sns.color_palette("Greys_r", n_colors=3)
    color = ['#186CA8', '#87C7F5', '#1E89D6']
    station = "上海"
    data = pd.read_csv('processed/cap_all.csv')
    data = data[data["终到站"] == station]

    inter = data[data['duration'] < 150]
    inter1 = inter[~pd.isnull(inter['capacity'])]
    d1 = inter1.groupby("编组").count()
    inter2 = inter[pd.isnull(inter['capacity'])]
    d2 = inter2.groupby("编组").count()
    if len(d2) == 1:
        n2 = 0
    else:
        n2 = d2.loc['大编组', '车次']
    df = pd.DataFrame({"确切数据": [0, d1.loc['大编组', '车次'], d1.loc['小编组', '车次']],
                       "普速列车": [0, 0, 0],
                       "推测数据": [n2 + d2.loc['小编组', '车次'], 0, 0],
                       })
    print(df)

    df.plot(kind='barh', stacked=True, ax=axe1, color=p[:], legend=None)
    # axe1.legend(ncol=1, loc='lower right')

    non_inter = data[data['duration'] > 150]
    non_inter1 = non_inter[~pd.isnull(non_inter['capacity'])]
    d1 = non_inter1.groupby("编组").count()
    non_inter2 = non_inter[pd.isnull(non_inter['capacity'])]
    d2 = non_inter2.groupby("编组").count()
    df = pd.DataFrame({"确切数据": [0, d1.loc['大编组', '车次'], d1.loc['小编组', '车次']],
                       "普速列车": [0, d2.loc['大编组', '车次'], 0],
                       "推测数据": [d2.loc['小编组', '车次'], 0, 0, ],
                       })
    print(df)
    df.plot(kind='barh', stacked=True, ax=axe2, color=p[:], legend=None)
    axe2.tick_params(axis="y", rotation=0)

    axe1.set_ylabel(None)
    axe1.set_xlabel('(b)上海站城际列车数量')
    axe2.set_xlabel('(c)上海站非城际列车数量')
    axe2.set_ylabel(None)
    axe1.set_yticklabels(['未知', '大编组', '小编组'])
    axe2.set_yticklabels(['未知', '大编组', '小编组'])


def fig_3_6():
    fig = plt.figure(constrained_layout=True, figsize=(6, 3), )
    gs0 = gridspec.GridSpec(15, 2, figure=fig)

    gs1 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[0:7, :])
    ax = fig.add_subplot(gs1[:])
    shift_share(ax)

    gs2 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[8:15, 0:1])
    ax2 = fig.add_subplot(gs2[:])
    gs3 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[8:15, 1:2])
    ax3 = fig.add_subplot(gs3[:])
    large_trains_proportion(ax2, ax3)
    plt.savefig('results/fig3_6.svg', dpi=200)


if __name__ == '__main__':
    Common.set_plt()
    # ktz_are_large_and_shift_distribution_by_station()
    # large_trains_proportion()
    fig_3_6()
    # gdc_large_are_long_duration_or_not()
