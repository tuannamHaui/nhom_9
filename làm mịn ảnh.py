import cv2
import numpy as np

# Định nghĩa kernel_size
kernel_size_1 = (3, 3)
kernel_size_2 = (3, 3)
kernel_size_3 = (5, 5)

image = cv2.imread('C:/Users/THAO/Pictures/Camera Roll/WIN_20231024_08_48_45_Pro.jpg')

kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                             [-1,2,2,2,-1],
                             [-1,2,8,2,-1],
                             [-1,2,2,2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0

# Áp dụng bộ lọc
smoothed_image_1 = cv2.filter2D(image, -1, kernel_sharpen_1)
smoothed_image_2 = cv2.filter2D(image, -1, kernel_sharpen_2)
smoothed_image_3 = cv2.filter2D(image, -1, kernel_sharpen_3)

cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image_1', smoothed_image_1)
cv2.imshow('Smoothed Image_2', smoothed_image_2)
cv2.imshow('Smoothed Image_3', smoothed_image_3)

cv2.waitKey(0)
cv2.destroyAllWindows()
