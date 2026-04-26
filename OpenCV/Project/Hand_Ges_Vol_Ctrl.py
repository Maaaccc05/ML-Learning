import cv2
import mediapipe as mp
import pyautogui

camera = cv2.VideoCapture(0)

my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    _ , image = camera.read()
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert to RGB
    output = my_hands.process(rgb_img)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)

    cv2.imshow("Hand Gesture Volume Control", image)
    key = cv2.waitKey(10)
    
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()