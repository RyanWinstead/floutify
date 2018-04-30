def imagePros():

	if openTrackingButtonClicked:
		video = cv2.VideoCapture(fileName)
		length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
		video.set(cv2.CAP_PROP_POS_FRAMES,trackbarValue)
		global image
		err, image = video.read()
	elif imageButtonClicked:
		global image
		image = cv2.imread(fileName)
    else:
        pass

	global image_gray1
	image_gray1= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	global image_contours
	image_contours = image.copy();
	#Adaptive Histogram Equalization
	clahe = cv2.createCLAHE(clipLimit=6, tileGridSize=(8,8))
	global cl1
	cl1 = clahe.apply(image_gray1)
	#Gray Scale GaussianBlur
	global image_gray
	image_gray = cv2.GaussianBlur(cl1, (3,3), 0,0);

	#image normalize
	dst = np.zeros(shape=(5,2))
	global image_norm
	image_norm= cv2.normalize(image_gray, dst, 0, 255, cv2.NORM_MINMAX)

	#Kernel Definitions
	kernel = np.ones((3,3),np.uint8)
	kernel2 = np.ones((1,2), np.uint8)

	#Threshold and Noise Reduction with dilation and erosion
	global image_edged
	ret, image_edged = cv2.threshold(image_norm, 115, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU);
	global image_edged2
	image_edged2 = cv2.dilate (image_edged, kernel, iterations = 2);
	global image_edged3
	image_edged3 = cv2.erode (image_edged2, kernel2, iterations = 3);

	#Find Contours
	cnts = cv2.findContours(image_edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE);
	#print(cnts)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    return cnts, image_edged3, image_contours