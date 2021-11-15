import pandas as pd


class TimetableSchedule:
    table = None
    work_dir = None

    alight_s = 1.54
    alight_l = 1.84
    profile_s = 'MtrPassenger'
    profile_l = 'TrainPassenger'

    capacity = {
        's_CRH380D': 513,
        's_CRH1A': 645,
        's_CRH1A_80': 516,  # 上座率80%
        'l_CRH2A': 1226,
        'l_CRH380B': 890,  # 上座率80%
        'l_CR400BFB': 1026,  # 上座率80%
        'l_CRH380D': 513,
    }

    def __init__(self, working_dir='E:/Master/Thesis/Simulation/current/Tables/'):
        self.table = []
        self.curve = []
        self.curve_key = {}
        self.work_dir = working_dir

    @staticmethod
    def __time_to_str(sec):
        minute = int(sec // 60)
        sec = int(sec % 60)
        if sec >= 10:
            return '0:0' + str(minute) + ':' + str(sec)
        else:
            return '0:0' + str(minute) + ':0' + str(sec)

    def __create_short(self, capacity, origin_no, train_type, time):
        return {'From': 'short-train' + str(origin_no), 'To': 'dpt', 'Population': capacity,
                'Time Offset ': str(time) + 's',
                'Curve': train_type, 'Avatar or Colour': 'RED', 'Profile': self.profile_s,
                'Init Action': 'from-train',
                'Give Tokens...': ''}

    def __append_short(self, capacity, origin_no, train_type, time):
        t = self.__create_short(capacity, origin_no, train_type, time)
        self.table.append(t)

    def __append_long(self, capacity, origin_no, train_type, time):
        t = self.__create_short(capacity, origin_no, train_type, time)
        t['From'] = 'long-train' + str(origin_no)
        t['Avatar or Colour'] = 'BLUE'
        t['Profile'] = self.profile_l
        self.table.append(t)

    def __add_curve(self, train_type, capacity):
        if train_type not in self.curve_key.keys():
            t = {'Curve Name': train_type,
                 'Interval Duration': self.__time_to_str(capacity * self.alight_s / 16),
                 'Values...': 1, }
            if train_type.split('_')[0] == 'l':
                t['Interval Duration'] = self.__time_to_str(capacity * self.alight_l / 16)
            self.curve.append(t)
            self.curve_key[train_type] = True

    def add_shift(self, origin_no, train_type, time):
        if train_type.split('_')[0] == 's':
            self.__append_short(self.capacity[train_type], origin_no, train_type, time)
        else:
            self.__append_long(self.capacity[train_type], origin_no, train_type, time)
        self.__add_curve(train_type, self.capacity[train_type])

    def export(self):
        t = pd.DataFrame(self.table).reindex(
            columns=['From', 'To', 'Population', 'Time Offset ', 'Curve', 'Avatar or Colour', 'Profile', 'Init Action',
                     'Give Tokens...'])
        t.to_csv(self.work_dir + 'TimetableSchedule.csv', index=False)
        c = pd.DataFrame(self.curve).reindex(
            columns=['Curve Name', 'Interval Duration', 'Values...'])
        c.to_csv(self.work_dir + 'TimetableCurve.csv', index=False)
