# Edge detection on an example image

import numpy as np
import cv2


def showImagesSideBySide(img_A, img_B):
    '''Helper function to draw two images side by side'''
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))


# TODO: Define callback function
    '''callback function for the sliders'''
    # read slider positions
    
    # blur the image
    
    # run Canny edge detection with thresholds set by sliders
    
    # show the resulting images in one window
    showImagesSideBySide(img, canny)


# TODO: load example image as grayscale

# resize if needed

# clone if needed


# TODO: initial Canny edge detection result creation


# TODO: create window with sliders
# define a window name
window_name = 'Canny edge detection demo'
# show the resulting images in one window

# create trackbars (sliders) for the window and define one callback function


# wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
