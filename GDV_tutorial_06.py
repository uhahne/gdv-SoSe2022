import numpy as np
import cv2

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

blue = (255, 0, 0)
red = (0, 0, 255)
green = (20, 200, 20)
black = (0, 0, 0)

font_size_large = 3
font_size_small = 1
font_size_smaller = .6
font = cv2.FONT_HERSHEY_SIMPLEX

# exemplary color conversion (only for the class)
BGR_blue_img = np.zeros((1, 1, 3), np.uint8)
BGR_blue_img[0][0] = (255, 0, 0)
print('Blue in BGR and HSV:')
print(BGR_blue_img)
print(cv2.cvtColor(BGR_blue_img, cv2.COLOR_BGR2HSV))

BGR_red_img = np.zeros((1, 1, 3), np.uint8)
BGR_red_img[0][0] = (0, 0, 255)
print('Red in BGR and HSV:')
print(BGR_red_img)
print(cv2.cvtColor(BGR_red_img, cv2.COLOR_BGR2HSV))

BGR_green_img = np.zeros((1, 1, 3), np.uint8)
BGR_green_img[0][0] = (0, 255, 0)
print('Green in BGR and HSV:')
print(BGR_green_img)
print(cv2.cvtColor(BGR_green_img, cv2.COLOR_BGR2HSV))

# color ranges, default values
hue = 120
hue_range = 10
saturation = 200
saturation_range = 100
value = 200
value_range = 100


# implement the callback to pick the color on double click
def color_picker(event, x, y, flags, param):
    global hue, saturation, value
    if event == cv2.EVENT_LBUTTONDBLCLK:
        (h, s, v) = hsv[y, x]
        hue = int(h)
        saturation = int(s)
        value = int(v)
        print('New color selected:', (hue, saturation, value))


while True:
    # get video frame (always BGR format!)
    ret, frame = cap.read()
    if (ret):
        # copy image to draw on
        img = frame.copy()

        # draw arrows
        img = cv2.arrowedLine(img, (10, 10), (100, 10), blue, thin)
        img = cv2.putText(img, 'X', (115, 25), font,
                          font_size_small, blue, thin)
        img = cv2.arrowedLine(img, (10, 10), (10, 100), blue, thin)
        img = cv2.putText(img, 'Y', (5, 130), font,
                          font_size_small, blue, thin)

        # computing color ranges for display
        lower_blue = np.array([hue - hue_range,
                               saturation - saturation_range,
                               value - value_range])
        upper_blue = np.array([hue + hue_range,
                               saturation + saturation_range,
                               value + value_range])
        HSV_blue_img = np.zeros((1, 1, 3), np.uint8)
        HSV_blue_img[0, 0] = (hue, saturation, value)
        medium_blue_array = cv2.cvtColor(HSV_blue_img, cv2.COLOR_HSV2BGR)[0, 0]
        blue_BGR = (int(medium_blue_array[0]), int(
            medium_blue_array[1]), int(medium_blue_array[2]))

        # draw selection color circle
        img = cv2.circle(img, (width - 50, height - 50), 30, blue_BGR, -1)
        img = cv2.putText(img, 'H = ' + str(hue),
                          (width - 200, height - 75),
                          font, font_size_smaller, blue, thinner)
        img = cv2.putText(img, 'S = ' + str(saturation),
                          (width - 200, height - 50),
                          font, font_size_smaller, blue, thinner)
        img = cv2.putText(img, 'V = ' + str(value), (width - 200,
                          height - 25), font, font_size_smaller, blue, thinner)

        # convert to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # create a mask
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # apply mask
        result = cv2.bitwise_and(img, img, mask=mask)

        # show the original image with drawings in one window
        title = 'Original image'
        cv2.namedWindow(title)
        cv2.setMouseCallback(title, color_picker)
        cv2.imshow(title, img)
        # show the masked image in another window
        cv2.imshow('Masked image', result)
        # show the mask image in another window
        cv2.imshow('Mask image', mask)

        # deal with keyboard input
        key = cv2.waitKey(10)
        if key == ord('q'):
            break
        if key == ord('h'):
            hue -= 1
        if key == ord('H'):
            hue += 1
        if key == ord('s'):
            saturation -= 1
        if key == ord('S'):
            saturation += 1
        if key == ord('v'):
            value -= 1
        if key == ord('V'):
            value += 1
    else:
        print('Could not start video camera')
        break

cap.release()
cv2.destroyAllWindows()
