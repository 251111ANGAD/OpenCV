#   Rotating images
import cv2
img_normal = cv2.imread("L1\pika.png")
rows, columns = img_normal.shape[:2]
img_matrix = cv2.getRotationMatrix2D((columns/2, rows/2), 45, 1)
img_rotated = cv2.warpAffine(img_normal, img_matrix, (columns, rows))

cv2.imshow("L3-2-1", img_normal)
cv2.imshow("L3-2-2", img_rotated)
if cv2.waitKey(0) == 27:  # Wait for ESC key to close all windows
    cv2.destroyAllWindows()