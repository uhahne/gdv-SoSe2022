import cv2
import copy

# loading images in grey and color
img_gray = cv2.imread('images/logo.png', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('images/logo.png', cv2.IMREAD_COLOR)

# do some print out about the loaded data
print(type(img_gray))  # prints class numpy.ndarray
print(type(img_color))  # prints class numpy.ndarray

print(img_gray.shape)  # prints the size of the image array
print(img_color.shape)  # prints the size of the image array

# Continue with the color image
# img = imgColor

# Continue with the grayscale image
# img = img_gray
# copy the original image --> see https://docs.python.org/3/library/copy.html
img = copy.copy(img_gray)

# Extract the size or resolution of the image
height = img.shape[0]
width = img.shape[1]
print('height = ' + str(img.shape[0]))
print('width = ' + str(img.shape[1]))

# resize image
# new_width = 7
# new_height = 5
# new_size = (new_width, new_height)
# img = cv2.resize(img, new_size)

# row and column access, see
#   https://numpy.org/doc/stable/reference/arrays.ndarray.html
#   for general access on ndarrays
# print first row
# print (img[0])
# print first column
# print (img[:,0])

# set area of the image to black
# for i in range (30):
#     for j in range (width):
#         img[i][j] = [0,0,0]

# find all used colors in the image
colors = []
for i in range(height):
    for j in range(width):
        curr_color = img[i, j]
        if colors.count(curr_color) == 0:
            colors.append(curr_color)
print('Those gray values are in the image:\n ' + str(colors))

# copy one part of an image into another one
letters = img[30:105, 5:130]
img[115:190, 150:275] = letters

# save image
cv2.imwrite('img_tutorial02.jpg', img)

# show the image
title = 'OpenCV Python Tutorial'
# Note that window parameters have no effect on MacOS
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# show the original image (copy demo)
title = 'How a copy works'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
