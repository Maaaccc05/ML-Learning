import cv2
image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is not None:
    cropped = image[50:300, 60:200]

    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# syntax for image cropping --> image[start y: end y, start x: end x]