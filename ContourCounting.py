import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils
import sys
import tracking
from imageProcess import imagePros

#if image button is pressed
def ContourCounting(fileName):
    length = 0


    option = ""
    cnts, image_edged3, image_contours = imagePros(fileName, option)
    print(cnts, image_edged3, image_contours)

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
        #draw outlines around cells
    	cv2.drawContours(image_contours,[hull],0,(34,255,34),2);
    	counter = counter + 1;


    cv2.putText(image_contours, "cell count: " + str(counter), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255),2);


    cv2.imshow("Original", image_contours);
    print("Before the wait")
    cv2.waitKey(0)
    print("After the wait");

    return
