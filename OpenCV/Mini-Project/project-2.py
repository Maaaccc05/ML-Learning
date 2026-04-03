import cv2

file_path = input("Enter Your file location")

image = cv2.imread(file_path)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()