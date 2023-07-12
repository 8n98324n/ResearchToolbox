

hrv_variable_list = ["HR", "SDNN", "rMSSD", "pNN50", "ln(HF)", "ln(LF)", "ln(LF/HF)"]
hrv_variable_index = ["{}".format(i) for i in hrv_variable_list]  # remote PPG
hrv_difference_index = ["{}_difference".format(i) for i in hrv_variable_list]

thermal_index_list = [i for i in range(61)]
thermal_selected_index_list = [18, 25, 21, 22, 58, 28, 29, 30, 32, 34, 49, 52, 53, 51, 48, 50, 55, 57, 54, 56, 59, 60]
thermal_point_difference_index = [str(ind) + "_difference" for ind in thermal_index_list]
thermal_selected_point_difference_index = [str(ind) + "_difference" for ind in thermal_selected_index_list]
thermal_point_mean_index = [str(ind) + "_mean" for ind in thermal_index_list]
thermal_selected_point_mean_index = [str(ind) + "_mean" for ind in thermal_selected_index_list]

