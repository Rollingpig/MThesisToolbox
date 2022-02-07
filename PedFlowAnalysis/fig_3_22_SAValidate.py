import pandas as pd
import matplotlib.pyplot as plt
import Common
from PedFlowAnalysis.basicFlow import Flow

no_data_range = 20
offset1 = 29 + 26/29


def str_to_time(x):
    return int(x.split(':')[-2]) * 60 + float(x.split(':')[-1])


def binning(sequence, length):
    flow = [0 for i in range(int(length * 60))]
    for person in sequence:
        position = int(person)
        flow[position] += 1
    return flow


def read_simulation(file):
    data = pd.read_csv(file)['flow']
    return Flow(data.values)


def read_arctime(file, offset=0.001):
    data = pd.read_excel(file)['开始时间']
    res = data.apply(lambda x: str_to_time(x) + offset)
    return Flow(binning(res.values, 7))


def draw_line(flows, axe, bin=41, color=None):
    if color:
        for flow in flows:
            axe.plot([i for i in range(no_data_range+bin, len(flow))], flow[no_data_range+bin:], color=color)
    else:
        for flow in flows:
            axe.plot([i for i in range(no_data_range+bin, len(flow))], flow[no_data_range+bin:])


def draw_validation_img():
    fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True, figsize=(6.5, 2))
    colors = ['tomato', 'wheat']
    # colors = ['black', 'lightgrey']

    # 绘制左图的模拟数据
    simulation_file = ['Data/SA_simulation/Test0-' + str(i) + '_flow.csv' for i in range(30)]
    simulation_flows = [read_simulation(simulation_file[i]).averaging() for i in range(30)]
    draw_line(simulation_flows, ax[0], color=colors[1])

    # 绘制左图的观测数据
    stair_flow = read_arctime('Data/SA_Validation/stairs.xls')
    escalator_flow = read_arctime('Data/SA_Validation/escalators.xls')
    stair_flow_plus = read_arctime('Data/SA_Validation/stairs_add.xls', offset1)
    stair_flow = stair_flow + stair_flow_plus
    total_flow = stair_flow + escalator_flow
    draw_line([total_flow.averaging()], ax[0], color=colors[0])

    # 绘制左图的XY轴与标题
    ax[0].set_title('Flow Rate')
    #ax[0].set_title('扶梯截面流量')
    ax[0].set_xlabel('Time(s)')
    #ax[0].set_xlabel('时间(秒)')
    ax[0].set_ylabel('Flow Rate (ppl/s)')
    #ax[0].set_ylabel('流量 (人/秒)')
    print(sum([max(flow) for flow in simulation_flows]) / 30, max(total_flow.averaging()))

    cumulated_sim_data = [read_simulation(simulation_file[i]).cumulate() for i in range(30)]
    draw_line([Flow(cumulated_sim_data, multi_input=True) / 30], ax[1], color=colors[1])
    draw_line([total_flow.cumulate().values()], ax[1], color=colors[0])
    ax[1].set_title('Cumulative Population')
    ax[1].set_xlabel('Time(s)')
    ax[1].set_ylabel('Passenger Num')
    #ax[1].set_title('累计旅客数量')
    #ax[1].set_xlabel('时间(秒)')
    #ax[1].set_ylabel('旅客数量(人)')

    # plt.savefig('Results/validation.svg', dpi=200)
    plt.savefig('Results/validation.png', dpi=200)


if __name__ == '__main__':
    Common.set_plt_en()
    draw_validation_img()
