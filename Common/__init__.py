from matplotlib import pyplot as plt


def set_plt():
    med = 8
    # 设置子图上的标题字体
    params = {
        'font.family': 'Microsoft YaHei',
        # Youyuan, SimHei, STFangsong, FZYaoti, STXihei, STSong, simsun
        'axes.titlesize': 10,
        # 设置图例的字体
        'legend.fontsize': med,
        # 设置图像的画布
        'figure.figsize': (6.5, 3),
        # 设置标签的字体
        'axes.labelsize': 10,
        # 设置xy轴上的标尺的字体
        'xtick.labelsize': med,
        'ytick.labelsize': med,
        # 设置整个画布的标题字体
        'figure.titlesize': 10,
    }
    # 更新默认属性
    plt.rcParams.update(params)


def set_plt_en():
    large = 10
    med = 7
    # 设置子图上的标题字体
    params = {
        'axes.titlesize': large,
        # 设置图例的字体
        'legend.fontsize': med,
        # 设置图像的画布
        'figure.figsize': (6.5, 3),
        # 设置标签的字体
        'axes.labelsize': large,
        # 设置x轴上的标尺的字体
        'xtick.labelsize': med,
        # 设置整个画布的标题字体
        'ytick.labelsize': med,
        'figure.titlesize': large,
    }
    # 更新默认属性
    plt.rcParams.update(params)