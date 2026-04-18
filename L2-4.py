import cv2

img = cv2.imread("L1\pika.png")
img_old = cv2.imread("L2\{D3EF25EB-83A3-4425-8E93-6D387E8C5B8F}.png")
#   Gaussian Blur
img_gb = cv2.GaussianBlur(img, (15, 15), 0)
#   Median Blur
img_mb_new = cv2.medianBlur(img, 15)
img_mb_old = cv2.medianBlur(img_old, 3)

cv2.imshow("L2-4-1", img)
cv2.imshow("L2-4-2", img_gb)
cv2.imshow("L2-4-3-1", img_mb_new)
cv2.imshow("L2-4-3-2", img_mb_old)

if cv2.waitKey(0):
    cv2.destroyAllWindows()