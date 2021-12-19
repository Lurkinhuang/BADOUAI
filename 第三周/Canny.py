'''Canny'''
import cv2
import numpy as np

# Method 1

# #   read img and change to gray
# img = cv2.imread('lenna.png', 0)
# # Gaussian filter
# img = cv2.GaussianBlur(img,(5,5),0)
# # Canny
# canny = cv2.Canny(img,50,128)
# cv2.imshow('canny', canny)
# cv2.waitKey(0)

# Method 2

def canny_threshold (low_threshold):
    detected_edges = cv2.GaussianBlur(img, (5, 5), 0)  # Gaussian filter
    detected_edges = cv2.Canny(detected_edges, low_threshold, low_threshold * ratio, apertureSize = kernel_size)  # Canny detection
    cv2.imshow('Canny', detected_edges)

# define parameter for canny function
low_threshold = 0
max_lowthreshold = 100
ratio = 3
kernel_size = 3

# read picture and change to gray
img = cv2.imread('lenna.png', 0)

# create bar
cv2.namedWindow('Canny')
cv2.createTrackbar('Min threshold', 'Canny', low_threshold, max_lowthreshold, canny_threshold)
canny_threshold(0)  # initialization

if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()