import Common
import matplotlib.pyplot as plt
import seaborn as sns


def pie(x, axe, labels, title, startangle=0):
    p1 = ['red', 'darkorange', 'gold', 'green', 'darkturquoise', 'dodgerblue', 'purple']
    p2 = sns.light_palette("skyblue", reverse=True, n_colors=len(x))
    # p3 = sns.color_palette("RdBu", n_colors=len(x))
    p3 = sns.color_palette("Greys", n_colors=len(x))
    axe.pie(x=x, labels=labels, autopct='%1.0f%%', colors=p3[:len(x)],
            wedgeprops={'linewidth': 0.7, 'edgecolor': '#444444'},
            startangle=startangle, radius=1)
    axe.set_xlabel(title)


def fig_3_2_2():
    fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True, sharey='row',
                           figsize=(6, 3), )
    labels = ['地铁', '出租车', '社会车辆', '公交车', '长途汽车', '步行']
    pie([15, 24, 25, 18, 10, 8], ax[0], labels, '(a)2035年分担率预测')
    pie([42, 12, 9, 19, 10, 8], ax[1], labels, '(b)2045年分担率预测')

    plt.savefig('fig_3_2_2.svg', dpi=300)


if __name__ == '__main__':
    Common.set_plt()
    fig_3_2_2()
