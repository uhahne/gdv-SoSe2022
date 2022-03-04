# first step is to import the opencv module which is called 'cv2'
import cv2

# check the opencv version
print(cv2.__version__)

# load an image with image reading modes using 'imread'
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.
img = cv2.imread('images/logo.png', cv2.IMREAD_COLOR)

# resize image with 'resize'
new_width = 640
new_height = 480
new_size = (new_width, new_height)
img = cv2.resize(img, new_size)

# rotate image (but keep it rectangular) with 'rotate'
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# save image with 'imwrite'
cv2.imwrite('img_tutorial01.jpg', img)

# show the image with 'imshow'
title = 'OpenCV Python Tutorial'
# Note that window parameters have no effect on MacOS
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
