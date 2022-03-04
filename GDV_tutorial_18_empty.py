# inspired from https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html
import cv2
import numpy as np

''' Initialize images '''
# load object image as color image
img_object = cv2.imread('images\\sift_object01.jpg', cv2.IMREAD_COLOR)
# extract shape of the image
rows_obj, cols_obj, dims_obj = img_object.shape
# create a greyscale image for the corner detection
img_obj_gray = cv2.cvtColor(img_object, cv2.COLOR_BGR2GRAY)
# create a window and show loaded image
window_object = 'Object image'
cv2.namedWindow(window_object, cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow(window_object, cols_obj, rows_obj)
cv2.imshow(window_object, img_object)

# load table image as color image
img_table = cv2.imread('images\\sift_table01.jpg', cv2.IMREAD_COLOR)
# extract shape of the image
rows_table, cols_table, dims_table = img_object.shape
# create a greyscale image for the corner detection
img_table_gray = cv2.cvtColor(img_table, cv2.COLOR_BGR2GRAY)
# create a window and show loaded image
window_table = 'Table image'
cv2.namedWindow(window_table, cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow(window_object, cols_table, rows_table)
cv2.imshow(window_table, img_table)
print('Loading images done.')
# wait until key pressed
cv2.waitKey(0)

''' do the feature detection with SIFT '''
# TODO: Create a SIFT detector for 500 features (see https://docs.opencv.org/4.5.3/d7/d60/classcv_1_1SIFT.html#ad337517bfdc068ae0ba0924ff1661131)


# Detect features and compute descriptors in both images
keypoints_obj, descriptors_obj = ??
keypoints_table, descriptors_table = ??

# TODO: Draw detected feature points in both images and show them 
# see (https://docs.opencv.org/4.5.3/d4/d5d/group__features2d__draw.html#ga5d2bafe8c1c45289bc3403a40fb88920)


cv2.imshow(window_object, img_object)
cv2.imshow(window_table, img_table)
print('Feature detection done.')
cv2.waitKey(0)

''' do the feature matching with a brute force matcher '''
# TODO: Initialize and run BFMatcher with default params (see https://docs.opencv.org/4.5.3/d3/da1/classcv_1_1BFMatcher.html#abe0bb11749b30d97f60d6ade665617bd)


# store all the good matches as per Lowe's ratio test.
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# TODO: Draw matches with cv2.drawMatchesKnn 
img_matching = cv2.drawMatchesKnn...
window_matching = 'Matching'
cv2.namedWindow(window_matching)
cv2.resizeWindow(window_matching, img_matching.shape[0], img_matching.shape[1])
cv2.imshow(window_matching, img_matching)
print('Matching images done.')
cv2.waitKey(0)

''' Compute and visualize the homography based on the matching '''
# check if there are enough good matches
MIN_MATCH_COUNT = 10
RANSAC_REPROJECTION_THRESHOLD = 3.0
if len(good) > MIN_MATCH_COUNT:
    # extract coordinates from the keypoints
    src_pts = np.float32(
        [keypoints_obj[m[0].queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32(
        [keypoints_table[m[0].trainIdx].pt for m in good]).reshape(-1, 1, 2)
    # TODO: find the homography with RANSAC (see https://docs.opencv.org/4.5.3/d9/d0c/group__calib3d.html#ga4abc2ece9fab9398f2e560d53c8c9780)

    print('\nTransformation matrix\n', '\n'.join(['\t'.join(
        ['%03.3f' % cell for cell in row]) for row in M]))
    # TODO: draw the outline of the object into the table image
    h, w, d = img_object.shape
    # Step 1: take the image corners of the object image
    
    # Step 2: transform the corners with the found homography
    
    # Step 3: draw the outline with polylines
    
else:
    print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
    mask = None

# TODO: draw only the good matches in green using drawMatchesKnn with matchColor and matchesMask


cv2.imshow(window_matching, img_matching)
print('Homography computation done.')
cv2.waitKey(0)
cv2.destroyAllWindows()
