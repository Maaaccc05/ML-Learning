# Gaussian Blur Syntax: cv2.GaussianBlur(src, (kernel_size, kernel_size), sigma)

import cv2
import numpy as np

image = cv2.imread("OpenCV/landscape-lake-mountain-clear-nature-wallpaper-preview.jpg")

blur = cv2.GaussianBlur(image, (21, 21), 5) # Can't pass even value it should be odd in kernel_size

cv2.imshow("Original",image)
cv2.imshow("Blurr", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()



# Median Blur Syntax : cv2.medianBlur(src, kernel_size)

img = cv2.imread("OpenCV/Blur-img2.jpeg")

med_blur = cv2.medianBlur(img, 3)

cv2.imshow("Original",img)
cv2.imshow("MedianBlur", med_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()



# Sharpening an Image Syntax: cv2.filter2D(src, ddepth, kernel)

sharpenImg = cv2.imread("OpenCV/37054504-089d7a00-214d-11e8-8982-ca836f7a4460.jpg")

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(sharpenImg, -1, sharpen_kernel)

cv2.imshow("Original", sharpenImg)
cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()