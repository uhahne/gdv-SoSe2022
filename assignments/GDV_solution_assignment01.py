import cv2
import copy
import numpy as np

# backup helper method
def getNewDimensions(img, scale_percent):
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        return dim

use_backup = False

### Create an image with a color gradient
# define the dimension
height = 600
width = 1200
# create a line with increasing values
gradient_line = np.linspace(0,255, width)
# round the values to integers
np.round(gradient_line)
# repeat the lines
gradient_image = np.repeat(gradient_line, height)
# reshape the repeated lines into a matrix
gradient_image = np.reshape(gradient_image, (height, width), 'F')
# convert to a grayscale (uint8) image
img_background = gradient_image.astype(np.uint8)

if use_backup:
    # backup solution: load gradient image
    img_background = cv2.imread('images/gradation01L.jpg', cv2.IMREAD_GRAYSCALE)
    # resize image (only if large backup image had been loaded)
    scaling = 25 # percent of original size
    img_background = cv2.resize(img_background, getNewDimensions(img_background,scaling), cv2.INTER_AREA)
    # Extract the new size of the image
    height = img_background.shape[0]
    width = img_background.shape[1]

# Cut s small square image from the middle of the background image
square_size = 100
half_height = int(height/2)
half_width = int(width/2)
img_square = img_background[half_height:half_height+square_size,half_width:half_width+square_size]

# Some debug printouts to check if image sizes are correct
print ('Background image size:' + str(img_background.shape)) # prints the size of the image array 
print ('Square image size:' + str(img_square.shape)) # prints the size of the image array

# Show the image
title = 'OpenCV Python Tutorial 02 Illusion'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE) # Note that window parameters have no effect on MacOS

# Define animation/recording speed and other settings
do_write_video = False
step = 2
delay_in_ms = 10
extra_delay = 500
border_offset = 20

# Draw the square on top left and right for comparison
img_background[border_offset:border_offset+square_size,border_offset:border_offset+square_size] = img_square
img_background[border_offset:border_offset+square_size,width - (square_size + border_offset):width - border_offset] = img_square

# Create the `VideoWriter()` object
if do_write_video:
    out = cv2.VideoWriter('video_illusion.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, 
        (width, height))

# Repeat until q key pressed
stop = False
while not(stop):
    # move the square from left to right
    for pos_x in range(border_offset,width-border_offset-square_size, step):
        # copy the original image --> see https://docs.python.org/3/library/copy.html
        img = copy.copy(img_background)
        # let the small square move from left to right in the middle of the image     
        img[half_height:half_height+square_size,pos_x:pos_x+square_size] = img_square

        cv2.imshow(title, img)

        # debug print
        # print(pos_x)

        # make a pause at the left position
        if pos_x == border_offset:
            print ('waiting left: square appears bright')
            cv2.waitKey(extra_delay)

        # make a longer pause at the original cut position
        if ((pos_x > half_width - step/2) and (pos_x < half_width + step/2)) :
            print ('waiting middle: square has vanished')
            cv2.waitKey(4*extra_delay)

        # make a pause at the right position
        if pos_x > width - border_offset - square_size - step:
            print ('waiting right: square appears dark')
            cv2.waitKey(extra_delay)
        
        if do_write_video:
            if img.ndim == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            out.write(img)

        if cv2.waitKey(delay_in_ms) == ord('q'):
            stop = True # to end the while loop
            break # break the for loop
    # do not loop if video recording is active
    if do_write_video:
        stop = True # to end the while loop

# Close all windows at the end
cv2.destroyAllWindows()