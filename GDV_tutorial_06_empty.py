import numpy as np
import cv2
import copy

# print keyboard usage
print('This is a HSV color detection demo. Use the keys to adjust the \
selection color in HSV space. Circle in bottom left.')
print('The masked image shows only the pixels with the given HSV color within \
a given range.')
print('Use h/H to de-/increase the hue.')
print('Use s/S to de-/increase the saturation.')
print('Use v/V to de-/increase the (brightness) value.\n')

# capture webcam image
cap = cv2.VideoCapture(0)

# get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))
print('Video properties:')
print('  Width = ' + str(width))
print('  Height = ' + str(height))
print('  Codec = ' + str(codec))

# drawing helper variables
thick = 10
thin = 3
thinner = 2
font_size_large = 3
font_size_small = 1
font_size_smaller = .6
font = cv2.FONT_HERSHEY_SIMPLEX


# TODO: define  RGB colors as variables


# exemplary color conversion (only for the class), tests usage of cv2.cvtColor

# color ranges, enter found default values and uncomment
# hue =
hue_range = 10
# saturation =
saturation_range = 100
# value =
value_range = 100

while True:
    # get video frame (always BGR format!)
    ret, frame = cap.read()
    if (ret):
        # copy image to draw on
        img = copy.copy(frame)

        # draw arrows (coordinate system)

        # computing color ranges for display

        # draw selection color circle and text for HSV values

        # convert to HSV

        # create a bitwise mask

        # apply mask

        # show the original image with drawings in one window

        # show the masked image in another window

        # show the mask image in another window

        # deal with keyboard input

    else:
        print('Could not start video camera')
        break

cap.release()
cv2.destroyAllWindows()
