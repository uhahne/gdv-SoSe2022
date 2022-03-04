# Corner detection on example image inspired by
# https://docs.opencv.org/4.5.3/dc/d0d/tutorial_py_features_harris.html

import numpy as np
import cv2


# display two images side by side
def showImagesSideBySide(img_A, img_B):
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))


# do a non-maximum suppression
def doNonMaximaSuppression(img, window_size):
    # loop over each pixel in the image and keep pixel only if
    # it is maximal in a window with kernel_size
    h, w = img.shape
    result = np.zeros((h, w), np.uint8)
    offset = int((window_size - 1) / 2)
    for y in range(offset, h-1-offset):
        for x in range(offset, w-1-offset):
            window = img[y-offset:y+1+offset, x-offset:x+1+offset]
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(window)
            if (max_loc == (offset, offset)):
                result[y, x] = img[y, x]
    return result


# load example image
img = cv2.imread('images/chessboard-contrast-squares.jpg', cv2.IMREAD_COLOR)
# resize if needed
img = cv2.resize(img, None, fx=0.1, fy=0.1)

# define parameters for Harris corner detection
blockSize = 2
ksize = 3
k = 0.04
# create a greyscale image for the corner detection
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert to floating point image
img_float = np.float32(img_gray)
# harris corner detection using OpenCV method cornerHarris
harris_corner_img = cv2.cornerHarris(img_float, blockSize, ksize, k)
# run non-maximum suppression to find isolated corner points
img_suppressed = doNonMaximaSuppression(harris_corner_img, 5)
# resulting image is dilated for increasing the corner size so that
# they become more visible than a single pixel
img_dilated = cv2.dilate(img_suppressed, None)

# threshold for an optimal value, it may vary depending on the image and set
# corner pixels in the original image to a distinct color
img[img_dilated > 0.01*img_dilated.max()] = [0, 0, 255]

# create window
window_name = 'Corner demo'
cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)

# show resulting images
showImagesSideBySide(img, cv2.cvtColor(img_suppressed,
                                       cv2.COLOR_GRAY2BGR))

# wait for key to be pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
