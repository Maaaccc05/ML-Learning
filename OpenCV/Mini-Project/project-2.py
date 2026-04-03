import cv2

file_path = input("Enter Your file location")

image = cv2.imread(file_path)

choice = input("1.Type 'line' for drawing line on image\n2.Type 'rectangle' to draw rectangle on image\n3.Type 'circle' to draw circle on image\n4.Type 'text' to add tect on image ").lower()

if choice == 'line':
    pt1 = input("Enter the point from where you want line")
    pt2 = input("Enter the point till where you want line")
    color = input("Choose color in format of (0, 0, 0)")
    thickness = input("Choose thickness")
    cv2.line(image, pt1,pt2, color, thickness)
else:
    print("Wrong text")
