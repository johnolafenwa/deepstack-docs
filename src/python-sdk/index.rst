.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python SDK
==========

To ensure easy integration of DeepStack APIs into your Python code and applications, we have developed the DeepStack **Python SDK** which allows you to use DeepStack APIs to process images, videos, camera feeds and utilize advance functionalities like file/Numpy array/byte/PIL/camera inputs, file/byte outputs, callbacks and more using few lines of Python code. 

The Python SDK is can be installed from **Pypi** via **pip install deepstack-sdk** and it is available on `GitHub <https://github.com/johnolafenwa/DeepStackPython>`_


Install DeepStack
-----------------

If you haven't done so, kindly follow `this link <https://docs.deepstack.cc/index.html#installation>`_ to install DeepStack.


Install Python SDK
------------------

Run the command below to install DeepStack Python SDK

.. tabs::

   .. code-tab:: bash Pypi

    pip install deepstack-sdk --upgrade




Object Detection
----------------

**1) Detect Objects in an image**

.. figure:: ../static/detection.jpg

.. code:: python

   from deepstack_sdk import ServerConfig, Detection

   config = ServerConfig("http://localhost:80")
   detection = Detection(config)

   response = detection.detectObject("image.jpg",output="image_output.jpg")

   for obj in response:
      print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))

.. figure:: ../static/detection_output.jpg


**Available Parameters**:

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.

- **detectObject()**
   - *image* (required): file path, numpy array, PIL Image, image bytes, url
   - *format* (optional): jpg, png
   - *min_confidence* (optional): 0.1 to 1.0
   - *callback* (optional): function name, parses in image_byte [without label and boxes] and detections into the function
   - *output* (optional): file path of none if you don't want to save to file
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 


**2) Detect Objects in a video**

.. code:: python

   from deepstack_sdk import ServerConfig, Detection

   config = ServerConfig("http://localhost:80")
   detection = Detection(config)

   detection.detectObjectVideo("video.mp4",output="video_output.mp4")

**Available Parameters**

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.

- **detectObjectVideo()**
   - *video* (required):  file path, Camera video feed IP, integer for OpenCV Camera e.g 0, 1, 2
   - *min_confidence* (optional): 0.1 to 1.0
   - *codec* (optional): Default: cv2.VideoWriter_fourcc(*'mp4v')
   - *fps* (optional): frames per second
   - *continue_on_error* (optional):  Default: false
   - *output* (required): file path, cv2.VideoWriter
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 


Face API
--------

**1) Detect faces in an image**

.. figure:: ../static/got.jpg

.. code:: python

   from deepstack_sdk import ServerConfig, Face

   config = ServerConfig("http://localhost:80")
   face = Face(config)

   response = face.detectFace("image.jpg",output="image_output.jpg")

   for obj in response:
      print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))


.. figure:: ../static/got_detected.jpg

**Available Parameters**:

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.

- **detectFace()**
   - *image* (required): file path, numpy array, PIL Image, image bytes, url
   - *format* (optional): jpg, png
   - *min_confidence* (optional): 0.1 to 1.0
   - *callback* (optional): function name, parses in image_byte [without label and boxes] and detections into the function
   - *output* (optional): file path of none if you don't want to save to file
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 


**3) Register images of the same face with an ID**

.. figure:: ../static/thanos.jpg

.. code:: python
  
   from deepstack_sdk import ServerConfig, Face

   config = ServerConfig("http://localhost:80")
   face = Face(config)

   images = ["face_image1.jpg","face_image12.jpg", "face_image3.jpg", "face_imageN.jpg"]
   response = face.registerFace(images=images,userid="Thanos")
   print(response)



**4) Recognize faces in an image**

.. figure:: ../static/thanos2.jpg

.. code:: python

   from deepstack_sdk import ServerConfig, Face

   config = ServerConfig("http://localhost:80")
   face = Face(config)

   response = face.recognizeFace(image=r"face_image.jpg", output="face_output.jpg" )
   print(response)


.. figure:: ../static/face_output.jpg
   

**Available Parameters**:

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.
  

- **recognizeFace()**
   - *image* (required): file path, numpy array, PIL Image, image bytes, url
   - *format* (optional): jpg, png
   - *min_confidence* (optional): 0.1 to 1.0
   - *callback* (optional): function name, parses in image_byte [without label and boxes] and detections into the function
   - *output* (optional): file path of none if you don't want to save to file
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 



**5) List registered faces**


.. code:: python

   from deepstack_sdk import ServerConfig, Face

   config = ServerConfig("http://localhost:80")
   face = Face(config)

   response = face.listFaces()
   for obj in response:
      print(obj)


**6) Delete a face from registered list**

.. code:: python

   from deepstack_sdk import ServerConfig, Face

   config = ServerConfig("http://localhost:80")
   face = Face(config)

   response = face.deleteFace("Thanos")
   print(response)



**7) Detect faces in a video**

.. code:: python

   from deepstack_sdk import ServerConfig, Face

   config = ServerConfig("http://localhost:80")
   face = Face(config)

   response = face.detectFaceVideo("video.mp4",output="face_detected.mp4")

   for obj in response:
      print("Face Detected, Confidence: {}".format(obj.confidence))


**Available Parameters**:

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.
  

