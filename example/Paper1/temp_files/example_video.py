# 來源 https://github.com/IS2AI/thermal-facial-landmarks-detection
# 安裝dlib要用conda install -c conda-forge dlib 參考:https://pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/
# USAGE 
# python dlib_predict_video.py --input video/2_0.avi --models  models/ --upsample 1 --output demo/output.mp4

# 确保人脸图像是正的

import numpy as np

import sys
sys.path.insert(0, sys.path[0]+"/../")
from researchtoolbox.thermal_imaging import features_extraction as fe


input_file_path = "test_videos"  # 实际上是视频
model_path = "../resource/models"
output_file_path = "../result/thermal/video_output/"
no_rectangle_image_path = "../result/thermal/test_images_output/"
upsampling_times = 1
n_feature_points = 54+7  # 臉部特徵點的數量
n_sampling = 30  # downsampling
adaptive_length = np.int16(30*10/n_sampling)  # 多少禎以後，限制數值變化的範圍
resize_height = 600  # 調整影像的大小。600時，大概每秒可以處理1禎，但是如果下降到300，只需要1/100的時間。不過，識別正確性會減低。
height_lower_threshold = np.int16(resize_height*0.2)
height_upper_threshold = np.int16(resize_height*0.8)
x_average = 0
y_average = 0
minimum_gray_color = 30  # 設一個最低的值,以避免抓到奇怪的數值

para_dict = {
    "n_feature_points": n_feature_points,
    "n_sampling": n_sampling,
    "resize_height": resize_height,
    "upsampling_times": upsampling_times,
    "minimum_gray_color": minimum_gray_color
}

thermal = fe.features_extraction(model_path, input_file_path, output_file_path, no_rectangle_image_path, para_dict)
thermal.run()


