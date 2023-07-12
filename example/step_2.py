#Commonly Used Packages
import os
import pandas as pd
import numpy as np
import sys
sys.path.insert(0, sys.path[0]+"/../")
from researchtoolbox.utility import preprocessing as pre
from researchtoolbox.remote_ppg import analysis as als
from researchtoolbox.visualization import chart as vis
from researchtoolbox.constant_variable import *


target_folder_path = '../result/remote_ppg/'
input_file_path = os.path.join(target_folder_path, "bpm_output","summary","result.csv")
save_path = os.path.join("../result/remote_ppg/bpm_output","summary","result_updated.csv")

group_1 = 21
group_2 = 47

df = als.PreAnalysis().process(input_file_path, save_path)  # Prepare input data frame for r-PPG analysis
# df = pd.read_csv(save_path)

df_seq0 = df[df["Seq"] == 0]
df_seq0, _ = pre.Outlier().get_outliers(df_seq0, hrv_difference_index)

v = vis.HeatPlot().single_ROI(df_seq0, hrv_variable_list, group_1, group_2)

