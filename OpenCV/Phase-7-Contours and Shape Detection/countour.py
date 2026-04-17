"""
    Syntax of Countours: contours, hierarchy = cv2.findContours(img, mode, method)
    Syntax for Draw Contoirs: cv2.drawContours(img, contours, contour_index, color, thickness)

"""

import cv2

img = cv2.imread("OpenCV/Phase-7-Contours and Shape Detection/triangle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Find Contours

contours, hirearchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()