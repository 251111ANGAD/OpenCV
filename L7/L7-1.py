import cv2
import numpy as np

image = cv2.imread("L7\\Image20260613172358.jpg")
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#   First red range
lower_red = np.array([0, 40, 40])
upper_red = np.array([0, 255, 255])
#   Creating the first mask
mask_1 = cv2.inRange(image_HSV, lower_red, upper_red)
#   Second red range
lower_red_1 = np.array([160, 40, 40])
upper_red_1 = np.array([180, 255, 255])
#   Creating the second mask
mask_2 = cv2.inRange(image_HSV, lower_red_1, upper_red_1)
#   Merging the two masks
mask = mask_1 + mask_2
#   Morphological opening (removes small objects from the foreground)
final_mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2)
#   Dilation
dilated_mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations = 1)

cv2.imshow("L7-1 (Red Mask 1)", mask_1)
cv2.imshow("L7-2 (Red Mask 2)", mask_2)
cv2.imshow("L7-3 (Merged Masks)", mask)
cv2.imshow("L7-4 (Final Mask)", final_mask)
cv2.imshow("L7-5 (Dilated Mask)", dilated_mask)
cv2.imshow("L7-6 (HSV Image)", image_HSV)
cv2.imshow("L7-7 (Original Image)", image)

cv2.waitKey(0)
cv2.destroyAllWindows()