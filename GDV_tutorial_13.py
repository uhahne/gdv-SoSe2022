# Inspired by https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
import numpy as np
import cv2

refPtSrc = []
refPtDst = []


def clickSrc(event, x, y, flags, param):
    # grab references to the global variables
    global refPtSrc
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(refPtSrc)
        if (pos == 0):
            refPtSrc = [(x, y)]
        else:
            refPtSrc.append((x, y))
        # draw a circle at the clicked position
        cv2.circle(img, refPtSrc[pos], 4, (0, 255, 0), 2)
        cv2.imshow('Original', img)


def clickDst(event, x, y, flags, param):
    # grab references to the global variables
    global refPtDst
    # if the left mouse button was clicked,
    # add the point to the destination array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(refPtDst)
        if (pos == 0):
            refPtDst = [(x, y)]
        else:
            refPtDst.append((x, y))
        # draw a circle at the clicked position
        cv2.circle(dst_transform, refPtDst[pos], 4, (0, 255, 0), 2)
        cv2.imshow('Transformed image', dst_transform)


# Load image and resize for better display
img = cv2.imread('images\\nl_clown.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
rows, cols, dim = img.shape
clone = img.copy()
dst_transform = np.zeros(img.shape, np.uint8)
cv2.namedWindow('Original')
cv2.setMouseCallback('Original', clickSrc)
cv2.namedWindow('Transformed image')
cv2.setMouseCallback('Transformed image', clickDst)

computationDone = False
# keep looping until the 'q' key is pressed
while True:
    # if there are four reference points,
    # then compute the transform and apply the transformation
    if not(computationDone) and (len(refPtSrc) == 4 and len(refPtDst) == 4):
        T_perspective = cv2.getPerspectiveTransform(np.float32(
            refPtSrc), np.float32(refPtDst), solveMethod=cv2.DECOMP_SVD)
        print('\nProjective transform:\n', '\n'.join(
            ['\t'.join(['%03.3f' % cell for cell in row])
             for row in T_perspective]))
        dst_transform = cv2.warpPerspective(img, T_perspective, (cols, rows))
        computationDone = True

    # display the image and wait for a keypress
    cv2.imshow('Original', img)
    cv2.imshow('Transformed image', dst_transform)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the transformation
    if key == ord("r"):
        dst_transform = np.zeros(img.shape, np.uint8)
        img = clone.copy()
        refPtSrc = []
        refPtDst = []
        computationDone = False
    # if the 'q' key is pressed, break from the loop
    elif key == ord("q"):
        break

cv2.destroyAllWindows()
