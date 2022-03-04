# Demonstrating usage of filters in OpenCV
import cv2
import numpy as np
import time


def convolution_with_opencv(image, kernel):
    # flip the kernel as opencv filter2D function is a
    # correlation not a convolution

    # when ddepth=-1, the output image will have the same depth as the source.

    # run filtering

    # return result
    return result


def show_kernel(kernel):
    # show the kernel as image
    title_kernel = 'Kernel'
    # Note that window parameters have no effect on MacOS
    cv2.namedWindow(title_kernel, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_kernel, 300, 300)
    # scale kernel to make it visually more appealing
    kernel_img = cv2.normalize(
        kernel, kernel, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    cv2.imshow(title_kernel, kernel_img)
    cv2.waitKey(0)


def show_resulting_images(image, result):
    title_original = 'Original image'
    # Note that window parameters have no effect on MacOS
    cv2.namedWindow(title_original, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(title_original, image)

    title_result = 'Resulting image'
    # Note that window parameters have no effect on MacOS
    cv2.namedWindow(title_result, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(title_result, result)

    key = cv2.waitKey(0)
    if key == ord('s'):
        # save resulting image
        res_filename = 'filtered_with_%dx%d_gauss_kernel_with_sigma_%d.png' % (
                    kernel_size, kernel_size, sigma)
        cv2.imwrite(res_filename, result)
    cv2.destroyAllWindows()

# use a main method for the program


def main():
    # Load the image.
    image_name = 'images/Bumbu_Rawon.jpg'
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    # image = cv2.resize(image, (320,213))

    # define kernel
    # define kernel size

    # define Gaussian standard deviation (sigma). If it is non-positive,
    # it is computed from kernel_size as
    # sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8

    # create the kernel with OpenCV

    # visualize the kernel
    show_kernel(kernel)

    # run convolution and measure the time it takes
    # start time to calculate computation duration

    # run the convolution

    # end time after computation

    # print timing results
    print('Computing the convolution of an image with a resolution of',
          image.shape[1], 'by', image.shape[0], 'and a kernel size of',
          kernel.shape[0], 'by', kernel.shape[1], 'took', end-start, 'seconds.')

    # show the original and the resulting image
    show_resulting_images(image, result)


# define to start the main method
