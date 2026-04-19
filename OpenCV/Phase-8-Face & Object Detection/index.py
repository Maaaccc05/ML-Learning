import cv2

face_cascade = cv2.CascadeClassifier("OpenCV/Phase-8-Face & Object Detection/haarcascade_frontalcatface.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.05, 5) # ---> 1.1 is ---> Reduce image size by 10% at each step, 5 is ---> How many nearby detections are needed to confirm a face

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()