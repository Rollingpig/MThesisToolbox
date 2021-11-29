from Timatable import TimetableSchedule
import random

"""
    MassMotion列车班次时刻表文件生成器
    文件直接生成至MassMotion的工作目录
"""


def long_shift_group_random(working_dir, ):
    """常速列车为主的发车"""
    tb = TimetableSchedule(working_dir)

    # 创建一个长度为32的随机站台指定列表
    schedule = [i for i in range(16)]
    random.shuffle(schedule)
    schedule2 = [i for i in range(16)]
    random.shuffle(schedule2)
    while schedule2[0] == schedule[-1]:
        random.shuffle(schedule2)
    schedule = schedule + schedule2

    # 创建随机大编组标签
    simulation_hour = 2
    shift_interval = 600
    is_long = []
    for j in range(simulation_hour):
        # 创建一小时内的随机大编组标签
        long = [i for i in range(6)]
        random.shuffle(long)
        is_long = is_long + long
    print(is_long)

    schedule = schedule[:int(simulation_hour*3600 / shift_interval)]
    for train_no, platform_id in enumerate(schedule):
        p = is_long.pop()
        if p < 2:
            tb.add_shift(platform_id, 's_CRH1A_80', train_no * shift_interval)
        else:
            tb.add_shift(platform_id, 'l_CRH380B', train_no * shift_interval)

    tb.export()


def short_shift_group_random(working_dir, ):
    """加入城际列车的发车"""
    tb = TimetableSchedule(working_dir)

    # 创建一个长度为32的随机站台指定列表
    schedule = [i for i in range(16)]
    random.shuffle(schedule)
    schedule2 = [i for i in range(16)]
    random.shuffle(schedule2)
    while schedule2[0] == schedule[-1]:
        random.shuffle(schedule2)
    schedule = schedule + schedule2

    # 创建随机大编组标签
    simulation_hour = 2
    shift_interval = 8.5 * 60
    is_long = []
    for j in range(simulation_hour):
        # 创建一小时内的随机大编组标签
        long = [i for i in range(7)]
        random.shuffle(long)
        is_long = is_long + long
    print(is_long)

    schedule = schedule[:int(simulation_hour*3600 / shift_interval)]
    for train_no, platform_id in enumerate(schedule):
        p = is_long.pop()
        if p < 2:
            tb.add_shift(platform_id, 'l_CR400BFB', train_no * shift_interval)
        else:
            tb.add_shift(platform_id, 's_CRH1A_80', train_no * shift_interval)

    tb.export()


def create_short_shift_group(working_dir, period=420):
    """
    列车班次时刻表生成器：城际列车
    全部生成CRH1A列车，边缘站台，间隔420秒
    """
    edge_platform_id = 15
    tb = TimetableSchedule(working_dir)
    for train_no in range(50):
        tb.add_shift(edge_platform_id, 's_CRH1A', train_no * period)
    tb.export()


def create_long_shift_group(working_dir, period=600):
    """
    列车班次时刻表生成器：非城际列车
    全部生成CRH2A列车，边缘站台，间隔600秒
    """
    edge_platform_id = 0
    mid_platform_id = 13
    tb = TimetableSchedule(working_dir)
    for train_no in range(50):
        tb.add_shift(edge_platform_id, 'l_CRH2A', train_no * period)
    tb.export()


if __name__ == '__main__':
    working_directory = 'E:/Master/Thesis/Simulation/current/Tables/'
    # create_short_shift_group(working_directory)
    create_long_shift_group(working_directory)
    # long_shift_group_random(working_directory)
    # short_shift_group_random(working_directory)
