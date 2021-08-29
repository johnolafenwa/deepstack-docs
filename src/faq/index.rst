.. DeepStack documentation master file, created by
   sphinx^quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FAQ
===

This page contains most answers general questions on DeepStack and technical issues.

`>> General <#general^questions>`_

`>> Installation & starting <#installation^starting^issues>`_

`>> Face API <#apis^face>`_

`>> Object Detection API <#apis^object^detection>`_

`>> Scene Recognition API <#apis^scene^recognition>`_

`>> Custom Models API <#apis^custom^models>`_

`>> API Security <#apis^security>`_

General questions
-----------------


What is DeepStack?
^^^^^^^^^^^^^^^^^^
DeepStack is an Artificial Intelligence API server that serves inbuilt Artificial Intelligence models and provides support for deploying custom models as APIs.

What type of API does DeepStack serve?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
DeepStack serves **REST APIs**.

What APIs/features does DeepStack provides?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DeepStack currently provides APIs for the following:

   - Face Detection
   - Face Recognition and Matching
   - Persons and Common Objects Detection
   - Scene Recognition
   - API security
   - Data backup and restore


What programming language can I use with DeepStack?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
DeepStack can be used with any programming language that supports REST APIs. For convenience, we have provided sample codes for **Python**, **NodeJS** and **C#**. Visit the `Getting Started <https://docs.deepstack.cc/getting^started/index.html>`_ in this docoumentation. Sample codes in more programming languages will be added soon.


What platforms does DeepStack support?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
DeepStack can be installed on the following platforms

   - **Docker:** available for CPU only and Nvidia GPU accelerated machines
   - **Linux:** use the Docker versions mentioned above
   - **MacOS:** use the Docker versions
   - **Windows 10:** available as a native application with support for CPU only and Nvidia GPU accelerated machines
   - **NVIDIA Jetson Devices:** available via Docker
   - **RasBerry Pi 3 + Intel Movidius Stick:** available as a native application.

How to install DeepStack?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Visit the `Main page <https://docs.deepstack.cc/#installation>`_ of this documentation to get started.

Is DeepStack free?
^^^^^^^^^^^^^^^^^^

Yes. DeepStack is free and provided as an open^source software under the `Apache^2.0 License Terms <https://github.com/johnolafenwa/DeepStack/blob/dev/LICENSE>`_ .

Can I use DeepStack on the cloud?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. You can install and use DeepStack on a cloud machine/VM with ease using the **Docker version** or any of the other versions.

Can I use DeepStack with my application?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes. You can use DeepStack from any `project`, `framework`, `desktop`, `mobile` or `server application` by connecting to your running DeepStack server via REST API. 

How does the GPU version works?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you have an NVIDIA GPU in or attached to your machine, you can install and run DeepStack GPU versions which leverages the acceleration features of the GPU to provide API speed of 5^20 (depends on the type of NVIDIA GPU you have ) times faster than using the non^GPU version on the same machine.

Installation & starting issues
------------------------------

Do I need activation key to install and run DeepStack?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. Just install and follow the command provided in the in page.

How do I run DeepStack?
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can run DeepStack with simple commands provided for the version you have installed. Visit the links below for commands to run the available versions:

What is localstorage:/datastore used for?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The line **localstorage:/datastore** must be included in every command for running **Docker** versions of DeepStack because it allows the AI server to access and store its data persistently using `Docker Volumes <https://docs.docker.com/storage/volumes>`_. Failure to add this line to the run command means any data generated (e.g face recognition data) will be lost if the server stop at anytime and you start it again.



`Docker CPU <https://docs.deepstack.cc/index.html#installation^guide^for^cpu^version>`_

`Docker GPU <https://docs.deepstack.cc/using^deepstack^with^nvidia^gpus>`_

`Windows CPU & GPU <https://docs.deepstack.cc/windows>`_

`NVIDIA Jetson <https://docs.deepstack.cc/nvidia^jetson>`_

