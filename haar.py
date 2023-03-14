import cv2
img=cv2.imread("4f.jpg")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces=face_cascade.detectMultiScale(grey,1.1,4)
print(len(faces))

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)


