import cv2
import numpy as np

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()


def detectDrawAndShowBlobs(img):
    # determine the used global variables
    global params, window_name

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # create a greyscale image for the corner detection
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect blobs
    keypoints = detector.detect(img_gray)

    # use an image clone to for drawing
    img_clone = np.copy(img)

    # Draw detected blobs as blue circles
    # Note that cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size
    # of the circle corresponds to the size of blob.
    img_clone = cv2.drawKeypoints(img_clone, keypoints,
                                  np.array([]), (255, 0, 0),
                                  cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # display the image
    cv2.imshow(window_name, img_clone)


# define the callback function
def on_change(val):
    global params, img

    # Change thresholds
    params.minThreshold = cv2.getTrackbarPos('minThreshold', window_name)
    params.maxThreshold = cv2.getTrackbarPos('maxThreshold', window_name)

    # Filter by Area.
    filter_area_val = cv2.getTrackbarPos('minArea', window_name)
    if filter_area_val > 0:
        params.filterByArea = True
    else:
        params.filterByArea = False
    params.minArea = filter_area_val

    # Filter by Circularity
    filter_circularity_val = cv2.getTrackbarPos(
        'minCircularity (in %%)', window_name)
    if filter_circularity_val > 0:
        params.filterByCircularity = True
    else:
        params.filterByCircularity = False
    params.minCircularity = filter_circularity_val/100.0

    # Filter by Convexity
    filter_convexity_val = cv2.getTrackbarPos('minConvexity (in %%)',
                                              window_name)
    if filter_convexity_val > 0:
        params.filterByConvexity = True
    else:
        params.filterByConvexity = False
    params.minConvexity = filter_convexity_val/100.0

    # Filter by Inertia
    filter_inertia_val = cv2.getTrackbarPos('minInertiaRatio (in %%)',
                                            window_name)
    if filter_inertia_val > 0:
        params.filterByInertia = True
    else:
        params.filterByInertia = False
    params.minInertiaRatio = filter_inertia_val/100.0

    detectDrawAndShowBlobs(img)


# load example image as color image
img = cv2.imread('images\\blobtest.jpg', cv2.IMREAD_COLOR)

# create a window with sliders and show resulting image
window_name = 'Blob detection demo'
cv2.namedWindow(window_name, cv2.WINDOW_GUI_EXPANDED)

# create sliders for all parameters and one callback function
cv2.createTrackbar('minArea', window_name, 0, 2500, on_change)
cv2.createTrackbar('minThreshold', window_name, 10, 255, on_change)
cv2.createTrackbar('maxThreshold', window_name, 200, 255, on_change)
cv2.createTrackbar('minCircularity (in %%)', window_name, 0, 100, on_change)
cv2.createTrackbar('minInertiaRatio (in %%)', window_name, 0, 100, on_change)
cv2.createTrackbar('minConvexity (in %%)', window_name, 0, 100, on_change)

# detect, draw and show blobs
detectDrawAndShowBlobs(img)

# wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
