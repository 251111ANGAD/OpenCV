import cv2
import os

video = cv2.VideoCapture("L8\\Cars.mp4")
cascade = cv2.CascadeClassifier("L8\\cars.xml")

while True:
    value, bg = video.read()
    gray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    cars = cascade.detectMultiScale(gray, 1.1, 3)
    #   Drawing rectangle on cars
    for (x, y, w, h) in cars:
        cv2.rectangle(bg, (x, y), (x + w, y + h), (255, 0, 255), 2)
    cv2.imshow("L8-2", bg)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()