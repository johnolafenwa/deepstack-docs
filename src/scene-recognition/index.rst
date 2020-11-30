.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Scene Recognition
=================

The scene recognition api classifies an image into one of 365 scenes.

To use this API, you need to enable the scene API when starting DeepStack.


Starting DeepStack on Docker
----------------------------

Below we start DeepStack with only the Scene APIs enabled.

**CPU Version**

.. code-block:: bash

    sudo docker run -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 \
    deepquestai/deepstack


**GPU Version**

.. code-block:: bash

    sudo docker run --gpus all -e VISION-SCENE=True -v localstorage:/datastore \
    -p 80:5000 deepquestai/deepstack:gpu


Starting DeepStack on Raspberry PI
----------------------------------

.. code-block:: bash

    sudo deepstack start "VISION-SCENE=True"


Starting DeepStack on Windows
-----------------------------

Start the **DeepStack App**, Click *Start Server*, Select the **SCENE API** and click *Start Now* .

.. figure:: ../static/scene-windows.jpg


**Example**

.. figure:: ../static/office.jpg

.. code-block:: python

   import requests

   image_data = open("office.jpg","rb").read()

   response = requests.post("http://localhost:80/v1/vision/scene",files={"image":image_data}).json()
   print("Label:",response["label"])
   print(response)


**Response**

.. code-block:: text

   Label: conference_room
   {'success': True, 'confidence': 0.7373981, 'label': 'conference_room'}




.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
