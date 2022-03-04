# Template matching, originally with objects from the image. Typical example
# is counting blood cells
import cv2

use_color = True

if use_color:
    # load image and template image, note that the template has been manually
    # cut out of the image

    # read shape of the template and original image

else:
    # load image and template image, note that the template has been manually
    # cut out of the image

    # read shape of the template and original image

    # Define template matching methods,
    # see https://docs.opencv.org/4.5.3/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d for the math behind each method

    # loop over all methods in order to compare them

    # work on a new image each time

    # do the template matching

    # get the best match location

    # draw rectangle at found location

    # show original image with found location

    # show image with the template matching result for all pixels

    cv2.waitKey(0)

cv2.destroyAllWindows()
