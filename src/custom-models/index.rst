.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Custom Models
=================

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/wQKUQ6Y2n3Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   
DeepStack provides a simple API to detect common objects in images and videos. The Object detection API supports 80 objects. Often your use case might involve objects that DeepStack doesn't natively support, or you might want to finetune the object detection for your own kind of images, probably cctv images or night images if the built in object detection API doesn't work perfectly enough for you.
For this, you can train a new model on your own images and deploy that to DeepStack.

The video above provides end to end guide to doing this.

Here we shall go over the full process of preparing your image dataset, training and deploying with DeepStack.

Step 1: `Prepare Your Dataset <datasetprep>`_

Step 2: `Train Your Model <training>`_

Step 3: `Deploy Your Model <deployment>`_

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   datasetprep/index
   training/index
   deployment/index

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`