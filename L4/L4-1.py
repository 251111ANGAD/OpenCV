#   Drawing Shapes
import cv2
img_normal = cv2.imread("L1\pika.png")
img_line = cv2.imread("L1\pika.png")
img_rectangle = cv2.imread("L1\pika.png")
img_circle = cv2.imread("L1\pika.png")
img_text = cv2.imread("L1\pika.png")
img_line = cv2.line(img_line, (0, 0), (200, 200), (255, 0, 0), 5)  # Draw a blue line from top-left to (200, 200) with thickness of 5
img_rectangle = cv2.rectangle(img_rectangle, (50, 50), (150, 150), (0, 255, 0), -1)  # Draw a green rectangle from (50, 50) to (150, 150) with filled color
img_circle = cv2.circle(img_circle, (200, 200), 50, (0, 0, 255), -1)  # Draw a red circle at (200, 200) with radius of 50 and filled color  
img_text = cv2.putText(img_text, "Hello, OpenCV!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # Draw blue text at (50, 50) with font scale of 1 and thickness of 2

cv2.imshow("L4-1-1", img_normal)
cv2.imshow("L4-1-2", img_line)
cv2.imshow("L4-1-3", img_rectangle)
cv2.imshow("L4-1-4", img_circle)
cv2.imshow("L4-1-5", img_text)
if cv2.waitKey(0) == 27:  # Wait for ESC key to close all windows
    cv2.destroyAllWindows()