import cv2

faceDetction = cv2.CascadeClassifier("OpenCV/Mini-Project/Face Detection/haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetction.detectMultiScale(gray, 1.5, 4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 4)
    
    cv2.imshow("FaceCam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
