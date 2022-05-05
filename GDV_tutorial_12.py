# Inspired by https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
import numpy as np
import cv2

# define global arrays for the clicked (reference) points
ref_pt_src = []
ref_pt_dst = []


def click_src(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt_src
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(ref_pt_src)
        if (pos == 0):
            ref_pt_src = [(x, y)]
        else:
            ref_pt_src.append((x, y))
        # draw a circle around the clicked point
        cv2.circle(img, ref_pt_src[pos], 4, (0, 255, 0), 2)
        cv2.imshow('Original', img)


def click_dst(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt_dst
    # if the left mouse button was clicked, add the point to the destination array
    if event == cv2.EVENT_LBUTTONDOWN:
        pos = len(ref_pt_dst)
        if (pos == 0):
            ref_pt_dst = [(x, y)]
        else:
            ref_pt_dst.append((x, y))
        # draw a circle around the clicked point
        cv2.circle(dst_transform, ref_pt_dst[pos], 4, (0, 255, 0), 2)
        cv2.imshow('Transformed image', dst_transform)


# Load image and resize for better display
img = cv2.imread('images\\nl_clown.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)

# initialize needed variables and windows
rows, cols, dim = img.shape
clone = img.copy()
dst_transform = np.zeros(img.shape, np.uint8)
cv2.namedWindow('Original')
cv2.setMouseCallback('Original', click_src)
cv2.namedWindow('Transformed image')
cv2.setMouseCallback('Transformed image', click_dst)


# keep looping until the 'q' key is pressed
computationDone = False
while True:
    # if there are three reference points, then compute the transform and apply the transformation
    if not(computationDone) and (len(ref_pt_src) == 3 and len(ref_pt_dst) == 3):
        T_affine = cv2.getAffineTransform(np.float32(ref_pt_src), np.float32(ref_pt_dst))
        print('\nAffine transformation:\n', '\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_affine]))
        dst_transform = cv2.warpAffine(img, T_affine, (cols, rows))
        computationDone = True

    # display the image and wait for a keypress
    cv2.imshow('Original', img)
    cv2.imshow('Transformed image', dst_transform)
    key = cv2.waitKey(10)

    # if the 'r' key is pressed, reset the transformation
    if key == ord("r"):
        dst_transform = np.zeros(img.shape, np.uint8)
        img = clone.copy()
        ref_pt_src = []
        ref_pt_dst = []
        computationDone = False
    # if the 'q' key is pressed, break from the loop
    elif key == ord("q"):
        break

cv2.destroyAllWindows()
