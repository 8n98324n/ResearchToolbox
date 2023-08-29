import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

import sys
sys.path.insert(0, sys.path[0]+"/../")
from researchtoolbox.constant_variable import *
from researchtoolbox.ml import parameter_optimization as op
from researchtoolbox.ml import dataset as dt
from researchtoolbox.ml import cross_validation as cv
from researchtoolbox.ml import supervised_learning as svl


# 需要決定的參數
step = [11, 21]
method_list = ["rf", "svm"]
mode = "rPPG"

source_folder_path = '../resource/video/video_source/'
target_folder_path = '../result/remote_ppg/'

result = {"total_accuracy": [], "total_F1": []}

for method in method_list:
    input_file_path = os.path.join(target_folder_path, "bpm_output","summary","result_updated.csv")
    output_file_path = os.path.join(target_folder_path, "bpm_output","summary", "{}_{}_{}vs{}_results.csv".format(mode, method, step[0], step[1]))
    save_path_bar = os.path.join(target_folder_path, "bpm_output","summary", "SHAP_plot_{}_{}_{}vs{}_results.png".format(mode, method, step[0], step[1]))
    save_path_dot = os.path.join(target_folder_path, "bpm_output","summary", "SHAP_{}_{}_{}vs{}_results.png".format(mode, method, step[0], step[1]))

    param_dict = {
        "input_file_path": input_file_path,
        "output_file_path": output_file_path,
        "save_path_bar": save_path_bar,
        "save_path_dot": save_path_dot,
        "model": method,
        "features": hrv_variable_list,
        # "add_principal_component_analysis": False,
        # "n_principal_component_list": [int(x) for x in np.linspace(3, 15, num=13)],
        "parameter_grid_search": False,
        "select_important_feature": False,
        "n_parameter_grid_search_iteration": 100,
        "repeat_times": 1,
        "parameter_search_fold": 5,
        "n_fold": 10,
    }

    x_read, y_read, remember_no = dt.Dataset().read_dataset(param_dict["features"], input_file_path, step=step)
    model_random = op.AutoOptimize().model_preparation(method)
    scaler = StandardScaler()
    # transform data
    x_read_scaled = scaler.fit_transform(x_read)
    x_read_scaled = pd.DataFrame(data=x_read_scaled)


    cross_validation_settings = cv.cross_validation_setting_model(n_fold = 10,
                                                                  repeat_times = 1,
                                                                  add_principal_component_analysis = False,  # 为false表示不做主成分分析
                                                                  principal_component_ratio = 0.85)  # 根据 累计解释方差比率 决定主成分个数，此处阈值设定为0.85

    data_model_settings = svl.supervised_learning_data_model(x = x_read_scaled,
                                                             Y = y_read,
                                                             remember_no = remember_no)

    acc, f1 = cv.cross_validation(param_dict).do_cross_validation(cross_validation_settings, data_model_settings, model_random)

    result["total_accuracy"].append(acc)
    result["total_F1"].append(f1)

