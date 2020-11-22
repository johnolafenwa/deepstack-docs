.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Getting Started
================

In this tutorial, we shall go through the complete process of using DeepStack to build a Face Recognition system.

Setting Up DeepStack
--------------------

Install and Setup DeepStack Using the `Install Guide <../index.html#installation-guide-for-cpu-version>`_ . If you have a system with Nvidia GPU, follow instruction on Using DeepStack with NVIDIA GPU to install the GPU Version of DeepStack


Starting DeepStack on Docker
----------------------------

For **CPU Version**

.. code-block:: bash

  sudo docker run -e VISION-FACE=True -v localstorage:/datastore \ 
  -p 80:5000 deepquestai/deepstack


For **GPU Version**

.. code-block:: bash

  sudo docker run --gpus all -e VISION-FACE=True -v localstorage:/datastore \
  -p 80:5000 deepquestai/deepstack:gpu


*Basic Parameters*

**-e VISION-FACE=True** This enables the face recognition APIs, all apis are disabled by default.

**-v localstorage:/datastore** This specifies the local volume where deepstack will store all data.

**-p 80:5000** This makes deepstack accessible via port 80 of the machine.


Starting DeepStack on Raspberry PI
----------------------------------

.. code-block:: bash

  sudo deepstack start "VISION-FACE=True"


Face Recognition
----------------

Think of a software that can identify known people by their names. Face Recognition does exactly that. Register a picture of a number of people and the system will be able to recognize them again anytime. Face Recognition is a two step process: The first is to register a known face and second is to recognize these faces in new pictures.


**REGISTERING A FACE**

Here we are building an application that can tell the names of a number of popular celebrities. First we collect pictures of a number of celebrities and we register them with **DeepStack**.


.. figure:: ../static/tomcruise.jpg

.. figure:: ../static/adele.jpg

.. figure:: ../static/idriselba.jpg

.. figure:: ../static/perri.jpg


Below we will register the faces with their names

.. code-block:: python

   import requests

   def register_face(img_path,user_id):
      image_data = open(img_path,"rb").read()
      response = requests.post("http://localhost:80/v1/vision/face/register",
      files={"image":image_data}, data={"userid":user_id}).json()
      print(json)

   register_face("cruise.jpg","Tom Cruise")
   register_face("adele.jpg","Adele")
   register_face("elba.jpg","Idris Elba")
   register_face("perri.jpg","Christina Perri")



**RECOGNITION**

.. figure:: ../static/adele2.jpg

.. code-block:: python

   import requests

   test_image = open("test-image.jpg","rb").read()

   res = requests.post("http://localhost:80/v1/vision/face/recognize",
   files={"image":test_image}).json()

   for user in res["predictions"]:
      print(user["userid"])



**Response**

.. code-block:: text

   Adele


We have just created a face recognition system. You can try with different people and test on different pictures of them.

The `next tutorial <../face-recognition.html>`_ is dedicated to the full power of the face recognition api as well as best practices to make the best out of it.


Performance
-----------

DeepStack offers three modes allowing you to tradeoff speed for performance. During startup, you can specify performance mode to be , **High** , **Medium** and **Low**.

The default mode is **Medium**

You can specify a different mode during startup as seen below.

**CPU Version**

.. code-block:: bash

   sudo docker run -e MODE=High VISION-FACE=True -v localstorage:/datastore \
   -p 80:5000 deepquestai/deepstack

**GPU Version**

.. code-block:: bash

   sudo docker run --rm --runtime=nvidia -e MODE=High -e VISION-FACE=True \
   -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu

Note the **-e MODE=High** above.

On Windows, you can easily select the **High** mode in the UI.

.. figure:: ../static/windows-mode.jpg


.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
