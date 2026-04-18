import cv2
import numpy as np

img = cv2.imread("umbrella.webp")
#Convert the image to rgb
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Splitting the image into it's 3 channels
r, g, b = cv2.split(img)

cv2.imshow("R", r)
cv2.imshow("G", g)
cv2.imshow("B", b)

if cv2.waitKey(0):
    cv2.destroyAllWindows()