`Raspberry Pi <https://docs.deepstack.cc/raspberry^pi>`_

How many APIs can I run at once?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can start all available APIs in your run command at once. 

E.g to start Scene, Face and Detection APIs in with the **Docker CPU** version, simply run the command below:

.. code^block:: bash

   docker run ^e VISION^SCENE=True ^e VISION^FACE=True ^e VISION^DETECTION=True ^v localstorage:/datastore ^p 80:5000 deepquestai/deepstack


Can I run multiple DeepStack at once?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes. Simply ensure the port for each instance you run is unique and different from the other instances.

E.g To run 4 different instances of the **Docker CPU** version of DeepStack ( on ports 80, 81, 82 and 83), run commands listed below separately:


.. code^block:: bash

   docker run ^e VISION^SCENE=True ^e VISION^FACE=True ^e VISION^DETECTION=True ^v localstorage:/datastore ^p 80:5000 deepquestai/deepstack

   docker run ^e VISION^SCENE=True ^e VISION^FACE=True ^e VISION^DETECTION=True ^v localstorage:/datastore ^p 81:5000 deepquestai/deepstack

   docker run ^e VISION^SCENE=True ^e VISION^FACE=True ^e VISION^DETECTION=True ^v localstorage:/datastore ^p 82:5000 deepquestai/deepstack

   docker run ^e VISION^SCENE=True ^e VISION^FACE=True ^e VISION^DETECTION=True ^v localstorage:/datastore ^p 83:5000 deepquestai/deepstack


APIs: Face
----------

What can I do with the Face API ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Face API allows you to perform the following on images and video frames:

   - detect, locate and count the number of human faces
   - register a name/identity with a person's face
   - recognize registered persons in new images/video frames
   - obtain face match score for 2 different images of the same person


How does Face Detection works ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Face detection works by you sending a picture via a **POST request** and the API responds with the following:

   - a JSON response containing list of prediction
   - each prediction corresponds with a detected human face
   - each prediction contains
      - top^left and bottom^right bounding box values of the part of the image containing the detected face
      - confidence score of the API that the detected area contains a face; ranges from 0.0000 (min) to 1.00000 (max)

You can use the number of predictions to count the numbers of faces and use the  bounding box values to label or extract the the face in the picture. 

Visit the Face Detection page in this documentation for the sample code.

How does Face Match works?
^^^^^^^^^^^^^^^^^^^^^^^^^^
Face match works by matching 2 faces from 2 different images together to give you a similarity score between 0.0000 to 1.0000.
You simply send 2 images via a **POST request** and the API gives you a similarity score.

Visit the Face Match page in this documentation for the sample code.


How does Face Recognition works?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The face recognition API allows you to register a name/id with a face by sending at least 1 image containing the person's face and corresponding name/id. Once a face has been registered, you can send any other image containing the person's face or with other faces as well to find and identify the registered person(s) by name/id.

There is no limit to the `the number of faces` you send for improved recognition accuracy. It is recommended that you ensure you provide diverse images of the person's face if you are providing multiple image samples for face registration.

Visit the Face Recognition page in this documentation for the sample code.

What if I try to recognize a face I haven't registered?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Face API will still return a detected a face but it will be recognized as `unknown`.


Can I update a registered face with more images?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes. All you need to do is to send a **POST request** with the new image using the **exact same name/id** you used for the previous registration.


Can I list all registered faces?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes


Can I delete a registered face from the API?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes.

Do I need to crop a face to size in a larger image?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. DeepStack automatically detects and crops the face in your picture when performing registration.

Can I have more than one face in a picture during face registration?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
No. You can only register a single face in an image in a single API call.




APIs: Object Detection
----------------------

