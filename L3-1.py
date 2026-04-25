import cv2

img_normal = cv2.imread("L1\pika.png")
img_grayscaled = cv2.imread("L1\pika.png")
img_grayscaled_cv2 = cv2.imread("L1\pika.png", 0)

#   How Grayscaling Happens
row, column = img_normal.shape[0:2]

for i in range(row):
    for j in range(column):
        img_grayscaled[i, j] = sum(img_grayscaled[i, j]) * (1/3)

cv2.imshow("L3-1-1", img_normal)
cv2.imshow("L3-1-2", img_grayscaled)
cv2.imshow("L3-1-3", img_grayscaled_cv2)

if cv2.waitKey(0):
    cv2.destroyAllWindows()