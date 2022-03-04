# Edge detection on an example image

import numpy as np
import cv2


def showImagesSideBySide(img_A, img_B):
    '''Helper function to draw two images side by side'''
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))


def on_change(val):
    '''callback function for the sliders'''
    # read slider positions
    blur_slider_pos = cv2.getTrackbarPos('Blur: ', window_name)
    ksize = (blur_slider_pos, blur_slider_pos)
    T_lower = cv2.getTrackbarPos('T_lower: ', window_name)
    T_upper = cv2.getTrackbarPos('T_upper: ', window_name)
    # blur the image
    img = cv2.blur(img_clone, ksize)
    # run Canny edge detection with thresholds set by sliders
    canny = cv2.Canny(img, T_lower, T_upper)
    # show the resulting images in one window
    showImagesSideBySide(img, canny)


# load example image as grayscale
img = cv2.imread('images\\nl_clown.jpg', cv2.IMREAD_GRAYSCALE)
# resize if needed
img = cv2.resize(img, (400, 400))
# clone if needed
img_clone = np.copy(img)

# initial Canny edge detection result creation
T_lower = 30
T_upper = 240
canny = cv2.Canny(img, T_lower, T_upper)
# DEBUG: print(cv2.minMaxLoc(canny))

''' create window with sliders '''
# define a window name
window_name = 'Canny edge detection demo'
# show the resulting images in one window
showImagesSideBySide(img, canny)
# create trackbars (sliders) for the window and define one callback function
cv2.createTrackbar('Blur: ', window_name, 1, 150, on_change)
cv2.createTrackbar('T_lower: ', window_name, 30, 255, on_change)
cv2.createTrackbar('T_upper: ', window_name, 240, 255, on_change)

# wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
























