import pandas as pd
import matplotlib.pyplot as plt
from PedFlowAnalysis.basicFlow import Flow
from scipy import stats
import os
import numpy as np
import Common


def read_flow_from_arc_time(file, video_len=8, time_offset=0):
    def str_to_time(x):
        return int(x.split(':')[-2]) * 60 + float(x.split(':')[-1])

    def binning(sequence, length):
        flow = [0 for i in range(int(length * 60))]
        for person in sequence:
            position = int(person)
            flow[position] += 1
        return flow

    data = pd.read_excel(file)
    res = data['开始时间'].apply(lambda x: str_to_time(x)+time_offset)
    return Flow(binning(res.values, video_len))


def draw_line(flows, axe, bin_len=31, color=None, time_offset=0):
    s = bin_len // 2
    if color:
        for flow in flows:
            axe.plot([i+time_offset for i in range(s, len(flow))], flow[s:], color=color)
    else:
        for flow in flows:
            axe.plot([i+time_offset for i in range(s, len(flow))], flow[s:])


def cumulative_and_flow(folder, tlim):
    """分析"""
    flows = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            flows.append(read_flow_from_arc_time(path))

    fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True,
                           figsize=(6, 2), )

    length = 16
    q = np.zeros([len(flows), length * 60])
    for row, flow in enumerate(flows):
        c = flow.cumulate().values()
        draw_line([c], ax[0], bin_len=0, time_offset=0)
        # Find 50% quantile position
        mid = c[-1]//2
        k = 0
        for cc in c:
            if cc > mid:
                break
            k += 1
        # Put aligned flow into array q
        a = flow.averaging(bin=21, unit=60)
        q[row, length//2*60-k:length//2*60+len(a)-k] = np.array(a)

    q = q.transpose()
    res1 = []
    res2 = []
    res3 = []
    for x in range(-tlim, tlim):
        k = q[x + length//2*60]
        k = k[k > 0]
        mean = np.mean(k)
        std = np.std(k)
        res1.append(mean)
        ci = stats.t.interval(0.95, df=len(k)-1, loc=np.mean(k), scale=stats.sem(k))
        res2.append(ci[1])
        res3.append(ci[0])
    ax[1].plot([i for i in range(-tlim, tlim)], res1)
    ax[1].fill_between(x=np.arange(-tlim, tlim), y1=res2, y2=res3, alpha=0.4)

    ax[0].set_xlabel('时间 (秒)')
    ax[0].set_ylabel('累计到达人数 (人)')
    ax[0].set_xlim([0, 300])
    ax[0].set_ylim([0, 250])
    ax[1].set_xlim([-tlim, tlim])
    ax[1].set_ylim([0, max(res2)+10])
    ax[1].set_xlabel('半数旅客到达后时刻 (秒)')
    ax[1].set_ylabel('20秒平均流量 (人/分钟)')
    plt.savefig('Results/'+folder+'.png', dpi=200)


if __name__ == '__main__':
    Common.set_plt()
    cumulative_and_flow(folder='MTREscalator', tlim=30)
    cumulative_and_flow(folder='TrainEscalator', tlim=110)
