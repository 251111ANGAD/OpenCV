import cv2
import numpy as np

img = cv2.imread("L1\pika.png")
kernel = np.ones((15, 15), np.uint8)
img_eroded = cv2.erode(img, kernel)

cv2.imshow("L2-3-2", img_eroded)
cv2.imshow("L2-3-1", img)

if cv2.waitKey(0):
    cv2.destroyAllWindows()