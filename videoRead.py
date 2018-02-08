import numpy as np
import cv2

def nothing(x):
    pass

video = cv2.VideoCapture('luluvid.mp4')

cv2.namedWindow("video")
cv2.resizeWindow('Video', 100,100)
cv2.createTrackbar("Scrubber","video",0,10,nothing)
total = 0

while(video.isOpened()):
    ret, frame = video.read()
    (grabbed, frame) = video.read()
    if not grabbed:
        total+=1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #img = cv2.IMREAD_COLOR(frame,0)
    cv2.imshow('video',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
