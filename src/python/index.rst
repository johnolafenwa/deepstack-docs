.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DeepStack - Python Guide!
=========================

Official Python Guide for DeepStack AI Server.
----------------------------------------------

**DeepStack** is an AI server that empowers every developer in the world to easily build state-of-the-art AI systems both on premise and in the cloud. The promises of Artificial Intelligence are huge but becoming a machine learning engineer is hard. **DeepStack** is device and language agnostic. You can run it on **Windows**, **Mac OS**, **Linux**, **Raspberry PI** and use it with any programming language.

**DeepStack** is developed and maintained by `DeepQuest AI <https://deepquestai.com>`_ .



Top Features
=============
* `FACE DETECTION & RECOGNITION <face-recognition>`_
* `OBJECT DETECTION <object-detection>`_
* `SCENE RECOGNITION <scene-recognition>`_
* `SUPPORT FOR CUSTOM ONNX, KERAS AND TENSORFLOW MODELS <custom-models>`_
* `IN-BUILT SECURITY <security>`_
* `API REFERENCE <api-reference>`_


Example Code
============
.. figure:: static/road.jpg

Using DeepStack, we can classify the scene of the above image as seen below.

.. code-block:: python

  import requests

  image_data = open("image.jpg","rb").read()

  response = requests.post("http://localhost:80/v1/vision/scene",
  files={"image":image_data}).json()
  print(response)

**Response**

.. code-block:: json

  { 'success': true, label: 'highway', confidence: 0.63377846 }



Installation
============

**DeepStack** is available in three variants, **CPU Version**, **GPU Version** and **Raspberry PI Version** (With Support for Intel Neural Compute Stick)

`Installation Guide for GPU Version <using-deepstack-with-nvidia-gpus>`_

`Installation Guide for Raspberry Pi <raspberry-pi>`_

Installation Guide for CPU Version
----------------------------------

Step 1: Install Docker (If not already installed)
Mac OS and Windows Users can install docker from `Docker's Website <https://www.docker.com/products/docker-desktop>`_ .

To install on a **Linux** operating system, run the commands below

.. code-block:: bash

  sudo apt-get update
  sudo apt-get install docker.io

Step 2: Install DeepStack

.. code-block:: bash

  docker pull deepquestai/deepstack


Step 3: Run DeepStack with Scene Recognition API enabled

.. code-block:: bash

  docker run -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack


*Basic Parameters*

**-e VISION-SCENE=True** This enables the scene recognition API, all apis are disabled by default.

**-v localstorage:/datastore** This specifies the local volume where DeepStack will store all data.

**-p 80:5000** This makes DeepStack accessible via port 80 of the machine.


Run the **example scene recognition** code at the begining of this page to verify your installation is working.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting-started/index
   face-recognition/index
   face-detection/index
   face-match/index
   object-detection/index
   scene-recognition/index



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
