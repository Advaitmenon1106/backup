import cv2
import numpy as np

def sliding_window(image, stepSize, windowSize):
	# slide a window across the image
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

winW = 256
winH = 256

cap = cv2.VideoCapture('Assignment3/soccer-closeup.mp4')
#cap = cv2.VideoCapture(0)

master = cv2.imread('Assignment3/template.jpeg')
sift = cv2.SIFT_create(nfeatures=200)
master = cv2.GaussianBlur(master,(3,3),0)   
kp1, des1 = sift.detectAndCompute(master, None)
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame,(3,3),0)   
    #frame = cv2.resize(frame,(500,300))
    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    max_match = 0
    x1=0
    y1=0
    for (x, y, window) in sliding_window(frame, stepSize=64, windowSize=(winW, winH)):
            if window.shape[0] != winH or window.shape[1] != winW:
                continue
            kp2, des2 = sift.detectAndCompute(window, None)
            if des2 is not None:
                matches = bf.match(des1, des2)
                if len(matches) > max_match:
                      max_match = len(matches)
                      x1=x
                      y1=y
    cv2.rectangle(frame, (x1, y1), (x1 + winW, y1 + winH), (0, 255, 0), 2)		
    cv2.imshow("Face Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
