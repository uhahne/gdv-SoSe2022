# Corner detection on example image inspired by
# https://docs.opencv.org/4.5.3/dc/d0d/tutorial_py_features_harris.html

import numpy as np
import cv2


# display two images side by side
def showImagesSideBySide(img_A, img_B):
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))


# TODO: do a non-maximum suppression
def doNonMaximaSuppression(img, window_size):
    # loop over each pixel in the image and keep pixel only if
    # it is maximal in a window with window_size
    foo = 0  # TODO: remove this line (it is just here that the script is running)


# load example image
img = cv2.imread('images/chessboard-contrast-squares.jpg', cv2.IMREAD_COLOR)
# resize if needed
img = cv2.resize(img, None, fx=0.1, fy=0.1)

# define parameters for Harris corner detection
blockSize = 2
ksize = 3
k = 0.04
# TODO: create a greyscale image for the corner detection

# TODO: convert to floating point image

# TODO: harris corner detection using OpenCV method cornerHarris

# TODO: run non-maximum suppression to find isolated corner points

# TODO: dilate resulting image for increasing the corner size so that
# they become more visible than a single pixel

# TODO: threshold for an optimal value, it may vary depending on the image
# and set corner pixels in the original image to a distinct color
# HINT: use something like "img[corner_img > threshold] = color" instead
# of a draw function to keep it simple

# create window
window_name = 'Corner demo'
cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)

# show resulting images
# TODO: replace second image with the corner response image
showImagesSideBySide(img, img)

# wait for key to be pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
