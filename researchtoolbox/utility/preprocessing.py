        
import numpy as np
import os
import pandas as pd

"""
This module contains classes and methods for transforming a BVP signal in a BPM signal.
"""

class Outlier:
    """
    Manage (multi-channel, row-wise) BVP signals, and transforms them in BPMs.
    """
    def __init__(self):
        pass

    def get_outliers(self, df, column_list, k=1.5):  # 剔除异常值（1.5(Q3-Q1)）
        outlier_index_list = []
        for column in column_list:
            mins = df[column] < df.describe()[column]['25%']-k*(df.describe()[column]['75%']-df.describe()[column]['25%'])
            maxs = df[column] > df.describe()[column]['75%']+k*(df.describe()[column]['75%']-df.describe()[column]['25%'])
            mask = mins | maxs
            # print(df.loc[mask, column])
            df.loc[mask, column] = np.nan
            outlier_index_list += df.loc[mask, column].index.tolist()
        return df, list(set(outlier_index_list))
