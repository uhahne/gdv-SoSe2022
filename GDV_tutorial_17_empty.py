# The following OpenCV functions are meant to be used in this tutorial
# SimpleBlobDetector (with params) see https://docs.opencv.org/3.4/d0/d7a/classcv_1_1SimpleBlobDetector.html#details 
# drawKeypoints see https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html#gab958f8900dd10f14316521c149a60433 


import cv2
import numpy as np

# TODO: Setup SimpleBlobDetector parameters

# TODO: Define a function to detect blobs, draw them and display the image
    # determine the used global variables
    
    # Create a detector with the parameters
    
    # create a greyscale image for the corner detection
    
    # Detect blobs
    
    # use an image clone to for drawing
    
    # Draw detected blobs as blue circles
    # Note that cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size
    # of the circle corresponds to the size of blob.
                                  
    # display the image

# TODO: Define the callback function

    # provide access to the global blob detector parameters
    
    # use an image clone to for drawing

    # TODO: Filter by area
    
    # TODO: Change threshold parameters

    # TODO: Filter by circularity

    # TODO: Filter by inertia
    
    # TODO: Filter by convexity

    # call the detect, draw and show function



# load example image as color image
img = cv2.imread('images\\blobtest.jpg', cv2.IMREAD_COLOR)

# TODO: Create a window with sliders and show resulting image

# HINT: Create sliders for all parameters using only one callback function

# TODO: call the detect, draw and show function


# TODO: wait until a key is pressed and end the application

