import pandas as pd

from SimulationDataAnalysis.basicTool.statsCompare import two_group_compare


def export_compare_table(input_file, output_file, field):
    shifts = ['城际列车', '非城际列车']
    years = ['2035年', '2045年']
    securities = ['传统安检', '安检互认', '人脸识别+安检互认']

    data = pd.read_csv(input_file, index_col=0)

    res = []
    for shift1 in shifts:
        for year1 in years:
            for security1 in securities:
                label1 = shift1 + year1 + security1
                data1 = data[(data['编组大小'] == shift1) &
                             (data['公交分担'] == year1) &
                             (data['安检模式'] == security1)]
                res0 = {'r1': label1, }
                if len(data1) > 0:
                    for shift2 in shifts:
                        for year2 in years:
                            for security2 in securities:
                                label2 = shift2 + year2 + security2
                                if label2 != label1:
                                    data2 = data[(data['编组大小'] == shift2) &
                                                 (data['公交分担'] == year2) &
                                                 (data['安检模式'] == security2)]
                                    if len(data2) > 0:
                                        res0.update({label2: two_group_compare(data1[field], data2[field])})
                                    else:
                                        res0.update({label2: ''})
                                else:
                                    res0.update({label2: ''})
                res.append(res0)

    pd.DataFrame(res).to_csv(output_file, encoding='gbk')


if __name__ == '__main__':
    # export_compare_table('/results/trip-lobby.csv', 'results/md-trip-time-lobby.csv', field='Duration')
    # export_compare_table('/results/trip-lobby.csv', 'results/md-los-lobby.csv', field='LOS Duration')
    # export_compare_table('results/trip-gate.csv', 'results/md-trip-time-gate.csv', field='Duration')
    # export_compare_table('results/trip-gate.csv', 'results/md-los-gate.csv', field='LOS Duration')
    export_compare_table('processed simulation data/pop-Interchange.csv', 'results/md-pop-interchange.csv', field='maxPop')
