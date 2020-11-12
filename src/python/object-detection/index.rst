.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Object Detection
================

The object detection API locates and classifies 80 different kinds of objects in a single image. 

To use this API, you need to enable the detection API when starting DeepStack


Starting DeepStack on Docker
----------------------------

Below we start DeepStack with only the Detection APIs enabled.

**CPU Version**

.. code-block:: bash

    sudo docker run -e VISION-DETECTION=True -v localstorage:/datastore -p 80:5000 \
    deepquestai/deepstack


**GPU Version**

.. code-block:: bash

    sudo docker run --gpus all -e VISION-DETECTION=True -v localstorage:/datastore \
    -p 80:5000 deepquestai/deepstack:gpu


*Basic Parameters*

**-e VISION-DETECTION=True** This enables the object detection API, all apis are disabled by default.

**-v localstorage:/datastore** This specifies the local volume where deepstack will store all data.

**-p 80:5000** This makes deepstack accessible via port 80 of the machine.


Starting DeepStack on Raspberry PI
----------------------------------

.. code-block:: bash

    sudo deepstack start "VISION-DETECTION=True"


Starting DeepStack on Windows
-----------------------------

Start the **DeepStack App**, Click *Start Server*, Select the **DETECTION API** and click *Start Now*.

.. figure:: ../static/object-detection.png


**Example**

.. figure:: ../static/family-and-dog.jpg

.. code-block:: python

    import requests

    image_data = open("test-image3.jpg","rb").read()

    response = requests.post("http://localhost:80/v1/vision/detection",files={"image":image_data}).json()

    for object in response["predictions"]:
        print(object["label"])

    print(response)


**Response**

.. code-block:: text

    dog
    person
    person
    {'predictions': [{'x_max': 819, 'x_min': 633, 'y_min': 354, 'confidence': 99, 'label': 'dog', 'y_max': 546}, {'x_max': 601, 'x_min': 440, 'y_min': 116, 'confidence': 99, 'label': 'person', 'y_max': 516}, {'x_max': 445, 'x_min': 295, 'y_min': 84, 'confidence': 99, 'label': 'person', 'y_max': 514}], 'success': True}


We can use the coordinates returned to extract the objects

.. code-block:: python

    import requests
    from PIL import Image

    image_data = open("test-image3.jpg","rb").read()
    image = Image.open("test-image3.jpg").convert("RGB")

    response = requests.post("http://localhost:80/v1/vision/detection",files={"image":image_data}).json()
    i = 0
    for object in response["predictions"]:

        label = object["label"]
        y_max = int(object["y_max"])
        y_min = int(object["y_min"])
        x_max = int(object["x_max"])
        x_min = int(object["x_min"])
        cropped = image.crop((x_min,y_min,x_max,y_max))
        cropped.save("image{}_{}.jpg".format(i,label))

        i += 1


.. figure:: ../static/dog.jpg

.. figure:: ../static/man.jpg

.. figure:: ../static/woman.jpg


Setting Minimum Confidence
--------------------------

By default, the minimum confidence for detecting objects is 0.45. The confidence ranges between 0 and 1. If the confidence level for an object falls below the min_confidence, no object is detected.

The min_confidence parameter allows you to increase or reduce the minimum confidence.

We lower the confidence allowed below.

..code-block:: python

    import requests

    image_data = open("test-image3.jpg","rb").read()

    response = requests.post("http://localhost:80/v1/vision/detection",
    files={"image":image_data},data={"min_confidence":0.30}).json()


CLASSES
-------

The following are the classes of objects DeepStack can detect in images

.. code-block:: text

    person,   bicycle,   car,   motorcycle,   airplane,
    bus,   train,   truck,   boat,   traffic light,   fire hydrant,   stop_sign,
    parking meter,   bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,
    bear,   zebra, giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,
    frisbee,   skis,   snowboard, sports ball,   kite,   baseball bat,   baseball glove,
    skateboard,   surfboard,   tennis racket, bottle,   wine glass,   cup,   fork,
    knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange, broccoli,   carrot,
    hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed, dining table,
    toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave,
    oven,   toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,
    hair dryer, toothbrush.


Performance
-----------

DeepStack offers three modes allowing you to tradeoff speed for performance. During startup, you can specify performance mode to be , **High** , **Medium** and **Low**. 

The default mode is **Medium**.

You can specify a different mode during startup as seen below as seen below

**CPU Version**

.. code-block:: bash

   sudo docker run -e MODE=High VISION-DETECTION=True -v localstorage:/datastore -p 80:5000 \
   deepquestai/deepstack


**GPU Version**

.. code-block:: bash

   sudo docker run --gpus all -e MODE=High -e VISION-DETECTION=True -v localstorage:/datastore \
   -p 80:5000 deepquestai/deepstack:gpu


Note the **-e MODE=High** above

On Windows, you can easily select the High mode in the UI.

.. figure:: ../static/detection-high.jpg

Note the **High** radio button selected above.

**Speed Modes are not available on the Raspberry PI Version**


.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
