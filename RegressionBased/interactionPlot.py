import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.linear_model import LinearRegression


def evaluate_model(X1, X2, X3, X4, X5):
    # 5 * X1 + 4 * X2 * X1 * X3 - 2 * X1 * X2 + random.random()*2
    return X1 * X2 * X4 + 2*X1+2*X3 - X3 * X2 * X4 + random.random()*1


def sc(x, y, c, avg, ax):
    ax.scatter(avg[x], avg[y], s=10, c=avg[c], marker='o', cmap='bwr')
    title = 'x='+x+' y='+y+' color='+c
    ax.set_title(title)


def interactions(avg_file='../stochastic_test_data/inputs+results.csv'):
    p = [['str_cst', 'ATR', 'grp_shr'], ['grp_shr', 'ATR', 'str_cst'], ['str_cst', 'MFR', 'trl_shr'],
         ['str_cst', 'MDB', 'grp_shr'], ['avg_spd', 'MDB', 'grp_shr'], ['avg_int', 'MDB', 'grp_shr'], ]
    avg = pd.read_csv(avg_file)
    fig, ax = plt.subplots(2, 3, constrained_layout=True, figsize=(6.5, 4),)
    for i in range(len(p)):
        sc(p[i][0], p[i][1], p[i][2], avg, ax[i // 3][i % 3])
    plt.savefig('results/interactionPlot.png', dpi=120)
    # plt.show()


def test():
    # Generate samples
    size = 2000
    X1 = pd.Series(np.random.randint(0, 100, size=size) / 100)
    X2 = pd.Series(np.random.randint(0, 100, size=size) / 100)
    X3 = pd.Series(np.random.randint(0, 100, size=size) / 100)
    X4 = pd.Series(np.random.randint(0, 100, size=size) / 100)
    X5 = pd.Series(np.random.randint(0, 100, size=size) / 100)
    # Run model
    # If the model is written in Python, then generally
    # you will loop over each sample input and evaluate the model
    Y = np.zeros([size])
    X = []
    sx = []
    sy = []
    for i in range(size):
        Y[i] = evaluate_model(X1[i], X2[i], X3[i], X4[i], X5[i])
        X.append([X1[i], X2[i], X3[i], X4[i], X5[i]])
        sx.append([float(X2[i])])
        sy.append([float(Y[i])])
    model = LinearRegression()
    model.fit(X, Y)
    print(model.coef_, model.score(X,Y))
    p1 = [[0,2,0]]
    p2 = [[0,1,0]]
    # print(model.predict(p2)-model.predict(p1))
    fig, ax = plt.subplots(2, 2, constrained_layout=True, figsize=(6.5, 5), )
    ss = 7
    ax[0][0].scatter(X1, Y, s=ss, c=X2, marker='o', cmap='RdBu')
    ax[0][1].scatter(X3, Y, s=ss, c=X2, marker='o', cmap='RdBu')
    ax[1][0].scatter(X2, Y, s=ss, c=X2, marker='o', cmap='RdBu')

    model2 = LinearRegression()
    model2 = model2.fit(sx, sy)
    x2 = [[0], [1]]
    y2 = model2.predict(x2)
    print(model2.score(sx, sy))
    ax[1][0].plot(x2, y2, color='black', linestyle='-')
    plt.show()


if __name__ == '__main__':
    # interactions()
    test()

