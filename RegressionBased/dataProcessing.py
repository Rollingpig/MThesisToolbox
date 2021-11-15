import pandas as pd
import matplotlib.pyplot as plt


def combine():
    r = pd.DataFrame()
    for i in range(1, 4):
        path = 'processed' + str(i) + '.csv'
        q = pd.read_csv(path)
        r = pd.concat([r, q], sort=True)
    r = r.sort_values(by='id')
    r.to_csv('processed.csv', index=False,)


def hist_show():
    result = pd.read_csv('processed.csv')
    res = result.iloc[:, 2]
    hist = res.hist(bins=15)
    # hist = res.hist(bins=[i for i in range(140, 170, 3)])
    plt.show()


def get_average(file='inputs+raw_results.csv'):
    raw = pd.read_csv(file)
    res = raw[['id', 'time_sur', 'main_span']].groupby('id').mean()
    res.to_csv('processed.csv')


def x_plus_y(x_file='random_inputs.csv', y_file='raw_result.csv', output_path='inputs+raw_results.csv'):
    x = pd.read_csv(x_file)
    y = pd.read_csv(y_file)
    x['id'] = [i for i in range(len(x))]
    id = []
    for i in range(len(x)):
        for j in range(len(y) // len(x)):
            id.append(i)
    y['id'] = id
    result = pd.merge(x, y, how='outer')
    result.to_csv(output_path)


if __name__ == '__main__':
    # x_plus_y(x_file='LHS_input.csv', y_file='raw_result.csv', output_path='inputs+raw_results.csv')
    # x_plus_y(x_file='LHS_input.csv', y_file='processed.csv', output_path='inputs+results.csv')
    combine()
    print('hello world')