.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Face Detection
==============

The face detection API detects faces and returns their coordinates. It functions similarly to the face recognition API except that it does not perform recognition.

**Example**

.. figure:: ../static/family.jpg

.. code-block:: python

    import requests

    image_data = open("family.jpg","rb").read()

    response = requests.post("http://localhost:80/v1/vision/face",files={"image":image_data}).json()

    print(response)

**Response**

.. code-block:: json

    {'predictions': [{'x_max': 712, 'y_max': 261, 'x_min': 626, 'confidence': 0.99990666, 'y_min': 145}, {'x_max': 620, 'y_max': 288, 'x_min': 543, 'confidence': 0.99986553, 'y_min': 174}, {'x_max': 810, 'y_max': 242, 'x_min': 731, 'confidence': 0.99986434, 'y_min': 163}, {'x_max': 542, 'y_max': 279, 'x_min': 477, 'confidence': 0.99899536, 'y_min': 197}], 'success': True}

We can use the coordinates returned to extract the faces from the image.

.. code-block:: python

    import requests
    from PIL import Image

    image_data = open("family.jpg","rb").read()
    image = Image.open("family.jpg").convert("RGB")

    response = requests.post("http://localhost:80/v1/vision/face",files={"image":image_data}).json()
    i = 0
    for face in response["predictions"]:

        y_max = int(face["y_max"])
        y_min = int(face["y_min"])
        x_max = int(face["x_max"])
        x_min = int(face["x_min"])
        cropped = image.crop((x_min,y_min,x_max,y_max))
        cropped.save("image{}.jpg".format(i))

        i += 1
    

.. figure:: ../static/family1.jpg

.. figure:: ../static/family2.jpg

.. figure:: ../static/family3.jpg

.. figure:: ../static/family4.jpg




.. toctree::
   :maxdepth: 2
   :caption: Contents:


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
