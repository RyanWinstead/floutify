#taking file name from videoMinEX.py putting through opencv tracker.py use opennCv QT functions

video = cv2.VideoCapture(fileName)
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
def onChange(trackbarValue):
        video.set(cv2.CAP_PROP_POS_FRAMES,trackbarValue)
        err,img = video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        cv2.imshow('video',gray)
        pass

"""
finish UI
    Mainwindow(buttons)
    PLayer window(opencv qt)
    make it pretty
    image normalization, histogram equlixation settings in UI
    cell type

****splitting cells(mAYRA'S CODE)
    function
    cut noisy frames out









3D video
    understand 2d
    plan how to move from 2d to 3d
"""


help tracker
organize github files
clean up code
