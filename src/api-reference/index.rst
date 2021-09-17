.. DeepStack documentation master file, created by
   sphinx-quickstart on Wed Sep 15 17:20:18 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

API Reference
=============


This documentation contains reference for all endpoints available in DeepStack.



Face Detection
---------------


.. code-block::

   http://localhost:80/v1/vision/face



The face detection API detects faces and returns their coordinates. It functions similarly to the face recognition API except that it does not perform recognition.

.. tabs::

  .. tab:: parameters [POST]

    **image** ( *file* ): an image object


  .. code-tab:: json Response

    {
      'predictions': [{'x_max': 712, 'y_max': 261, 'x_min': 626, 'confidence': 0.99990666, 'y_min': 145},
      {'x_max': 620, 'y_max': 288, 'x_min': 543, 'confidence': 0.99986553, 'y_min': 174},
      {'x_max': 810, 'y_max': 242, 'x_min': 731, 'confidence': 0.99986434, 'y_min': 163},
      {'x_max': 542, 'y_max': 279, 'x_min': 477, 'confidence': 0.99899536, 'y_min': 197}],
      'success': True

    }

|

Face Registration
------------------



.. code-block::

   http://localhost:80/v1/vision/face/register



The face registration endpoint allows you to register pictures of person and associate it with a userid. You can specify multiple pictures per person during registration.


.. tabs::

  .. tab:: parameters [POST]

    **image**   ( *file* ): an image object

    **Name**  ( *string* ): a unique id or name


  .. code-tab:: json Response

    {
      'message': 'face added',
      'success': True
    }


|

Face Recognition
-----------------


.. code-block::

   http://localhost:80/v1/vision/face/recognize



The face recognition endpoint detects all faces in an image and returns the userid for each face. Note that the userid was specified during the registration phase. If a new face is encountered, the userid will be unknown.



.. tabs::

  .. tab:: parameters [POST]

    **image** ( *file* ): an image object


  .. code-tab:: json Response

    {
      'success': True,
      'predictions': [{'Name 1': 'Idris Elba', 'y_min': 154, 'x_min': 1615, 'x_max': 1983, 'confidence': 0.76965684, 'y_max': 682},
                     {'Name 2': 'Adele', 'y_min': 237, 'x_min': 869, 'x_max': 1214, 'confidence': 0.6044803, 'y_max': 732}
    }

|


.. code-block::

   http://localhost:80/v1/vision/face/list



The face recognition API allows you to retrieve and delete faces that have been previously registered with DeepStack.


.. tabs::

  .. tab:: parameters [POST]

    **image** ( *file* ): an image object


  .. code-tab:: json Response

    {
      'success': True,
      'faces': ['Tom Cruise', 'Adele', 'Idris Elba', 'Christina Perri']

    }



|

.. code-block::

   http://localhost:80/v1/vision/face/delete



The face recognition API allows you to ensure that a specific name faces that have been deleted with DeepStack.


.. tabs::

  .. tab:: parameters [POST]

     **Name**  ( *string* ): a unique id or name



  .. code-tab:: json Response

    {
      'success': True
    }


|

Face Match
-----------------


.. code-block::

   http://localhost:80/v1/vision/face/match


The face match api compares faces in two different pictures and tells the similarity between them. A typical use of this is matching identity documents with pictures of a person.


.. tabs::

  .. tab:: parameters [POST]

    **image** ( *file* ): an image object



  .. code-tab:: json Response

      {
       'similarity': 0.73975885,
       'success': True
      }


|


Object Detection
-----------------


.. code-block::

   http://localhost:80/v1/vision/detection


The object detection API locates and classifies 80 different kinds of objects in a single image.

.. tabs::

  .. tab:: parameters [POST]

    **image** ( *file* ): an image object



  .. code-tab:: json Response

    {
      'predictions': [{'x_max': 819, 'x_min': 633, 'y_min': 354, 'confidence': 99, 'label': 'dog', 'y_max': 546},
      {'x_max': 601, 'x_min': 440, 'y_min': 116, 'confidence': 99, 'label': 'person', 'y_max': 516},
      {'x_max': 445, 'x_min': 295, 'y_min': 84, 'confidence': 99, 'label': 'person', 'y_max': 514}],
      'success': True

    }


|

Scene Recognition
------------------


.. code-block::

   http://localhost:80/v1/vision/scene


The scene recognition api classifies an image into one of 365 scenes.

.. tabs::

  .. tab:: parameters [POST]

    **image** ( *file* ): an image object



  .. code-tab:: json Response

    {
         "success": True,
         "confidence": 0.7373981,
         "label": "Place"
    }

|


.. toctree::
   :maxdepth: 2
   :caption: Contents:




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
