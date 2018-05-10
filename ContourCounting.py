import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils
import sys
import tracking
# from window import fileName, videoButtonClicked, openTrackingButtonClicked
from imageProcess import imagePros


def ContourCounting(fileName):
    length = 0

	# def checkIfSplit(cells, cx, cy):
	# 	if checked == False:
	# 		for i in range(length(cells)):
	# 			for j in range(i+1, length(cells)):
	# 				dx = abs(cells[j][0] - cells[i][0])
	# 				if dx <=50:
	# 					dy = abs(cells[j][1] - cells[i][1])
	# 					if dy <=50:
	# 						return checked







	#global counter
	#counter = 0





    option = ""
    cnts, image_edged3, image_contours = imagePros(fileName, option)
    print(cnts, image_edged3, image_contours)


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
    	# x,y,w,h = cv2.boundingRect(i)
    	# bboxes.append([x, y, w, h])
        #
    	# M = cv2.moments(i)
    	# cx = int(M['m10']/M['m00'])
    	# cy = int(M['m01']/M['m00'])
    	# cells.append([cx, cy])
    	# cellLet= chr(counter+67)
    	# cellTags.append(counter+67)
    	# cv2.putText(image_contours, cellLet, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (225,0,255),2);
    	counter = counter + 1;

    # countarry.append(counter)
    cv2.putText(image_contours, "cell count: " + str(counter), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255),2);




    # #Return Results
    # print("There are %d cells." %(counter));
    # #cv2.imshow("Original GrayScale", image_gray1);
    # #cv2.imshow("clahe_2", cl1);
    cv2.imshow("Original", image_contours);
    # #cv2.imshow("open", image_edged2);
    #cv2.imshow("erode", image_edged3);
    #cv2.imshow("threshold", image_edged);
    #cv2.imshow("filter", image_gray);

    print("Before the wait")
    cv2.waitKey(0)
    print("After the wait");

    # if cv2.waitKey(1) or 0xFF == ord('q'):
        # break

    return
