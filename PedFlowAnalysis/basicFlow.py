class Flow:
    flow = None
    # no_data_range = 20
    no_data_range = 0

    def __init__(self, data=None, multi_input=False):
        if not multi_input:
            self.flow = data
        else:
            total = [0 for i in range(len(data[0].flow))]
            for i in range(len(data[0].flow)):
                total[i] = sum([flow.flow[i] for flow in data])
            self.flow = total

    def averaging(self, bin=41, unit=1):
        part = int((bin - 1) / 2)
        avg_flow = [0 for i in range(len(self.flow))]
        for i in range(int(self.no_data_range + part), int(len(self.flow) - part)):
            avg_flow[i] = sum([self.flow[j] for j in range(i - part, i + part + 1)]) / bin * unit
        return avg_flow

    def cumulate(self):
        c_flow = [0 for i in range(len(self.flow))]
        for i, _ in enumerate(self.flow):
            c_flow[i] = sum([self.flow[j] for j in range(0, i)])
        return Flow(c_flow)

    def __add__(self, other):
        total = [0 for i in range(len(self.flow))]
        for i in range(len(self.flow)):
            total[i] = self.flow[i] + other.flow[i]
        return Flow(total)

    def __truediv__(self, other):
        total = [0 for i in range(len(self.flow))]
        for i in range(len(self.flow)):
            total[i] = self.flow[i] / other
        return total

    def values(self):
        return self.flow

    def get_flow_rate(self):
        return sum(self.flow) / (len(self.flow) - self.no_data_range)
