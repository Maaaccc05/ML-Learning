import cv2
from util import get_limits
from PIL import Image


Green = [0, 255, 0]
cap = cv2.VideoCapture("http://192.168.0.114:4747/video")
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=Green)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    boundbox = mask_.getbbox()

    if boundbox is not None:
        x1, y1, x2, y2 = boundbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
        
    cv2.imshow("Vid", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()