import numpy as np
import cv2

# open a video file
file = 'videos/hello_UH.m4v'
cap = cv2.VideoCapture(file)

# get camera image parameters from get()
width = int(cap.get(cv2.cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT))
count = int(cap.get(cv2.cv2.CAP_PROP_FRAME_COUNT))
print('Video properties:')
print('  Width = ' + str(width))
print('  Height = ' + str(height))
print('  Frame count = ' + str(count))

# start a loop
while True:
    # read one video frame
    ret, frame = cap.read()

    if (ret):
        # create four tiles of the image
        img = np.zeros(frame.shape, np.uint8)
        smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        img[:height//2, :width//2] = smaller_frame  # top left (original)
        # bottom left flipped horizontally
        img[height//2:, :width//2] = cv2.flip(smaller_frame, 0)
        # bottom left flipped both horizontally and vertically
        img[height//2:, width//2:] = cv2.flip(smaller_frame, -1)
        # top right flipped vertically
        img[:height//2, width//2:] = cv2.flip(smaller_frame, 1)

        # show the image
        cv2.imshow('Video image', img)

        # close the window and stop the loop if 'q' is pressed
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Error reading frame')
        break

# release the video and close all windows
cap.release()
cv2.destroyAllWindows()
