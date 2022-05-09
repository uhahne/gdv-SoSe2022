# Inspired by https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
import numpy as np
import cv2

# define global arrays for the clicked (reference) points
ref_pt_src = []
ref_pt_dst = []


# TODO define one callback functions for each image window
def clickSrc(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt_src
    # if the left mouse button was clicked, add the point to the source array
    
        # draw a circle around the clicked point
        
        # redraw the image


def clickDst(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt_dst
    # if the left mouse button was clicked, add the point to the source array
   
        # draw a circle around the clicked point
        
        # redraw the image


# Load image and resize for better display
img = cv2.imread('images\\nl_clown.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)

# TODO initialize needed variables and windows including mouse callbacks


# keep looping until the 'q' key is pressed
computationDone = False
while True:
    # TODO if there are three reference points, then compute the transform and apply the transformation
    if not(computationDone):
            
    # TODO display the image and wait for a keypress
       
    # TODO if the 'r' key is pressed, reset the transformation
   
        
    # TODO if the 'q' key is pressed, break from the loop
    

cv2.destroyAllWindows()
