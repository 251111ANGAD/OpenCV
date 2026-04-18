import cv2
img = cv2.imread("pika.png", 255)#The (..., 0) means greyscale
img_1 = cv2.imread("pika.png")
print(img_1.shape)
#Show loaded image in a new window with a title
cv2.imshow("L1", img)
#Hold the window until user presses key
cv2.waitKey(0)
#Close image window after key is pressed
cv2.destroyAllWindows()