import sys
import os
import pandas as pd
import numpy as np

import sys
sys.path.insert(0, sys.path[0]+"/../")
from researchtoolbox.constant_variable import *
from researchtoolbox.ml import parameter_optimization as op
from researchtoolbox.thermal_imaging import utils

from imutils import paths
import csv


# input_mp4_path = '../result/thermal/video_output'
input_mp4_path = './test_videos'
input_csv_path = '../result/thermal/csv_output'
output__csv_path = '../result/thermal'
result_length = 120
minimum_length = 60

video_files = list(paths.list_files(input_mp4_path))
csv_files = list(paths.list_files(input_csv_path))
debug = False
summary_list = []

#point_list =[index_of_left_eyebrow_outer,index_of_right_eyebrow_outer,index_of_left_eyebrow_inner,index_of_right_eyebrow_inner,index_of_fore_head,index_of_upper_nose,index_of_middle_nose,index_of_nose_tip,index_of_left_nostril,index_of_right_nostril,index_of_left_nose,index_of_right_nose,index_of_left_cheek,index_of_right_cheek,index_of_chin,index_of_throat,index_of_left_lip,index_of_upper_lip_outer,index_of_upper_lip,index_of_right_lip,index_of_lower_iip_outer,index_of_lower_iip]

for index, input_file_fullname in enumerate(video_files, 1):

    if debug:
        index=1
        input_file_fullname = 'PS-9_001_11_2022-05-21_120837_1.mp4'
        #input_file_fullname = video_files[index]

    base_name = os.path.splitext(os.path.basename(input_file_fullname))[0]

    print(input_file_fullname)
    fps = utils.get_fps(input_file_fullname)
    print(fps)

    #Find csv
    csv_file_fullname = ""
    csv_base_name = ""
    for _, current_file_fullname in enumerate(csv_files, 1):  # index
        if base_name in current_file_fullname:
            csv_file_fullname = current_file_fullname
            csv_base_name = base_name
            break

    if not os.path.exists(csv_file_fullname):
        continue

    with open(csv_file_fullname, newline='') as f:
        reader = csv.reader(f)
        data_table = list(reader)
        
    current_time = 0
    new_output  =[]
    sequence = 0
    output_file_name = ""

    for index_table, row in enumerate(data_table):
        current_time = current_time + 30/fps
        data_table[index_table].append(current_time)
        new_output.append(data_table[index_table])
        print(fps, current_time, result_length)
        if current_time > result_length:
            summary_list = utils.file_output(output__csv_path, base_name, sequence, new_output, summary_list)
            sequence = sequence+1
            current_time = 0
            new_output = []
        else:
            pass
    
    if current_time > minimum_length: #最低長度要求
        summary_list = utils.file_output(output__csv_path, base_name,sequence,new_output, summary_list)

column_name = ["Name"]
for point_index in range(len(point_list)):
    column_name.append(str(point_list[point_index]) + "_mean" )
    column_name.append(str(point_list[point_index]) + "_median" )
    column_name.append(str(point_list[point_index]) + "_std" )

print(summary_list)
if summary_list and len(summary_list) > 0:
    output_summary_file_name = output__csv_path + "/summary.csv"
    df = pd.DataFrame(summary_list)
    df_trimmed  = df.iloc[: , :len(point_list)*3+1]
    #df = pd.DataFrame(summary_list,columns=column_name) 
    df_trimmed.columns = column_name
    df_trimmed.to_csv(output_summary_file_name)
