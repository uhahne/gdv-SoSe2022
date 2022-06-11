# Image classification with kNN on CIFAR-10 data set
# go to https://www.cs.toronto.edu/~kriz/cifar.html and download the data
# CIFAR-10 python version: https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
# Extract into data folder.
import numpy as np
import cv2
from enum import Enum
import pickle
import glob

window_title = 'test image'


class Descriptor(Enum):
    ''' Define available descriptors '''
    COLOR32 = range(1)

    ''' Compute the descriptor vector '''
    def compute(self, img):
        if (self is Descriptor.COLOR32):
            # TODO
            return -1

    ''' Visually test the computation of the descriptor vector '''
    def testCompute(self, img):
        arr = self.compute(img)
        # get only the red channel (first 1024 values) and display it as greyscale image
        test_img = np.reshape(arr[:1024], (32, 32))
        cv2.imshow(window_title, test_img)
        cv2.waitKey(0)

    ''' Get the length of the descriptor vector '''
    def getSize(self):
        if (self is Descriptor.COLOR32):
            # TODO
            return -1


class TrainingSet:
    def __init__(self, root_path='') -> None:
        ''' Create and manage the image data set used as training data'''
        self.root_path = root_path

    def loadCifar10(self, batch_file, meta_file):
        ''' Load the CIFAR-10 data set and convert structure so that it can be used with OpenCV kNN algorithms'''
        with open(meta_file, 'rb') as fo:
            meta_data = pickle.load(fo, encoding='bytes')
        self.categories = meta_data[b'label_names']
        self.num_training_images = meta_data[b'num_cases_per_batch']
        with open(batch_file, 'rb') as fo:
            dict = pickle.load(fo, encoding='bytes')
        self.descriptor = Descriptor.COLOR32
        tempData = dict[b'data']
        tempResponses = np.array(dict[b'labels'])
        self.trainData = np.ndarray(shape=(self.num_training_images, self.descriptor.getSize()),
                                    buffer=np.float32(np.array(np.ravel(tempData))),
                                    dtype=np.float32)
        self.responses = np.ndarray(shape=(self.num_training_images, 1),
                                    buffer=np.float32(np.ravel(tempResponses)),
                                    dtype=np.float32)
        self.img_files = dict[b'filenames']
        print('Loaded CIFAR-10 training data:')
        print('Number of images: ', self.num_training_images)
        print('Used descriptor:', self.descriptor)
        print('Categories:', list(map(bytes.decode, self.categories)))

    def testCifar(self, index):
        ''' Test visually if the data is loaded correctly'''
        # TODO
        test_img = -1
        cv2.imshow(window_title, test_img)
        cv2.waitKey(0)


def classify_knn(trainData, sample, k):
    ''' Returns the dominating category in the k nearest neighbors'''
    # TODO implement knn classifier as explained here: https://docs.opencv.org/4.5.5/d5/d26/tutorial_py_knn_understanding.html


def run_test_on_folder(trainData, folder_name, k):
    ''' Loads all images found in the given folder and classifies them. '''
    num_test_images = 0
    for file in glob.glob(folder_name + '/*.jpg'):
        print('Testing file: %s' % file)
        descr = trainData.descriptor
        # load image
        img = cv2.imread(file, cv2.IMREAD_COLOR)
        descr.testCompute(img)
        newcomer = np.ndarray(shape=(1, descr.getSize()),
                              buffer=np.float32(descr.compute(img)),
                              dtype=np.float32)
        category = classify_knn(trainData, newcomer, k)
        print('Classified as %s' % category.decode())
        num_test_images += 1
    print('Found %d test images in %s' % (num_test_images, folder_name))


def main():
    # Initialize the training set and load CIFAR-10 data
    trainData = TrainingSet()
    trainData.loadCifar10('./data/cifar-10-batches-py/data_batch_1',
                          './data/cifar-10-batches-py/batches.meta')
    # create an image for visual debugging
    cv2.namedWindow(window_title, cv2.WINDOW_GUI_NORMAL)
    # check if training data is loaded correctly
    trainData.testCifar(375)
    # test a bunch of images
    # TODO define an appropriate number of neighbours (k)
    run_test_on_folder(trainData, './data/test_cifar/', k=-1)


if (__name__ == '__main__'):
    main()
