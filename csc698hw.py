import cv2
import numpy as np 

CURRENT_FRAME_FLAG = cv2.CV_CAP_PROP_POS_FRAMES
TOTAL_FRAMES_FLAG = cv2.CV_CAP_PROP_FRAME_COUNT
WIN_NAME = "Frame Grabber"
POS_TRACKBAR = "pos_trackbar"
VIDEO_PATH = None

cap = cv2.VideoCapture('cellvid.avi')
'''
output file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


def save_image():
    filename = "image_%0.5f.png" % t.time()
    cv2.imwrite(filename, frame)
'''
cv2.namedWindow(WIN_NAME)

def seek_callback(x):
	global frame
	i = cv2.getTrackbarPos(POS_TRACKBAR, WIN_NAME)
	cap.set(CURRENT_FRAME_FLAG, i-1)
	_, frame = cap.read()
	cv2.imshow(WIN_NAME, frame)


cv2.createTrackbar(POS_TRACKBAR, WIN_NAME, 0, int(cap.get(TOTAL_FRAMES_FLAG)), seek_callback)

def mouse_callback(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        save_image()

cv2.setMouseCallback(WIN_NAME, mouse_callback)



def skip_frame_generator(df):

    def skip_frame():
        global frame
        # get the current frame position
        cf = cap.get(CURRENT_FRAME_FLAG) - 1
        # skip of df frames
        cap.set(CURRENT_FRAME_FLAG, cf+df)
        # update the trackbar position
        cv2.setTrackbarPos(POS_TRACKBAR, WIN_NAME, int(cap.get(CURRENT_FRAME_FLAG)))
        # read and update the frame
        _, frame = cap.read()

    return skip_frame

    actions = dict()

actions[ord("D")] = skip_frame_generator(10)
actions[ord("d")] = skip_frame_generator(1)
actions[ord("a")] = skip_frame_generator(-1)
actions[ord("A")] = skip_frame_generator(-10)
actions[ord("q")] = lambda: exit(0)
actions[ord("s")] = save_image

def dummy ():
	pass

while True:

	'''
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	#out.write(frame) #TAKE VIDEO
	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)
'''
	cv2.imshow(WIN_NAME, frame)
	#waits for key stroke
	key =cv2.waitKey(0) & 0xFF
	actions.get(key, dummy)()

	'''
	if cv2.waitKey(96) & 0xFF == ord('q'):
		break
'''
cap.release() #releases the video so its not in use
#out.release()
cv2.destroyAllWindows()