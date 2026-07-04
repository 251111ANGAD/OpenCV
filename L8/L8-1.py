import cv2
import os
import numpy as np
from PIL import Image

video = cv2.VideoCapture("L8\\video.mp4")

for i in range(60):
    value, bg = video.read()
    if value == False:
        continue

while video.isOpened():
    value, image = video.read()
    if value == False:
        break
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red_1 = np.array([0, 40, 40])
    upper_red_1 = np.array([0, 255, 255])
    mask_1 = cv2.inRange(image_HSV, lower_red_1, upper_red_1)
    lower_red_2 = np.array([160, 40, 40])
    upper_red_2 = np.array([180, 255, 255])
    mask_2 = cv2.inRange(image_HSV, lower_red_2, upper_red_2)
    mask = mask_1 + mask_2
    final_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2)
    dilated_mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations = 1)
    inverted_mask = cv2.bitwise_not(dilated_mask)
    background_pixels_1 = cv2.bitwise_and(bg, bg, mask = dilated_mask)
    background_pixels_2 = cv2.bitwise_and(image, image, mask = inverted_mask)
    final_output = cv2.addWeighted(background_pixels_1, 1, background_pixels_2, 1, 0)

    cv2.imshow("L8-1", final_output)
    if cv2.waitKey(10) == 27:
        break