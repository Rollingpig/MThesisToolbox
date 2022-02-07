import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.gridspec as gridspec

import Common
from SimulationDataAnalysis.basicTool.basicVisualization import point_plot
from SimulationDataAnalysis.basicTool.GroupedDataReader import GroupAveragedDataReader

base_files = ['edge shrt 2035 scr.csv', 'edge shrt 2035 noscr.csv',
              'edge shrt 2035 face.csv', 'edge lng 2035 scr.csv',
              'edge lng 2035 noscr.csv', 'edge lng 2035 face.csv',
              'edge shrt 2045 scr.csv', 'edge shrt 2045 noscr.csv',
              'edge shrt 2045 face.csv', 'edge lng 2045 scr.csv',
              'edge lng 2045 noscr.csv', 'edge lng 2045 face.csv',
              ]
base_files_0 = ['edge shrt 2035 scr.csv', 'edge shrt 2035 noscr.csv',
                'edge shrt 2035 face.csv', 'edge lng 2035 scr.csv',
                'edge lng 2035 noscr.csv', 'edge lng 2035 face.csv',
                ]


def gate_trip_and_los():
    """不同条件下出站通道旅客平均通行耗时与低水平持续时间的对比，其中数据点上的竖线代表95%置信水平下的置信区间。"""
    fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True,
                           figsize=(6, 1.8), )

    files = ['trip time/trip gate ' + file for file in base_files_0]
    files2 = ['los_time/los gate ' + file for file in base_files_0]

    data = GroupAveragedDataReader().read_from_list(files, files2)
    data.to_csv('processed data/trip-gate.csv')

    point_plot(ax[0], data, title='出站通道旅客平均通行耗时', x='安检模式', y='Duration', hue='编组大小')
    point_plot(ax[1], data, title='出站通道旅客平均低水平持续时间', x='安检模式', y='LOS Duration', hue='编组大小')
    ax[0].set_ylabel('时间 (秒)')
    ax[1].set_ylabel('时间 (秒)')
    ax[0].get_legend().remove()
    ax[1].legend()

    plt.savefig('results/trip-gate.svg')


def section_trip_and_los(place='platform', text='地铁站台'):
    """
    不同条件下节点空间旅客平均通行耗时与低水平持续时间的对比，其中数据点上的竖线代表95%置信水平下的置信区间。
    :param place: lobby, concourse, platform
    :param text:
    :return:
    """
    fig = plt.figure(constrained_layout=True, figsize=(6, 2.2), )
    gs0 = gridspec.GridSpec(15, 2, figure=fig)
    gs1 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[:13, 0])
    ax = [fig.add_subplot(gs1[:])]
    gs2 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[:13, 1])
    ax.append(fig.add_subplot(gs2[:]))

    files = ['trip time/trip ' + place + ' ' + file for file in base_files]
    files2 = ['los_time/los ' + place + ' ' + file for file in base_files]

    data = GroupAveragedDataReader().read_from_list(files, files2)
    data.to_csv('processed data/trip-' + place + '.csv')

    point_plot(ax[0], data, title=text + '旅客平均通行耗时', x='安检模式', y='Duration', hue='编组大小x公交分担')
    fig.legend(ncol=4, mode="expand", loc='lower center')
    point_plot(ax[1], data, title=text + '旅客平均低水平持续时间', x='安检模式', y='LOS Duration', hue='编组大小x公交分担')
    ax[0].set_ylabel('时间 (秒)')
    ax[1].set_ylabel('时间 (秒)')
    ax[0].get_legend().remove()
    ax[1].get_legend().remove()

    plt.savefig('results/trip-' + place + '.svg')


def lobby_pop():
    """不同条件下换乘大厅旅客最高聚集人数的对比，其中数据点上的竖线代表95%置信水平下的置信区间。"""
    fig, ax = plt.subplots(nrows=1, ncols=1, constrained_layout=True,
                           figsize=(4.5, 2), )

    data = pd.read_csv('processed data/pop-Interchange.csv')

    point_plot(ax, data, title='换乘大厅最高聚集人数', x='安检模式', y='maxPop', hue='编组大小x公交分担')
    ax.set_ylabel('最高聚集人数')
    ax.legend(loc=(1.05, 0.2), labelspacing=1.2)

    plt.savefig('results/pop-lobby.png', dpi=200)


def lobby_composite(data, data2, save_path):
    fig, ax = plt.subplots(nrows=1, ncols=3, constrained_layout=True,
                           figsize=(12, 2), )

    data['编组大小x公交分担'] = data['编组大小x公交分担'].replace('非城际列车 2045年', 'Long Shifts 2045', False)
    data['编组大小x公交分担'] = data['编组大小x公交分担'].replace('城际列车 2045年', 'Short Shifts 2045', False)
    data['编组大小x公交分担'] = data['编组大小x公交分担'].replace('非城际列车 2035年', 'Long Shifts 2035', False)
    data['编组大小x公交分担'] = data['编组大小x公交分担'].replace('城际列车 2035年', 'Short Shifts 2035', False)

    # point_plot(ax[2], data, title='换乘大厅最高聚集人数', x='安检模式', y='maxPop', hue='编组大小x公交分担')
    # ax[2].set_ylabel('最高聚集人数')
    point_plot(ax[2], data, title='Max Population', x='安检模式', y='maxPop', hue='编组大小x公交分担')
    ax[2].set_ylabel('Max Population')
    ax[2].set_xticklabels(['Traditional', 'No Additional\n Checks', 'Facial Recognition'])
    ax[2].legend(loc=(1.05, 0.2), labelspacing=1, ncol=1)

    # point_plot(ax[0], data, title='换乘大厅通行耗时', x='安检模式', y='Duration', hue='编组大小x公交分担')
    # ax[0].set_ylabel('通行耗时（秒）')
    point_plot(ax[0], data2, title='Travel Time', x='安检模式', y='Duration', hue='编组大小x公交分担')
    ax[0].set_ylabel('Time (sec)')
    ax[0].get_legend().remove()
    ax[0].set_xticklabels(['Traditional', 'No Additional\n Checks', 'Facial Recognition'])

    # point_plot(ax[1], data, title='换乘大厅低水平持续时间', x='安检模式', y='LOS Duration', hue='编组大小x公交分担')
    # ax[1].set_ylabel('低水平持续时间（秒）')
    point_plot(ax[1], data2, title='Congestion Duration', x='安检模式', y='LOS Duration', hue='编组大小x公交分担')
    ax[1].set_ylabel('Time (sec)')
    ax[1].get_legend().remove()
    ax[1].set_xticklabels(['Traditional', 'No Additional\n Checks', 'Facial Recognition'])

    plt.savefig(save_path, dpi=200)


if __name__ == '__main__':
    Common.set_plt()
    # section_trip_and_los(place='platform', text='地铁站台')
    # section_trip_and_los('lobby', '换乘大厅')
    # section_trip_and_los('concourse', '地铁站厅')
    # gate_trip_and_los()
    lobby_composite(pd.read_csv('processed data/pop-Interchange.csv'),
                    pd.read_csv('processed data/trip-lobby.csv'),
                    'results/composite_lobby.png')
    lobby_composite(pd.read_csv('processed data/pop-mtr-concourse.csv'),
                    pd.read_csv('processed data/trip-concourse.csv'),
                    'results/composite_concourse.png.png')
    lobby_composite(pd.read_csv('processed data/pop-mtr-platform.csv'),
                    pd.read_csv('processed data/trip-platform.csv'),
                    'results/composite_platform.png')
