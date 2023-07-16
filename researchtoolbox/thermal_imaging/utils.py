import cv2

def rotate_image(raw_frame):  # 把图像转正
    raw_frame = cv2.transpose(raw_frame)
    raw_frame = cv2.flip(raw_frame, 0)
    raw_frame = cv2.transpose(raw_frame)
    rotate_frame = cv2.flip(raw_frame, 0)
    return rotate_frame