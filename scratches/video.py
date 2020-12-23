import cv2,time
video=cv2.VideoCapture(0)
time.sleep(5)
video.release()
"""check,frame=video.read()
print(check)
print(frame)
time.sleep(3)
cv2.imshow('capture',frame)"""
#cv2.waitkey(0)
"""a=1
while 1:
    a=a+1
    check,frame=video.read()
    print(frame)
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('capture',grey)
    key=cv2.waitkey(1)
    if key==ord('q'):
        break
print(a)"""
#video.release()
cv2.destroyAllWindows()