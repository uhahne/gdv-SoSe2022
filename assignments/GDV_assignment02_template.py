'''
Assignement 02: Object counting
Group: <Your group>
Names: <Your names>
Date: <Date of last changes>
Sources: <Sources of inspiration and collaboration (persons, videos, web pages, documents, books, ...)>
'''

import cv2
import glob # for loading all images from a directory

### Goal: Count the number of all colored balls in the images

# ground truth
num_yellow = 30
num_blue = 5
num_pink = 8
num_white = 10
num_green = 2
num_red = 6
gt_list = (num_red, num_green, num_blue, num_yellow, num_white, num_pink)

# define color ranges in HSV, note that OpenCV uses the following ranges H: 0-179, S: 0-255, V: 0-255 

# red


# green

# blue

# yellow

# white

# pink

### morphological operations
# optional mapping of values with morphological shapes
def morph_shape(val):
    if val == 0:
        return cv2.MORPH_RECT
    elif val == 1:
        return cv2.MORPH_CROSS
    elif val == 2:
        return cv2.MORPH_ELLIPSE

# dilation with parameters
def dilatation(img,size,shape): 
    element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                       (size, size))
    return cv2.dilate(img, element)

# erosion with parameters
def erosion(img,size,shape): 
    element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                       (size, size))
    return cv2.erode(img, element)

# opening
def opening(img,size,shape): 
    element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                       (size, size))
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, element)

# closing
def closing(img,size,shape): 
    element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                       (size, size))
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, element)

# set color under test
num_colors = 6
color_names = ['red', 'green', 'blue', 'yellow', 'white','pink']


# setting the parameters that work for all colors

# set individual (per color) parameters

num_test_images_succeeded = 0
for img_name in glob.glob('images/chewing_gum_balls*.jpg'): 
    # load image
    print ('Searching for colored balls in image:',img_name)

    all_colors_correct = True

    for c in range(0,num_colors):
        
        img = cv2.imread(img_name,cv2.IMREAD_COLOR)
        height = img.shape[0]
        width = img.shape[1]

        # TODO: Insert your algorithm here

        num_labels = 0 # TODO: implement something to set this variable
        num_rejected = 1
        num_final_labels = num_labels-num_rejected

        success = (num_final_labels == int(gt_list[c]))
        
        if success:
            print('We have found all', str(num_final_labels),'/',str(gt_list[c]), color_names[c],'chewing gum balls. Yeah!')
            foo = 0
        elif (num_final_labels > int(gt_list[c])):
            print('We have found too many (', str(num_final_labels),'/',str(gt_list[c]),') candidates for', color_names[c],'chewing gum balls. Damn!')
            all_colors_correct = False
        else:
            print('We have not found enough (', str(num_final_labels),'/',str(gt_list[c]),') candidates for', color_names[c],'chewing gum balls. Damn!')
            all_colors_correct = False
        
        # debug output of the test images
        if ((img_name == 'images\chewing_gum_balls01.jpg') 
            or (img_name == 'images\chewing_gum_balls04.jpg') 
            or (img_name == 'images\chewing_gum_balls06.jpg')):
            # show the original image with drawings in one window
            cv2.imshow('Original image', img)
            # show other images?

            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
    if all_colors_correct:
        num_test_images_succeeded += 1
        print ('Yeah, all colored objects have been found correctly in ',img_name)

print ('Test result:', str(num_test_images_succeeded),'test images succeeded.')

        
