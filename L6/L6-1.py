#   Creating a video collage using OpenCV
import cv2
import os
from PIL import Image
os.chdir("C:\\Users\\denis\\OneDrive\\Desktop\\OpenCV\\L6\\L6-Images")
path = "C:\\Users\\denis\\OneDrive\\Desktop\\OpenCV\\L6\\L6-Images"
mean_height = 0
mean_width = 0
num_images = len(os.listdir(path))
print(num_images)
for i in os.listdir("."):
    images = Image.open(os.path.join(path, i))
    width, height = images.size
    mean_width += width
    mean_height += height
mean_width = mean_width//num_images; print(mean_width)
mean_height = mean_height//num_images; print(mean_height)
#   Resizing images to the given height and width
for i in os.listdir("."):
    if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
        images = Image.open(os.path.join(path, i))
        width, height = images.size
        resized = images.resize((mean_width, mean_height), Image.LANCZOS)
        resized.save(i)
        print("Image Resized Sucessfully")
def create_video_collage():
    video_name = "L6-1.avi"
    os.chdir("C:\\Users\\denis\\OneDrive\\Desktop\\OpenCV\\L6\\L6-Images")
    image = []
    for i in os.listdir("."):
        if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
            image.append(i)
    frame = cv2.imread(os.path.join(".", image[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    for i in image:
        video.write(cv2.imread(os.path.join(".", i)))
    cv2.destroyAllWindows()
    video.release()
create_video_collage()