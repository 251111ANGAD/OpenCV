import cv2
import numpy as np

color_1 = np.array([245, 135, 66])
color_2 = np.array([212, 66, 245])

img_1 = np.full((300, 300, 3), color_1, dtype = np.uint8)
img_2 = np.full((300, 300, 3), color_2, dtype = np.uint8)
#Add colors
color_add_cv2 = cv2.add(img_1, img_2)
color_add_np = img_1 + img_2

print(f"cv2 add Result: {color_add_cv2[0][0]}")
print(f"np add Result: {color_add_np[0][0]}")
#Subtract colors
color_subtract_cv2 = cv2.subtract(img_1, img_2)
color_subtract_np = img_1 - img_2

print(f"\ncv2 subtract Result: {color_subtract_cv2[0][0]}")
print(f"np subtract Result: {color_subtract_np[0][0]}")
#Displaying this
cv2.putText(color_add_cv2, "Color Addition (cv2)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(color_subtract_cv2, "Color Subtraction (cv2)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
#Concactonating images
img = np.concatenate((img_1, img_2, color_add_cv2, color_subtract_cv2), axis=1)

cv2.imshow("L1-3", img)

if cv2.waitKey(0):
    cv2.destroyAllWindows()