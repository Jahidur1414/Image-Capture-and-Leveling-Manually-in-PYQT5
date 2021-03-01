
import cv2
import numpy as np
import os, sys

cropping = False

x_start, y_start, x_end, y_end = 0, 0, 0, 0

dir = "images/"
#-------------------------------------
dir_processed = dir #+ "_processed"
output_dir = "Croped_Image/" #+ "_small"

global image, oriImage

def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
    global croppedImage

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False  # cropping is finished

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2:  # when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            croppedImage = roi
            cv2.imshow("Cropped", roi)


for file in os.listdir(dir):

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)

    fullpath = dir + '/' + file

    image = cv2.imread(fullpath,0)
    oriImage = image.copy()

    key = cv2.waitKey(1) & 0xFF
    while True:
        i = image.copy()

        if not cropping:
            cv2.imshow("image", image)

        elif cropping:
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
            cv2.imshow("image", i)

        # cv2.imwrite(output_dir + '/' + file, i)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('a'):
            cv2.imwrite(output_dir + '/' + file, croppedImage)
            cv2.destroyAllWindows()
            break

# close all open windows
cv2.destroyAllWindows()
