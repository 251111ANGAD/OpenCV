import cv2
import os

cascade = cv2.CascadeClassifier("L9\\face_detector.xml")
folder = "L9\\images"
subfolder = "L9\\images\\private"
path = os.path.join(folder, subfolder)

if not os.path.exists(path):
    os.makedirs(path)

width, height = 640, 480
face_cascade = cv2.CascadeClassifier("L9\\face_detector.xml")
cam = cv2.VideoCapture()
 
count = 1
while count < 30:
    value, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)
        face = gray[y:y + h, x:x + w]
        face_resized = cv2.resize(face, (width, height))
        cv2.imwrite(os.path.join(path, f"face_{count}.jpg"), face_resized)
        count += 1
    cv2.imshow("L9-1", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()