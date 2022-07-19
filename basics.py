import time

import cv2

# img = cv2.imread(r"C:\Users\asus\Desktop\New folder\face.jpeg", 1)
# # print(type(img))
# # print(img.shape)
# # resizing the image
# resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[1]/2)))
# cv2.imshow("Legend", resized)  # to display the img
# cv2.waitKey(0)  # to delay the time of the image
# cv2.destroyAllWindows()
# now program to read the video
# video = cv2.VideoCapture(0)
# check, frame = video.read()              # frame is numpy array,that represents the first image that video captures
# print(check)           # and check is a bool data type, return true if python is able to read the VideoCapture Object
# print(frame)
# time.sleep(3)
# cv2.imshow("Capture",frame)
# cv2.waitKey(0)
# video.release()
# cv2.destroyAllWindows()
# now we are going to capture the video, we will use while loop.While condition will be such that ,until unless 'check'
# is true, python will display the frames because basically video is multiple frames which appears so quickly
# so it looks like a video
video = cv2.VideoCapture(0)
a = 1
while True:
    a = a + 1
    check, frame = video.read()
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # convert each image into gray scale image
    cv2.imshow("Capture",gray)
    key = cv2.waitKey(1)   # this will generate a new frame every 1 millisecond
    if key == ord('q'):   # once you enter the q window will be destroyed
        break
print(a)
video.release()
cv2.destroyAllWindows()

