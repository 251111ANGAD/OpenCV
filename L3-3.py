#   Edge Detection
import cv2
img_normal = cv2.imread("L1\pika.png")
img_edges = cv2.Canny(img_normal, 800, 700)  # Canny edge detection with lower and upper thresholds
cv2.imshow("L3-3-1", img_normal)
cv2.imshow("L3-3-2", img_edges)
if cv2.waitKey(0) == 27:  # Wait for ESC key to close all windows
    cv2.destroyAllWindows()