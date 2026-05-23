import cv2
import numpy as np

img_normal = cv2.imread("L1\pika.png")
gray = cv2.cvtColor(img_normal, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (5, 5), 0)
detected_circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)
print(detected_circles)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for i in detected_circles [0, :]:
        a, b, r = i[0], i[1], i[2]
        cv2.circle(img_normal, (a, b), r, (0, 0, 255), 2)
        cv2.imshow("L5-1-1", img_normal)
        cv2.waitKey(0)
cv2.destroyAllWindows()