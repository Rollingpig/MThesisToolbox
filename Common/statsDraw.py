import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statsmodels.stats.api as sms


font_size = 6
spacing = font_size + 2


def normality(r1: pd.Series, r2: pd.Series, axe: plt.Axes, annotate_position=(2, 85), space=0):
    ann_x, ann_y = annotate_position
    space += 3
    r = (r1 - r1.mean())/r1.std()
    stat, pv1 = stats.kstest(r, 'norm')
    if pv1 < 0.005:
        axe.annotate('non-normal, K-S Test, p={:.3f}'.format(pv1),
                     (ann_x, ann_y), xycoords='axes points', fontsize=font_size, color='red')
    else:
        axe.annotate('normal, K-S Test, p={:.3f}'.format(pv1),
                     (ann_x, ann_y), xycoords='axes points', fontsize=font_size, color='red')

    r = (r2 - r2.mean()) / r2.std()
    stat, pv2 = stats.kstest(r, 'norm')
    if pv2 < 0.005:
        axe.annotate('non-normal, K-S Test, p={:.3f}'.format(pv2),
                     (ann_x, ann_y-1*spacing), xycoords='axes points', fontsize=font_size, color='blue')
    else:
        axe.annotate('normal, K-S Test, p={:.3f}'.format(pv2), (ann_x, ann_y-1*spacing), xycoords='axes points',
                     fontsize=font_size, color='blue')

    # if (pv2 < 0.005) or (pv1 < 0.005):
    stat, pv = stats.ks_2samp(r1, r2)
    space += 1
    axe.annotate('Two Sample K-S Test h={:.3f} p={:.4f}'.format(stat, pv),
                 (ann_x, ann_y - space*spacing), xycoords='axes points', fontsize=font_size, color='black')
    return space


def two_sample_hist(r1: pd.Series, r2: pd.Series, axe: plt.Axes, annotate_position=(2, 105)):
    ann_x, ann_y = annotate_position
    label1, label2 = '1', '2'

    # Histogram
    max_n = float(max(r1.max(), r2.max()))
    min_n = float(min(r1.min(), r2.min()))
    bin_num = 10
    bins = [min_n + (max_n - min_n)/bin_num*i for i in range(0, bin_num)]
    axe.hist(r1, alpha=0.5, color='red', bins=bins, label=label1, density=False)
    axe.hist(r2, alpha=0.5, color='blue', bins=bins, label=label2, density=False)
    axe.annotate('μ={:.2f} σ={:.2f} N={:d}'.format(np.mean(r1), np.std(r1), len(r1)),
                 (ann_x, ann_y), xycoords='axes points', fontsize=font_size, color='red')
    axe.annotate('μ={:.2f} σ={:.2f} N={:d}'.format(np.mean(r2), np.std(r2), len(r2)),
                 (ann_x, ann_y-1*spacing), xycoords='axes points', fontsize=font_size, color='blue')


def t_test(r1: pd.Series, r2: pd.Series, axe: plt.Axes, annotate_position=(2, 85)):
    ann_x, ann_y = annotate_position

    # T-Test
    stat, pv = stats.levene(r1, r2)
    ib, it = get_ci(r1, r2)
    if pv < 0.005:
        t, p = stats.ttest_ind(r1, r2, equal_var=False)
        axe.annotate('welch t={:.2f} p={:.4f}'.format(t, p),
                     (ann_x, ann_y), xycoords='axes points', fontsize=font_size)
        axe.annotate('MD={:.2f} 95%CI={:.2f},{:.2f}'.format(r1.mean()-r2.mean(), ib, it),
                     (ann_x, ann_y - 1*spacing), xycoords='axes points', fontsize=font_size)
        # axe.annotate('unequal_var', (ann_x, ann_y - 2*spacing), xycoords='axes points', fontsize=font_size)

    else:
        t, p = stats.ttest_ind(r1, r2, equal_var=True)
        axe.annotate('t={:.2f} p={:.4f}'.format(t, p),
                     (ann_x, ann_y), xycoords='axes points', fontsize=font_size)
        axe.annotate('MD={:.2f} 95%CI={:.2f},{:.2f}'.format(r1.mean()-r2.mean(), ib, it),
                     (ann_x, ann_y - 1 * spacing), xycoords='axes points', fontsize=font_size)
        # axe.annotate('equal_var', (ann_x, ann_y - 2*spacing), xycoords='axes points', fontsize=font_size)


def get_ci(r1: pd.Series, r2: pd.Series):
    cm = sms.CompareMeans(sms.DescrStatsW(r1), sms.DescrStatsW(r2))
    ib, it = cm.tconfint_diff(usevar='unequal')
    return ib, it


def two_sample_hist_all(r1: pd.Series, r2: pd.Series, axe: plt.Axes, annotate_position=(2, 95)):
    ann_x, ann_y = annotate_position
    two_sample_hist(r1, r2, axe, (ann_x, ann_y))
    n = normality(r1, r2, axe, (ann_x, ann_y - 2 * spacing))
    print(n)
    t_test(r1, r2, axe, (ann_x, ann_y - n * spacing))
