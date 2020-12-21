.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Using DeepStack on Raspberry PI - ALPHA
=======================================

DeepStack on Rasperry PI makes it easier to develop and deploy embedded smart applications. This is a lighter version but with full support for all of deepstack's features including Object Detection, Face APIs, Scene Recognition. 

*Custom ONNX, Tensorflow, Keras and Openvino models support will be included in the BETA version.*

Note that due to the limited compute capacity of the Raspberry PI, DeepStack requires an `Intel Neural Compute Stick <https://ark.intel.com/content/www/us/en/ark/products/140109/intel-neural-compute-stick-2.html>`_ **(NCS)**



.. figure:: ../static/movidius.jpeg

The PI Version is in alpha and would be regularly improved for optimal performance.

Minimum System Requirements

- Raspberry PI 3B+
- Intel Movidius Neural Compute Stick 2

Installing DeepStack
--------------------

.. code-block:: bash

    wget https://deepquest.sfo2.digitaloceanspaces.com/deepstack/install-deepstack.sh

    install-deepstack.sh

DeepStack on the raspberry pi depends on **python3.5** or **Python3.7** installed.

Using DeepStack
---------------

Due to a number of factors, running DeepStack on the PI is slightly different.

Below are the various ways to run DeepStack. Ensure the NCS is plugged in before running DeepStack.

**Running with Scene Recognition**

.. code-block:: bash

    sudo deepstack start "VISION-SCENE=True"


**Running with Object Detection**

.. code-block:: bash

    sudo deepstack start "VISION-DETECTION=True"

**Running with Face APIs**

.. code-block:: bash

    sudo deepstack start "VISION-FACE=True"


Stopping DeepStack
------------------

.. code-block:: bash

    sudo deepstack stop


Using Custom Ports
------------------

DeepStack by default runs on port **80** you can run it on your choice port using the syntax below.

.. code-block:: bash

    sudo deepstack start "VISION-SCENE=True PORT=8080"

Limitations
-----------

- Only one api type can be run at once, for example, you would encounter errors if you attempt to run both **Object Detection** and **Face** at the same time.

- Custom Models are not supported at present, support for this would be added in the BETA release.

- Only One instance of DeepStack can be run at present, running a new instance would close the other , this is enforced due to limitations of the Neural Compute Stick.

- Use of Multiple NCSs is not yet supported. Only one can be used in this release.


Known Issues
------------

**DeepStack Not Responding :** This might occur if you start DeepStack without the NCS plugged in or you sometimes when you stop and rerun DeepStack. In any case, simply restart your Raspberry PI, plug in the NCS and start DeepStack. 

**Invalid Image :** This can occur if you send a very high resolution image, about 2000px * 2000px, to the **object detection** or **face** APIs. 

.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
