import cv2

image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is not None:
    cv2.imshow("Minato", image) # It will open the window
    cv2.waitKey(0) # Wait for key to close 
    cv2.destroyAllWindows() # Close the window
else:
    print("Could not load the image")
