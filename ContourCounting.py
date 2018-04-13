import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils

counter = 0;

image1 = cv2.imread("crop2.png");
image = cv2.imread("crop2.png", 0);

image_contours = image1.copy();

#Adaptive Histogram Equalization
clahe = cv2.createCLAHE(clipLimit=6, tileGridSize=(8,8))
cl1 = clahe.apply(image)
#Gray Scale GaussianBlur
image_gray = cv2.GaussianBlur(cl1, (3,3), 0,0);

#Kernel Definitions
kernel = np.ones((3,3),np.uint8)
kernel2 = np.ones((1,2), np.uint8)

#Threshold and Noise Reduction with dilation and erosion
ret, image_edged = cv2.threshold(image_gray, 115, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU);
image_edged2 = cv2.dilate (image_edged, kernel, iterations = 2);
image_edged3 = cv2.erode (image_edged2, kernel2, iterations = 3);

#Find Contours
cnts = cv2.findContours(image_edged3.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

#Ignore contours that do not satisfy size criteria
for i in cnts:
	if cv2.contourArea(i) < 700 or cv2.contourArea(i) > 6000:
		continue;
	hull = cv2.convexHull(i);
	cv2.drawContours(image_contours,[hull],0,(34,255,34),2);
	counter = counter + 1;

counter = counter;
#Return Results
print "There are %d cells." %(counter);
cv2.imshow("Original GrayScale", image);
cv2.imshow("clahe_2", cl1);
cv2.imshow("Original", image_contours);
cv2.imshow("open", image_edged2);
cv2.imshow("erode", image_edged3);
cv2.imshow("threshold", image_edged);
cv2.imshow("filter", image_gray);

cv2.waitKey(0)