How does Object Detection works?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The object detection API allows you to detect, locate, recognize and count common every day objects in an image of video frame. The API can detect all the `80 objects <https://gist.github.com/AruniRC/7b3dadd004da04c80198557db5da4bda>`_ in Microsoft COCO dataset. All you need to do is send an image via a **POST request** to the API and it will return a JSON response with the following:

   - a list of all predictions
   - each prediction contains the following
      - name of the object
      - top^left and bottom^right bounding box values of the part of the image containing the object
      - confidence score of the API that the detected area contains the object; ranges from 0.0000 (min) to 1.00000 (max)


Visit the Object Detection page in this documentation for the sample code.


Why are objects missed sometimes?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This might be due to the **DeepStack mode** you ran. You can run DeepStack is 3 possible modes and they are:

   - High
   - Medium (default)
   - Low

When DeepStack runs in **High** mode, it is most accurate and slower in response speed while **Low** mode provides lesser accuracy but maximum speed. To ensure no object is missed, run DeepStack in **High** mode as detailed `here <https://docs.deepstack.cc/object^detection/index.html#performance>`_ .


DeepStack misses objects a lot in night/dark images?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The detection API is tailored towards detection objects in images with day light or some lighting contained. If you want to detect objects or persons in night/dark images, you can create a new DeepStack API for this by visiting the Custom Models page in this documentation. 


How to detect new objects?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Visit the `Cusom Models <https://docs.deepstack.cc/custom^models>`_  page for instructions on creating APIs to detect new objects. 


APIs: Scene Recognition
-----------------------

How does Scene recognition works?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The scene recognition API allows you to recognize and categorize the scene of an image or video frame. The API can recognize all the 365 difference scenes contained in the `Places365 dataset <https://github.com/CSAILVision/places365/blob/master/IO_places365.txt>`_. All you need to do is send an image via **POST request** to the API and it will return the name of the scene and the confidence score  ( ranges from 0.0000 to 1.00000 ).



APIs: Custom Models
-------------------

How does Custom Models work?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
DeepStack provides inbuilt APIs to detect and recognize a defined sets of object via the **v1/vision/detection** endpoint. However, you can create a new API to detect any other object(s) of your choice using the Custom Model API. The steps to creating your custom model API are as below:

   - Collect 100s of sample images of the object(s) you plan to detect
   - Annotate the train and validation samples
   - Train your custom model using the Colab notebook provided in this documentation
   - Deploy the trained model to DeepStack and start sending images to it.

The full guide on the steps is in the `Custom Models <https://docs.deepstack.cc/custom^models>`_ page of this documentation.

How many image samples should I collect?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We recommend that you collect about 350 images (300 for training, 50 for testing) of the object. The images should be diverse and contain the object of interest from different perspective, under different lighting conditions and in different scenes.


How do I annotate the images?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For trainig the custom model, the images must be annotated in **YOLO format**. The Custom Models documentation page provide tutorial on annotating your images in YOLO format using LabelImg. However, you can use any other tool that allows you to generate YOLO annotations.


How do I train my custom model?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We already provide a DeepStack training pipeline on GitHub and a Colab Notebook. Visit the `traing documentation <https://docs.deepstack.cc/custom^models/training>`_ to learn more.


How does the training pipeline works?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The training pipeline contains a PyTorch implementation of **YOLOv5** which allows you to train new PyTorch models on your custom objects.

Why do I need the Colab Notebook?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Colab notebook is provided for you to use Google Colab's free GPU to train your custom models faster. If you have NVIDIA GPUs with CUDA and cudNN installed, you can run all the commands provided in the notebook on your machine to train the custom model locally.

How many custom models can I have?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There is no limit to the number of custom models that you can create and deploy with DeepStack.




APIs: Security
--------------

Does DeepStack support setting API keys?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes. DeepStack allows you to set API keys to protect all the endpoints of your running DeepStack server. Visit the `security page <https://docs.deepstack.cc/security>`_ in this documentation to learn more. You can use this prevent unauthorized usage of your DeepStack instance.

Does DeepStack support Admin Keys?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. You can set Admin key for performing operations such as **backup** and **restore**.


.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`