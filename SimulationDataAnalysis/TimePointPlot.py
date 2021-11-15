import matplotlib.pyplot as plt
import pandas as pd

import Common
from SimulationDataAnalysis.basicTool.basicVisualization import point_plot
from SimulationDataAnalysis.basicTool.GroupedDataReader import GroupAveragedDataReader


def part1():
    """不同条件下出站通道旅客平均通行耗时与低水平持续时间的对比，其中数据点上的竖线代表95%置信水平下的置信区间。"""
    fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True,
                           figsize=(6, 1.8), )

    files = ['trip p3 edge shrt 2035 scr.csv',
             'trip p3 edge shrt 2035 noscr.csv',
             'trip p3 edge shrt 2035 face.csv',
             'trip p3 edge lng 2035 scr.csv',
             'trip p3 edge lng 2035 noscr.csv',
             'trip p3 edge lng 2035 face.csv',
             ]
    files2 = ['los_time/los gate edge shrt 2035 scr.csv',
              'los_time/los gate edge shrt 2035 noscr.csv',
              'los_time/los gate edge shrt 2035 face.csv',
              'los_time/los gate edge lng 2035 scr.csv',
              'los_time/los gate edge lng 2035 noscr.csv',
              'los_time/los gate edge lng 2035 face.csv',
              ]
    data = GroupAveragedDataReader().read_from_list(files, files2)
    data.to_csv('results/trip-gate.csv')

    point_plot(ax[0], data, title='出站通道通行耗时', x='安检模式', y='Duration', hue='编组大小')
    point_plot(ax[1], data, title='出站通道低水平持续时间', x='安检模式', y='LOS Duration', hue='编组大小')
    ax[0].set_ylabel('旅客平均通行耗时 (秒)')
    ax[1].set_ylabel('旅客平均低水平时间 (秒)')
    ax[0].get_legend().remove()
    ax[1].legend()

    plt.savefig('results/trip-gate.png', dpi=200)


def part2():
    """不同条件下出站通道旅客平均通行耗时与低水平持续时间的对比，其中数据点上的竖线代表95%置信水平下的置信区间。"""
    fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True,
                           figsize=(6, 2), )

    files = ['trip lobby edge shrt 2035 scr.csv',
             'trip lobby edge shrt 2035 noscr.csv',
             'trip lobby edge shrt 2035 face.csv',
             'trip lobby edge lng 2035 scr.csv',
             'trip lobby edge lng 2035 noscr.csv',
             'trip lobby edge lng 2035 face.csv',
             'trip lobby edge shrt 2045 scr.csv',
             'trip lobby edge shrt 2045 noscr.csv',
             'trip lobby edge shrt 2045 face.csv',
             'trip lobby edge lng 2045 scr.csv',
             'trip lobby edge lng 2045 noscr.csv',
             'trip lobby edge lng 2045 face.csv',
             ]
    files2 = ['los_time/los lobby edge shrt 2035 scr.csv',
              'los_time/los lobby edge shrt 2035 noscr.csv',
              'los_time/los lobby edge shrt 2035 face.csv',
              'los_time/los lobby edge lng 2035 scr.csv',
              'los_time/los lobby edge lng 2035 noscr.csv',
              'los_time/los lobby edge lng 2035 face.csv',
              'los_time/los lobby edge shrt 2045 scr.csv',
              'los_time/los lobby edge shrt 2045 noscr.csv',
              'los_time/los lobby edge shrt 2045 face.csv',
              'los_time/los lobby edge lng 2045 scr.csv',
              'los_time/los lobby edge lng 2045 noscr.csv',
              'los_time/los lobby edge lng 2045 face.csv',
              ]
    data = GroupAveragedDataReader().read_from_list(files, files2)
    data.to_csv('results/trip-lobby.csv')

    point_plot(ax[0], data, title='换乘大厅通行耗时', x='安检模式', y='Duration', hue='编组大小x公交分担')
    point_plot(ax[1], data, title='换乘大厅低水平持续时间', x='安检模式', y='LOS Duration', hue='编组大小x公交分担')
    ax[0].set_ylabel('旅客平均通行耗时 (秒)')
    ax[1].set_ylabel('旅客平均低水平时间 (秒)')
    ax[0].get_legend().remove()
    ax[1].legend()

    plt.savefig('results/trip-lobby.png', dpi=200)


def part2_pop():
    """不同条件下出站通道旅客平均通行耗时与低水平持续时间的对比，其中数据点上的竖线代表95%置信水平下的置信区间。"""
    fig, ax = plt.subplots(nrows=1, ncols=1, constrained_layout=True,
                           figsize=(4.5, 2), )

    data = pd.read_csv('processed simulation data/pop-Interchange.csv')

    point_plot(ax, data, title='换乘大厅最高聚集人数', x='安检模式', y='maxPop', hue='编组大小x公交分担')
    ax.set_ylabel('最高聚集人数')
    ax.legend(loc=(1.05, 0.2), labelspacing=1.2)

    plt.savefig('results/pop-Interchange.png', dpi=200)


def part2_composite():
    """不同条件下出站通道旅客平均通行耗时与低水平持续时间的对比，其中数据点上的竖线代表95%置信水平下的置信区间。"""
    fig, ax = plt.subplots(nrows=1, ncols=3, constrained_layout=True,
                           figsize=(10, 2), )

    data = pd.read_csv('processed simulation data/pop-Interchange.csv')
    point_plot(ax[2], data, title='换乘大厅最高聚集人数', x='安检模式', y='maxPop', hue='编组大小x公交分担')
    ax[2].set_ylabel('最高聚集人数')
    ax[2].legend(loc=(1.05, 0.2), labelspacing=1, ncol=1)

    data = pd.read_csv('processed simulation data/trip-lobby.csv')
    point_plot(ax[0], data, title='换乘大厅最高聚集人数', x='安检模式', y='Duration', hue='编组大小x公交分担')
    ax[0].set_ylabel('最高聚集人数')
    ax[0].get_legend().remove()
    point_plot(ax[1], data, title='换乘大厅最高聚集人数', x='安检模式', y='LOS Duration', hue='编组大小x公交分担')
    ax[1].set_ylabel('最高聚集人数')
    ax[1].get_legend().remove()

    plt.savefig('results/com_lobby.png', dpi=200)


if __name__ == '__main__':
    Common.set_plt()
    # part2()
    # part1()
    part2_composite()