- **detectFaceVideo()**
   - *video* (required):  file path, Camera video feed IP, integer for OpenCV Camera e.g 0, 1, 2
   - *min_confidence* (optional): 0.1 to 1.0
   - *codec* (optional): Default: cv2.VideoWriter_fourcc(*'mp4v')
   - *fps* (optional): frames per second
   - *continue_on_error* (optional):  Default: false
   - *output* (required): file path, cv2.VideoWriter
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 



**8) Recognize faces in video**


.. code:: python

   from deepstack_sdk import ServerConfig, Face

   config = ServerConfig("http://localhost:80")
   face = Face(config)

   response = face.recognizeFaceVideo("video.mp4", output="webcam.mp4" )
   print(response)



**Available Parameters**:

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.
  

- **recognizeFaceVideo()**
   - *video* (required):  file path, Camera video feed IP, integer for OpenCV Camera e.g 0, 1, 2
   - *min_confidence* (optional): 0.1 to 1.0
   - *codec* (optional): Default: cv2.VideoWriter_fourcc(*'mp4v')
   - *fps* (optional): frames per second
   - *continue_on_error* (optional):  Default: false
   - *output* (required): file path, cv2.VideoWriter
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 




Custom Object Detection
-----------------------

**1) Detect custom objects from image**

To create detection model to detect your custom objects, visit the `Custom Models <https://docs.deepstack.cc/custom-models/>`_ page.

For sample custom models, visit the `Sample Custom Models <https://docs.deepstack.cc/custom-models-samples/>`_ page.


.. figure:: https://github.com/OlafenwaMoses/DeepStack_OpenLogo/raw/main/images/fedex.jpg

.. code:: python

   from deepstack_sdk import ServerConfig, Detection

   config = ServerConfig("http://localhost:80")
   detection = Detection(config, name="openlogo")

   response = detection.detectObject("image.jpg",output="image_output.jpg")

   for obj in response:
      print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))


.. figure:: https://github.com/OlafenwaMoses/DeepStack_OpenLogo/raw/main/images/fedex_detected.jpg



**Available Parameters**:

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.

- **Detection()**
   - *config* (required): an instance of `ServerConfig`
   - *name* (required): name of the custom model file ( e.g `openlogo` if the custom model file name is **openlogo.pt** )

- **detectObject()**
   - *image* (required): file path, numpy array, PIL Image, image bytes, url
   - *format* (optional): jpg, png
   - *min_confidence* (optional): 0.1 to 1.0
   - *callback* (optional): function name, parses in image_byte [without label and boxes] and detections into the function
   - *output* (optional): file path of none if you don't want to save to file
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 



**2) Detect custom objects in video**


.. code:: python

   from deepstack_sdk import ServerConfig, Detection

   config = ServerConfig("http://localhost:80")
   detection = Detection(config, name="openlogo")

   detection.detectObjectVideo("video.mp4",output="video_output.mp4")



**Available Parameters**:

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.

- **Detection()**
   - *config* (required): an instance of `ServerConfig`
   - *name* (required): name of the custom model file ( e.g `openlogo` if the custom model file name is **openlogo.pt** )
   
- **detectObjectVideo()**
   - *video* (required):  file path, Camera video feed IP, integer for OpenCV Camera e.g 0, 1, 2
   - *min_confidence* (optional): 0.1 to 1.0
   - *codec* (optional): Default: cv2.VideoWriter_fourcc(*'mp4v')
   - *fps* (optional): frames per second
   - *continue_on_error* (optional):  Default: false
   - *output* (required): file path, cv2.VideoWriter
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 



Scene Recognition
-----------------

**1) Scene recognition in image**

.. code:: python

   from deepstack_sdk import ServerConfig, SceneRecognition

   config = ServerConfig("http://localhost:80")
   scene = SceneRecognition(config)

   response = scene.recognizeScene(r"scene_image.jpg")

   print("Scene: {} , Confidence: {}".format(response.label, response.confidence))


**Available Parameters**:

- **ServerConfig()**
   - *server_url* (required): DeepStack's URL with port
   - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
   - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.

- **recognizeScene()**
   - *image* (required): file path, numpy array, PIL Image, image bytes, url
   - *format* (optional): jpg, png
   - *callback* (optional):  function name, parses in image_byte [without label and boxes] and detections into the function


**2) Scene recognition in video**

.. code:: python

   from deepstack_sdk import ServerConfig, SceneRecognition

   config = ServerConfig("http://localhost:80")
   scene = SceneRecognition(config)

   response = scene.recognizeSceneVideo("video.mp4", output="scene.mp4")


**Available Parameters**:

- **ServerConfig()**
      - *server_url* (required): DeepStack's URL with port
      - *api_key* (optional): API key must be provided if DeepStack was initiated as stated in `Security: API Key <https://docs.deepstack.cc/security/index.html#setting-api-key>`_.
      - *admin_key* (optional): Admin key must be provided if DeepStack was initiated as stated in `Security: Admin Key <https://docs.deepstack.cc/security/index.html#setting-admin-keys>`_.
   
- **recognizeSceneVideo()**
   - *video* (required):  file path, Camera video feed IP, integer for OpenCV Camera e.g 0, 1, 2
   - *min_confidence* (optional): 0.1 to 1.0
   - *codec* (optional): Default: cv2.VideoWriter_fourcc(*'mp4v')
   - *fps* (optional): frames per second
   - *continue_on_error* (optional):  Default: false
   - *output* (required): file path, cv2.VideoWriter
   - *output_font* (optional): cv2 font
   - *output_font_color* (optional):  r, g, b 

.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
