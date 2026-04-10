# syntax ---> cv2.VideoWriter(filename, codec, fps, frame_size)  codec---> compression format, fps ---> frames per second

import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

