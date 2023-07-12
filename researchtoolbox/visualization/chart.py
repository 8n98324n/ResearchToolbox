#Commonly Used Packages
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from matplotlib.colors import ListedColormap
import matplotlib as mpl
from scipy.stats import ttest_ind, ttest_rel, ttest_1samp

plt.rcParams['axes.unicode_minus'] = False    # 显示负号
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)


"""
This module contains classes and methods for transforming a BVP signal in a BPM signal.
"""

class ScatterPlot:
    """
    Manage (multi-channel, row-wise) BVP signals, and transforms them in BPMs.
    """
    def __init__(self):
        pass




class HeatPlot:

    # hrv_variable_list = ["HR", "SDNN", "rMSSD", "pNN50", "ln(HF)", "ln(LF)", "ln(LF/HF)"]

    def __int__(self):
        pass


    def single_ROI(self, df_seq0, hrv_variable_list, group1, group2):
        single_ROI_t_test = {}
        value_list = []
        color_list = []
        color_21_list = []
        color_11_list = []
        value_21_list = []
        value_11_list = []

        for i in hrv_variable_list:
            group_21 = df_seq0[df_seq0["Step"] == group1]["{}_difference".format(i)].dropna().tolist()
            group_11 = df_seq0[df_seq0["Step"] == group2]["{}_difference".format(i)].dropna().tolist()

            single_ROI_t_test["{}_difference".format(i)] = ttest_ind(group_21, group_11)
            # single_ROI_t_test["{}_difference".format(i)] = ttest_rel(group_21, group_11)  # 组内t-test
            avg_diff = np.mean(group_21) - np.mean(group_11)

            value_21_list.append(np.mean(group_21))
            value_11_list.append(np.mean(group_11))
            value_list.append(avg_diff)
            color_21_list.append(ttest_1samp(group_21, 0).pvalue)
            color_11_list.append(ttest_1samp(group_11, 0).pvalue)
            color_list.append(single_ROI_t_test["{}_difference".format(i)].pvalue)
            # color_list.append(rel_t_test_results["{}_difference".format(i)].pvalue)  # 组内t-test
            print("{}_difference\t{}\t{}".format(i, round(avg_diff, 3),
                                                 round(single_ROI_t_test["{}_difference".format(i)].pvalue, 3)))

        value_array = np.array([value_21_list, value_11_list, value_list])
        color_array = np.array([color_21_list, color_11_list, color_list])

        print()
        print(value_array)
        print(color_array)

        plt.xticks(np.arange(len(hrv_variable_list)), labels=hrv_variable_list, fontsize=12)
        plt.yticks(np.arange(3),
                   labels=[str(group1) + "_mean", str(group2) + "_mean", "{}-{} difference".format(group1, group2)],
                   fontsize=12)

        for i in range(3):
            for j in range(len(hrv_variable_list)):
                if color_array[i, j] >= 0.05:
                    color = "black"
                else:
                    color = "white"
                text = plt.text(j, i, round(value_array[i, j], 2), ha="center", va="center", color=color, fontsize=10)

        top = mpl.colormaps['YlOrRd_r']
        bottom = mpl.colormaps['YlGn_r']  # YlGn_r
        newcolors = np.vstack((top(np.linspace(0, 1, 5 * 5 * 2)[: 25]),
                               bottom(np.linspace(0, 1, 95 * 5 * 2)[95 * 5:])))
        newcmp = ListedColormap(newcolors, name="OrangeBlue")
        plt.imshow(color_array, vmin=0, vmax=1, cmap=newcmp)
        plt.tight_layout()

        plt.savefig("single_ROI.png", dpi=450)
        plt.show()


