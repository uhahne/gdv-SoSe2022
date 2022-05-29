# Assignment #4 - Image retrieval

## Task
Implement a Python program that creates a [photographic mosaic](https://en.wikipedia.org/wiki/Photographic_mosaic) of a given picture from a data set of images. The code to access the data base is given in [GDV_ImageRetrieval.py](./GDV_ImageRetrieval.py) and [GDV_TrainingSet.py](./GDV_TrainingSet.py). It is implemented in Python using OpenCV's machine learning capabilities (based on [kNN tutorial](https://docs.opencv.org/4.5.5/d5/d26/tutorial_py_knn_understanding.html)). The program should get an image as input and create another image that is composed only from the images of the data set. This resulting image needs to be stored. Hand in two nice photographic mosaics that have been created with your tool.
The bonus task is to implement new descriptors that lead to better results than the already implemented "tiny image" descriptor.
Write a short readme how to run the code and a brief explanation (max. 500 words, German or English).

## Remarks
In order to set up the data base, it is necessary to download the [Caltech-101 image data set](https://data.caltech.edu/records/20086). The annotations are not needed, only the image files from the folder '101_ObjectCategories'. Extract those into a subfolder 'data'.
The data can be saved to a file and reloaded again, as it is also usable for image classification, it is called training data.

## Hints
Note that the computation of descriptors for all images takes a while (1 minute on a new laptop). You can start with a subset in order to save time. Also finding best matches for each tile might take some seconds. Hence, the generation of the output mosaic might take some minutes.

## Rating
- The data set is set up correctly and the image descriptors are computed for all images (1 point)
- The input image is subdivided into tiles (1 point)
- For each tile the best matching image is found in the data set (1 point)
- The output image is correctly created, displayed and can be saved as a file (2 points)
- Two nice photographic mosaics are submitted (2 points)
- BONUS: A new descriptor is implemented that leads to nicer results (2 points)  
- Code is well readable, structured and documented (up to 2 points)
- Readme is well written and contains all steps to install and run the code (1 point)

## Acceptance criteria
- Hand in code (.py file) and readme.md file as one zip file via FELIX or as link to a github repository.
- Script runs without changes. Image output is generated.

## Pass criteria
- The assignment is passed, if 5 or more points are reached.