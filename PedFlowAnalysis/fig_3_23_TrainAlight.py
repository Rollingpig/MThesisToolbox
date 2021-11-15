import pandas as pd
import Common
import matplotlib.pyplot as plt
import os
import seaborn as sns
import matplotlib.gridspec as gs


def read_alight(file):
    def str_to_time(x):
        return int(x.split(':')[-2]) * 60 + float(x.split(':')[-1])

    data = pd.read_excel(file)
    data['开始时间'] = data['开始时间'].apply(lambda x: str_to_time(x))
    data['结束时间'] = data['结束时间'].apply(lambda x: str_to_time(x))
    data['interval'] = data['结束时间'] - data['开始时间']
    data['isTrolley'] = data['字幕内容']
    return data


def pie(x, axe, labels, title, startangle=0):
    axe.pie(x=x, labels=labels, autopct='%1.1f%%', colors=['#186CA8', '#87C7F5'],
            wedgeprops={'linewidth': 0.7, 'edgecolor': '#444444'},
            startangle=startangle, radius=1)
    axe.set_xlabel(title)


def alight_analysis():
    """分析铁路下车旅客的下车间隔"""
    file_list = []
    for root, dirs, files in os.walk('Data/TrainAlight'):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        for f in files:
            path = os.path.join(root, f)
            file_list.append(read_alight(path))
    d = pd.concat(file_list, axis=0)

    fig = plt.figure(constrained_layout=True, figsize=(6, 3), )
    gs0 = gs.GridSpec(2, 7, figure=fig)

    gs1 = gs.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[:, 0:3])
    ax = fig.add_subplot(gs1[:])
    ax2 = fig.add_subplot(gs.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[0, 3: 5])[:])
    ax3 = fig.add_subplot(gs.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[0, 5: 7])[:])
    ax4 = fig.add_subplot(gs.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[1, 3: 5])[:])
    ax5 = fig.add_subplot(gs.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[1, 5: 7])[:])

    '''r1 = d[d['isTrolley'] == 0]['interval']
    r2 = d[d['isTrolley'] == 1]['interval']
    Common.statsDraw.two_sample_hist_all(r1, r2, ax, (110, 90))'''

    p = sns.color_palette("ch:s=.25,rot=-.25", as_cmap=False)
    sns.boxplot(x='isTrolley', y='interval', data=d, ax=ax,
                linewidth=1, color=[24/255, 108/255, 168/255])
    ax.set_ylabel('下车间隔（秒）')
    ax.set_xlabel(None)
    ax.set_xlabel('(a)下车速率的差异')
    ax.set_xticklabels(['未携带拉杆箱', '携带拉杆箱'])

    pie([325, 38], ax2, ['扶梯', '楼梯'], '(b)拉杆箱旅客的偏好')
    pie([817-325, 606-38], ax3, ['扶梯', '楼梯'], '(c)未携带旅客的偏好')
    # pie(x=[278, 1117-278], labels=['携带拉杆箱', '未携带'], axe=ax4, title='(d)城际列车旅客', startangle=60)
    pie(x=[204, 849 - 204], labels=['携带拉杆箱', '未携带'], axe=ax4, title='(d)城际列车旅客', startangle=60)
    # pie(x=[107, 163 - 107], labels=['携带拉杆箱', '未携带'], axe=ax5, title='(e)非城际列车旅客')
    pie(x=[266, 737 - 266], labels=['携带拉杆箱', '未携带'], axe=ax5, title='(e)非城际列车旅客')

    plt.savefig('Results/fig_3_23.png', dpi=200)


if __name__ == '__main__':
    Common.set_plt()
    alight_analysis()
