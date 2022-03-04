''' This code is based on the stackoverflow answer from Fred Weinhaus: https://stackoverflow.com/a/59995542  '''
import cv2
import numpy as np

# global helper variables
window_width = 640
window_height = 480

# def getFrequencies(image):
# convert image to floats and do dft saving as complex output

# apply shift of origin from upper left corner to center of image

# extract magnitude and phase images

# get spectrum for viewing only

# Return the resulting image (as well as the magnitude and phase for the inverse)


# def createFromSpectrum():
# convert magnitude and phase into cartesian real and imaginary components

# combine cartesian components into one complex image

# shift origin from center to upper left corner

# do idft saving as complex output

# combine complex components into original image again

# re-normalize to 8-bits


def main():
    """ Load an image, compute frequency domain image from it and display both or vice versa """
    image_name = 'images\chewing_gum_balls01.jpg'

    # Load the image.
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (window_width, window_height))

    # show the original image
    title_original = 'Original image'
    # Note that window parameters have no effect on MacOS
    cv2.namedWindow(title_original, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_original, window_width, window_height)
    cv2.imshow(title_original, image)

    #result = getFrequencies(image)
    result = np.zeros((window_height, window_width), np.uint8)

    # show the resulting image
    title_result = 'Frequencies image'
    # Note that window parameters have no effect on MacOS
    cv2.namedWindow(title_result, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_result, window_width, window_height)
    cv2.imshow(title_result, result)

    # back = createFromSpectrum(??)
    back = np.zeros((window_height, window_width), np.uint8)

    # and compute image back from frequencies
    title_back = 'Reconstructed image'
    # Note that window parameters have no effect on MacOS
    cv2.namedWindow(title_back, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_back, window_width, window_height)
    cv2.imshow(title_back, back)

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()


if (__name__ == '__main__'):
    main()
