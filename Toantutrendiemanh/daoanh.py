import cv2
import numpy as np
# Đọc ảnh
img = cv2.imread('anh1.jpg', 0)
# hiển thị kiểu dữ liệu của ảnh
print(img.dtype)
# Tạo âm bản
img_neg = 255 - img
# Hiển thị ảnh
cv2.imshow('negative',img_neg)
cv2.waitKey(0)