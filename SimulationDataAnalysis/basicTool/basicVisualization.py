import pandas as pd
import seaborn as sns


def violin(axe, data: pd.DataFrame, title="", x_label=None, field="Duration"):

    le = len(data["index"].value_counts())
    axe.grid(linestyle="--")
    p = sns.light_palette("skyblue", reverse=True, n_colors=4)
    ax = sns.violinplot(x='index', y=field, data=data, ax=axe, linewidth=1.5, palette=p, saturation=1, cutoff=0)
    # ax = sns.boxplot(x='index', y=field, data=data, ax=axe, linewidth=1, palette=p,)
    try:
        ax.collections[0].set_linewidth(0)
        ax.collections[2].set_linewidth(0)
        ax.collections[4].set_linewidth(0)
    except IndexError:
        pass
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title(title)
    ax.set_xticklabels(x_label[:le])


def point_plot(axe, data: pd.DataFrame, title="", x='security', y="Duration", hue='编组大小'):
    axe.grid(linestyle="--")
    p = sns.color_palette("Paired")
    ax = sns.pointplot(x=x, y=y, hue=hue, data=data, ax=axe, linewidth=1, palette=p,
                       saturation=1, ci=95, markers=[".", "x", ".", "x"], dodge=True, )

    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.set_title(title)
