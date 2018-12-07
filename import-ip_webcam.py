# Using Android IP Webcam video .jpg stream (tested) automated translation from 2to3 in Python3 OpenCV4

import urllib.request, urllib.parse, urllib.error # was import urllib for Python2
import cv2
import numpy as np
import time

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.178.11:8080/shot.jpg'


while True:
    # Use urllib to get the image from the IP camera
    imgResp = urllib.request.urlopen(url) # was urllib.urlopen for Python2

    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)

    # Resize image
    cv2.namedWindow('IPWebcam',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('IPWebcam', 600,320)
	
    # put the image on screen
    cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    #time.sleep(0.1) 

    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
