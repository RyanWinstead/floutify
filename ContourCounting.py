def ContourCounting():
	import numpy as np
	import matplotlib.pyplot as plt
	import cv2
	import imutils
	import sys
	import tracking
	from window import fileName, videoButtonClicked, openTrackingButtonClicked
	from imageProcess import imagePros

	def checkIfSplit(cells, cx, cy):
		if checked == False:
			for i in range(length(cells)):
				for j in range(i+1, length(cells)):
					dx = abs(cells[j][0] - cells[i][0])
					if dx <=50:
						dy = abs(cells[j][1] - cells[i][1])
						if dy <=50:
							return checked


	def skipFrame(counter, countarry, trackbarValue):
		#edit later
		if countarry[trackbarValue] / countarry[trackbarValue-1] <= .60:
			return trackbarValue +1




	countarry= []
	#global counter
	#counter = 0

	cnts = []




	def onChange(trackbarValue, fileName):
		imagePros(fileName)

		#Ignore contours that do not satisfy size criteria
		cells = []
		bboxes = [];
		global x
		global y
		global w
		global h
		global counter
		counter = 0
		cellTags=[]
		for i in cnts:
			if cv2.contourArea(i) < 700 or cv2.contourArea(i) > 6000:
				continue;
			hull = cv2.convexHull(i);
			cv2.drawContours(image_contours,[hull],0,(34,255,34),2);
			x,y,w,h = cv2.boundingRect(i)
			bboxes.append([x, y, w, h])

			M = cv2.moments(i)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			cells.append([cx, cy])
			cellLet= chr(counter+67)
			cellTags.append(counter+67)
			cv2.putText(image_contours, cellLet, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (225,0,255),2);
			counter = counter + 1;

		# countarry.append(counter)
		cv2.putText(image_contours, "cell count: " + str(counter), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255),2);


		# countarry.append(counter)
		cv2.imshow("cellVid", image_contours);
		k = cv2.waitKey()
		print (cellTags)
		print (k)
		if k == 27:
			pass
		elif k in cellTags:
			print("key")
			cellnumber = k-67
			print(len(bboxes))
			print(cellnumber)
			tracking.track(bboxes[cellnumber][0], bboxes[cellnumber][1], bboxes[cellnumber][2], bboxes[cellnumber][3], cv2.CAP_PROP_POS_FRAMES)

		pass
	cv2.namedWindow('cellVid')
	cv2.createTrackbar( 'start', 'cellVid', 0, length, onChange )



	start = cv2.getTrackbarPos('start','cellVid')


	video.set(cv2.CAP_PROP_POS_FRAMES,start)


	onChange(0)




	#Return Results
	print("There are %d cells." %(counter));
	#cv2.imshow("Original GrayScale", image_gray1);
	#cv2.imshow("clahe_2", cl1);
	cv2.imshow("Original", image_contours);
	#cv2.imshow("open", image_edged2);
	cv2.imshow("erode", image_edged3);
	#cv2.imshow("threshold", image_edged);
	cv2.imshow("filter", image_gray);

	print("Before the wait")
	cv2.waitKey(0)
	print("After the wait");
	while(video.isOpened()):
	  ret, img=video.read()
	  if video.get(cv2.CAP_PROP_POS_FRAMES) >= end:
	     break
	  #cv2.imshow("Cell_Video", video)
	  if cv2.waitKey(1) or 0xFF == ord('q'):
	   break

	   return
