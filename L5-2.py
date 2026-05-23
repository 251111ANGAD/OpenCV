import cv2
import numpy as np
img_normal = cv2.imread("L5\Image20260523172643.jpg", 0)
params = cv2.SimpleBlobDetector_Params()
# Describe the parameters for blob detection
# Setting area filtering parameter
params.filterByArea = True
params.minArea = 100
# Setting circularity filtering parameter
params.filterByCircularity = True
params.minCircularity = 0.8
# Setting convexity filtering parameter
params.filterByConvexity = True
params.minConvexity = 0.2
# Setting inertia filtering parameter
params.filterByInertia = True
params.minInertiaRatio = 0.01
# Create a blob detector with the specified parameters
detector = cv2.SimpleBlobDetector_create(params)
# Detect blobs in the image
keypoints = detector.detect(img_normal)
# Draw detected blobs as red circles
blob_image = cv2.drawKeypoints(img_normal, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
text = f"Number of blobs detected: {len(keypoints)}"
cv2.putText(blob_image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
# Display the original image and the image with detected blobs
cv2.imshow("Original Image", img_normal)
cv2.imshow("Detected Blobs", blob_image)
cv2.waitKey(0)
cv2.destroyAllWindows()