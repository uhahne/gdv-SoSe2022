# Demonstrating usage of filters in OpenCV
import cv2
import numpy as np
import time
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')


def convolution_with_opencv(image, kernel):
    # flip the kernel as opencv filter2D function is
    # a correlation not a convolution
    kernel = cv2.flip(kernel, -1)
    # when ddepth=-1, the output image will have the same depth as the source.
    ddepth = -1
    output = cv2.filter2D(image, ddepth, kernel)
    return output


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
    # cv2.destroyWindow(title_kernel)


def show_kernel_3D(kernel, kernel_size, title):
    # show the kernel as 3D plot
    # Prepare data.
    z_factor = 100
    X = np.arange(0, kernel_size, 1)
    Y = np.arange(0, kernel_size, 1)
    X, Y = np.meshgrid(X, Y)
    Z = cv2.normalize(kernel, kernel, 0, z_factor,
                      cv2.NORM_MINMAX, cv2.CV_8UC1)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.cividis,
                           linewidth=0, antialiased=False)
    ax.set(title=title)
    # Customize the z axis.
    ax.set_zlim(0, z_factor)
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')
    plt.show()


def main():
    # Load the image.
    image_name = 'images/Bumbu_Rawon.jpg'
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    # image = cv2.resize(image, (320,213))

    # define kernel
    kernel_size = 35
    # sigma Gaussian standard deviation. If it is non-positive,
    # it is computed from kernel_size as
    # sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8
    sigma = 4
    kernel1D = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = np.transpose(kernel1D) * kernel1D
    # (kernel, kernel_size) = create_gaussian_blur_kernel(1)
    title = '%d by %d Gaussian kernel (sigma=%d)' % (
        kernel_size, kernel_size, sigma)
    show_kernel_3D(kernel, kernel_size, title)

    # run convolution and measure the time it takes
    # start time to calculate computation duration
    start = time.time()

    result = convolution_with_opencv(image, kernel)
    # end time after computation
    end = time.time()
    print('Computing the convolution of an image with a resolution of',
          image.shape[1], 'by', image.shape[0], 'and a kernel size of',
          kernel.shape[0], 'by', kernel.shape[1], 'took', end-start,
          'seconds.')

    # show the original and the resulting image
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


if (__name__ == '__main__'):
    main()
