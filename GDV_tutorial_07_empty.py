import cv2
import numpy as np

# Goal: Count the number of green smarties in the images
# define green in HSV
hue = 60  # 60 is pure green
hue_range = 10
saturation = 155
saturation_range = 100
value = 155
value_range = 100
lower_green = np.array([hue - hue_range, saturation -
                       saturation_range, value - value_range])
upper_green = np.array([hue + hue_range, saturation +
                       saturation_range, value + value_range])

# load image
img = cv2.imread('images\\smarties01.JPG', cv2.IMREAD_COLOR)
img = cv2.resize(img, (800, 600))

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# create a mask
mask = cv2.inRange(hsv, lower_green, upper_green)

# morphological operations code

# find connected components

# find center of mass and draw a mark in the original image

# go through all (reasonable) found connected components

# check size and roundness as plausibility

# find and draw center

# find and draw bounding box

# print out number of connected components
print('We have found x green smarties.')


# show the original image with drawings in one window
cv2.imshow('Original image', img)
# show the masked image in another window

# show the mask image in another window
cv2.imshow('Mask image', mask)
# cv2.imwrite('mask.jpg',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
