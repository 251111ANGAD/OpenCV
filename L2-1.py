import cv2
import numpy as np
import random

house = cv2.imread("L2\house.jpg")
planet = cv2.imread("L2\planet.jpg")
plouse = cv2.addWeighted(house, random.random(), planet, random.random(), 0)
husplant = cv2.subtract(house, planet)

cv2.imshow("L2-1-1", plouse)
cv2.imshow("L2-1-2", husplant)

if cv2.waitKey(0):
    cv2.destroyAllWindows()