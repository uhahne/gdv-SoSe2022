# Assignment #4 - Object detection

## Task
Implement an object or face detection script in Python using OpenCV's machine learning capabilities (see [DNN tutorials](https://docs.opencv.org/4.5.3/d2/d58/tutorial_table_of_content_dnn.html) alternatively [Cascade classifiers](https://docs.opencv.org/4.5.3/db/d28/tutorial_cascade_classifier.html)). Record a video that shows a stable detection of multiple objects or faces while the camera is moving. Draw the detection results into the video. The video should contain 900 frames, so that it runs for 30 seconds. Count the number of those frames in which the detection is correct and provide this information.
Write a short readme how to run the code and a brief explanation (max. 500 words, German or English).

## Remarks
In the tutorial 19 something similar is implemented. However, for the video we use in the tutorial, the model is not able to detect all the objects properly. This assignement can be passed either by changing the model or the video.
Please be aware that in real world applications the video is unknown and the object or face detection should work for any new input. If your detection does only work under some special circumstances, state them clearly in the readme.

## Rating
- Video is showing the requested object or face detection (up to 5 points)
  - just one object/face (1 point) or multiple objects/faces (3 points)
  - more than 80% of the frames detect the objects/faces correctly (1 point)
  - more than 90% of the frames detect the objects/faces correctly (1 point)
- Summary of detection results is stored in a file (1 point)
- Some other model than the one from the tutorials is used (up to 3 points)
- Code is well readable, structured and documented (up to 2 points)
- Readme is well written and contains all steps to install and run the code (1 point)

## Acceptance criteria
- Hand in code (.py file) and readme.md file as one zip file via FELIX.
- Script runs without changes. One output video is generated.
- In the readme, it is clearly visible described which model is used and how it has been processed before it was usable.

## Pass criteria
- The assignment is passed, if 5 or more points are reached.