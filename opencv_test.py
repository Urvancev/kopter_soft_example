import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

#cap.set(3,1366)
#cap.set(4,768)


i = 0
X = 10
Y = 100
n = 0
n1 = 0
num_frames = 0
start = time.time()
fps = 0
while(True):
    # Capture frame-by-frame

    ret, frame = cap.read()
        
   
    font = cv2.FONT_HERSHEY_SIMPLEX
    #fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(frame,"hello world"+str(i),(X,Y),font,2,(124,252,0),2,cv2.LINE_AA)
    cv2.putText(frame,"fps: "+str(fps),(2,50),font,1,(124,252,0),2,cv2.LINE_AA)
    # Display the resulting frame
    cv2.imshow('frame',frame)

    
    
    if X<400 and n == 0:
        X+=10
    elif X>=10:
        X-=10
        n = 1
    elif X<10:
        n = 0
    if Y<600 and n1 == 0:
        Y+=50
    elif Y>=100:
        Y-=50
        n1 = 1
    elif Y<100:
        n1 = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if i//30 == 1:
        seconds = time.time() - start
        fps = i//seconds
        i = 0
        start = time.time()
    i+=1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
