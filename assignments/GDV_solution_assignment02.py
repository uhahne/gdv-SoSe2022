import cv2
import numpy as np
import glob # for loading all images from a directory

### Goal: Count the number of all colored balls in the images

# ground truth
numYellow = 30
numBlue = 5
numPink = 8
numWhite = 10
numGreen = 2
numRed = 6
gtList = (numRed, numGreen, numBlue, numYellow, numWhite, numPink)

# define color ranges in HSV, note that OpenCV uses the following ranges H: 0-179, S: 0-255, V: 0-255 
hue_range = 10
saturation = 155
saturation_range = 100
value = 155
value_range = 100

# red
lower_red = np.array([160,145,value - value_range])
upper_red = np.array([180,255,value + value_range])
lower_red2 = np.array([0,145 ,value - value_range])
upper_red2 = np.array([10,255,value + value_range])

# green
lower_green = np.array([45 - hue_range,saturation - saturation_range,value - value_range])
upper_green = np.array([45 + hue_range,saturation + saturation_range,value + value_range])

# blue
lower_blue = np.array([100 - hue_range,saturation - saturation_range,value - value_range])
upper_blue = np.array([100 + hue_range,saturation + saturation_range,value + value_range])

# yellow
lower_yellow = np.array([30 - hue_range,saturation - saturation_range,value - value_range])
upper_yellow = np.array([30 + hue_range,saturation + saturation_range,value + value_range])

# white
lower_white = np.array([0,0,240])
upper_white = np.array([255,90,255])

# pink
lower_pink = np.array([0, 0,150])
upper_pink = np.array([12,145,255])

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
numColors = 6
colorNames = ['red', 'green', 'blue', 'yellow', 'white','pink']
lower_colors = [lower_red,lower_green,lower_blue,lower_yellow,lower_white, lower_pink]
upper_colors = [upper_red,upper_green,upper_blue,upper_yellow,upper_white, upper_pink]


# setting the parameters that work for all colors
kernel_shape = morph_shape(2)


# set individual parameters
dilation_needed = [False, False, False, False, False, False]
erosion_needed  = [False, False, False, True , True , False]
opening_needed  = [True , True , True , True , True , True ]
closing_needed  = [False, False, False, False, False, False]
kernel_size =     [7    , 7    , 3    , 3    , 3    , 7    ]
min_size        = [7    , 4    , 4    , 4    , 17   , 4    ]

num_test_images_succeeded = 0
for img_name in glob.glob('images/chewing_gum_balls*.jpg'): 
    # load image
    print ('Searching for colored balls in image:',img_name)

    allColorsCorrect = True

    for c in range(0,numColors):
        lower_color = lower_colors[c]
        upper_color = upper_colors[c]
    
        img = cv2.imread(img_name,cv2.IMREAD_COLOR)
        #img = cv2.resize(img,(60,80))
        height = img.shape[0]
        width = img.shape[1]

        # convert to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # DEBUG: find all used colors in the image
        #all_hsv_codes = hsv.reshape(-1, hsv.shape[-1])
        #print(np.unique(all_hsv_codes, axis=0, return_counts = True))

        # create a mask
        mask = cv2.inRange(hsv, lower_color, upper_color)
        if (colorNames[c] == 'red'):
            # DEBUG: print ('Hello Red!')
            mask2 = cv2.inRange(hsv,lower_red2,upper_red2)
            mask = cv2.bitwise_or(mask,mask2) 
            
        if (dilation_needed[c]):
            mask = dilatation(mask,kernel_size[c],kernel_shape)
        if (erosion_needed[c]):
            mask = erosion(mask,kernel_size[c],kernel_shape)
        if (opening_needed[c]):   
            mask = opening(mask,kernel_size[c],kernel_shape)
        if (closing_needed[c]):
            mask = closing(mask,kernel_size[c],kernel_shape)

        # mask out green parts as binary image
        result = cv2.bitwise_and(img, img, mask=mask)

        # find connected components
        # apply connected component analysis to the thresholded image
        connectivity = 4
        (numLabels, labels, stats, centroids) = cv2.connectedComponentsWithStats(mask, connectivity, cv2.CV_32S)

        # print out number of connected components and be aware that The first connected component, with an ID of 0
        # is always the background. We typically ignore the background, but if you ever need it, keep in mind that ID 0
        # contains it.
        #print('We have found ', str(numLabels-1),'/',str(gtList[c]), colorNames[c],'chewing gum balls.')

        # find center of mass and draw a mark in the original image
        red_BGR = (0,0,255)
        circle_size = 10
        circle_thickness = 5
        

        # go through all (reasonable) found connected components
        numFinalLabels = numLabels
        for i in range(1,numLabels):
            # check size and roundness as plausibility
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            if w < min_size[c] or h < min_size[c]:
                print ('Found a too small component.')
                numFinalLabels -= 1
                continue # found component is too small to be correct 
            roundness = 1.0
            if w > h:
                roundness = 1.0 / (w/h)
            elif h > w:
                roundness = 1.0 / (h/w)  
            if (roundness > 2):
                print ('Found a component that is not round enough.')
                numFinalLabels -= 1
                continue # ratio of width and height is not suitable

            # find and draw center
            center = centroids[i]
            center = np.round(center)
            center = center.astype(int)
            cv2.circle(img,center,circle_size,red_BGR,circle_thickness)
            # find and draw bounding box
            
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

        success = (numFinalLabels-1 == int(gtList[c]))
        
        if success:
            #print('We have found all', str(numFinalLabels-1),'/',str(gtList[c]), colorNames[c],'chewing gum balls. Yeah!')
            foo = 0
        elif (numFinalLabels-1 > int(gtList[c])):
            print('We have found too many (', str(numFinalLabels-1),'/',str(gtList[c]),') candidates for', colorNames[c],'chewing gum balls. Damn!')
            allColorsCorrect = False
        else:
            print('We have not found enough (', str(numFinalLabels-1),'/',str(gtList[c]),') candidates for', colorNames[c],'chewing gum balls. Damn!')
            allColorsCorrect = False
        
        if ((img_name == 'images\chewing_gum_balls01.jpg') 
            or (img_name == 'images\chewing_gum_balls04.jpg') 
            or (img_name == 'images\chewing_gum_balls06.jpg')):
            # show the original image with drawings in one window
            cv2.imshow('Original image', img)
            # show the masked image in another window
            cv2.imshow('Masked image', result)
            # show the mask image in another window
            cv2.imshow('Mask image', mask)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
    if allColorsCorrect:
        num_test_images_succeeded += 1
        print ('Yeah, all colored objects have been found correctly in ',img_name)

print ('Test result:', str(num_test_images_succeeded),'test images succeeded.')

        
