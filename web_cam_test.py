import cv2
import time
import threading

#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("http://10.21.143.47:8080/video")
#cap =
cap = cv2.open("http://10.21.143.47:8080/video")
cap.set(3,640)
cap.set(4,360)
#cap.set(3,1280)
#cap.set(4,720)
#cap.set(6, 24)
print(cv2.CAP_PROP_FPS)
i = 0
fps = 1
seconds = 0
start = time.time()
a = 0

ret, frame = cap.read()

def draw():
    global frame
    #frame = cv2.resize(frame,(1280,720))
    cv2.putText(frame,"fps: "+str(fps),(2,50),cv2.FONT_HERSHEY_SIMPLEX,1,(124,252,0),2,cv2.LINE_AA)

    if i//30 == 1:
        seconds = time.time() - start
        fps = i//seconds
        i = 0
        start = time.time()
    i+=1
    return 0

#t = threading.Thread(target=draw)
while (True):
    t = threading.Thread(target=draw)
    t.start()
    ret, frame = cap.read()
    #frame = cv2.resize(frame,(1280,720))
    #cv2.putText(frame,"fps: "+str(fps),(2,50),cv2.FONT_HERSHEY_SIMPLEX,1,(124,252,0),2,cv2.LINE_AA)

    t.join()
    if t.isAlive():
        time.sleep(0.001)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break
    



cap.release()
cv2.destroyAllWindows()
