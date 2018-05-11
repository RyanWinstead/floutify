import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils
import sys
import tracking
# from window import fileName, videoButtonClicked, openTrackingButtonClicked
from imageProcess import imagePros


class vidContour():
	def __init__(self, fileName):
		self.fileName = fileName
		cv2.namedWindow('cellVid')
		self.video = cv2.VideoCapture(self.fileName)
		self.length  = int(self.video.get(cv2.CAP_PROP_POS_FRAMES))
		cv2.createTrackbar( 'start', 'cellVid', 0, self.length, self.onChange)
		self.start = cv2.getTrackbarPos('start','cellVid')
		self.onChange(0)



	def onChange(self, trackbarValue):
		#set video to starting frame
		self.video.set(cv2.CAP_PROP_POS_FRAMES,self.start)
		cnts, image_edged3, image_contours = imagePros(self.fileName, option ='vid')


		cells = []
		bboxes = [];
		global x
		global y
		global w
		global h
		global counter
		counter = 0
		cellTags=[]
		#Ignore contours that do not satisfy size criteria
		for i in cnts:
			if cv2.contourArea(i) < 700 or cv2.contourArea(i) > 6000:
				continue;
			hull = cv2.convexHull(i);
			cv2.drawContours(image_contours,[hull],0,(34,255,34),2);
			x,y,w,h = cv2.boundingRect(i)
			#save coordinates in bboxes array
			bboxes.append([x, y, w, h])

			M = cv2.moments(i)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			#save centers in cells array
			cells.append([cx, cy])
			cellLet= chr(counter+67)
			cellTags.append(counter+67)
			cv2.putText(image_contours, cellLet, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (225,0,255),2);
			counter = counter + 1;

		cv2.putText(image_contours, "cell count: " + str(counter), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255),2);

		#show starting video frame with each cell tagged
		cv2.imshow("cellVid", image_contours);
		k = cv2.waitKey()
		print (cellTags)
		print (k)
		if k == 27:
			pass
		elif k in cellTags:
			#selected cell's coordinates are sent to tracking
			print("key")
			cellnumber = k-67
			print(len(bboxes))
			print(cellnumber)
			tracking.track(bboxes[cellnumber][0], bboxes[cellnumber][1], bboxes[cellnumber][2], bboxes[cellnumber][3], cv2.CAP_PROP_POS_FRAMES, self.fileName)

		pass
