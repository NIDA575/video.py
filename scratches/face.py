import cv2

#import numpy

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img=cv2.imread("C:\\Users\\HP\\Pictures\\Camera Roll\\farhana.jpg",1)

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.05, 5)

#resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(w+w,y+h),(0,255,0),3)

print(type(faces))

print(faces)

cv2.imshow("Gray",img)

print(img.shape)

#cv2.imshow("Queen",resized)

#cv2.imshow("Queen",img)

cv2.waitKey(0)

cv2.destroyAllWindows()

