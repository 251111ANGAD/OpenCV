import cv2
#   Image resizing
img = cv2.imread("L2\house.jpg")
img_resized = cv2.resize(img, (200, 200))

cv2.imshow("L2-2-2", img_resized)
cv2.imshow("L2-2-1", img)

if cv2.waitKey(0):
    cv2.destroyAllWindows()