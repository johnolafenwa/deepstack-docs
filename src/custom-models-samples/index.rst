.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Custom Models: Samples
======================

This page contains a list of custom models that has been trained and made publicly available by other DeepStack users and the DeepStack team. 

You can use any of the models listed below to detect the corresponding objects it is trained for. All you need to do is download the custom model's **.pt** file and deploy it as `detailed here <https://docs.deepstack.cc/custom-models/deployment>`_.

You can also contribute models you have trained by creating an issues on the `DeepStack's GitHub repository <https://github.com/johnolafenwa/deepstack>`_ and include the following in the issue's description

   - purpose of the custom model
   - object(s) that can be detected
   - link to the **.pt** file of the model.
   - link to a GitHub repository or post on the model [optional]



1. Licence Plate Detection
--------------------------

.. figure:: https://deepquest.sfo2.digitaloceanspaces.com/deepstackdev/docs/images/license-plate.png

This model is trained to detect Norwegian licence plates, but is tested with various other plates and are working with those.

   - Created by: `Odd <https://github.com/odd86>`_
   - Purpose: License Plate Detection
   - Model Type: YOLOv5

Pre-trained Model on GitHub: `https://github.com/odd86/deepstack_licenceplate_model <https://github.com/odd86/deepstack_licenceplate_model>`_


2. Logo Detection
-----------------

.. figure:: https://github.com/OlafenwaMoses/DeepStack_OpenLogo/raw/main/images/fedex_detected.jpg

This model is trained to detect all 352 logos in the `OpenLogo dataset <https://qmul-openlogo.github.io/>`_.

   - Created by: `DeepQuestAI <http://deepstack.cc/>`_
   - Purpose: Common Logo Detection
   - Model Type: YOLOv5x

Pre-trained Model on GitHub: `DeepStack_OpenLogo <https://github.com/OlafenwaMoses/DeepStack_OpenLogo>`_


3. Dark/Night scene objects Detection
-------------------------------------

.. figure:: https://github.com/OlafenwaMoses/DeepStack_ExDark/raw/main/images/1.jpg

This model is trained to detect 12 common objects in images and videos from Dark/Night scenes. This model was trained on the `ExDark Dataset <https://github.com/cs-chan/Exclusively-Dark-Image-Dataset>`_.

   - Created by: `DeepQuestAI <http://deepstack.cc/>`_
   - Purpose: Detecting common objects in dark/night images and videos
   - Model Type: YOLOv5x

Pre-trained Model on GitHub: `DeepStack_ExDark <https://github.com/OlafenwaMoses/DeepStack_ExDark>`_


4. Human action Detection/Recognition
-------------------------------------

.. figure:: https://github.com/OlafenwaMoses/DeepStack_ActionNET/raw/main/images/test4_detected.jpg

This model is trained to detect/recognize **16 human actions** in images and videos. This model was trained on the `ActionNET Dataset <https://github.com/OlafenwaMoses/Action-Net>`_.

   - Created by: `DeepQuestAI <http://deepstack.cc/>`_
   - Purpose: Detecting 16 human actions in images and videos
   - Model Type: YOLOv5x

Pre-trained Model and Dataset on GitHub: `DeepStack_ActionNET <https://github.com/OlafenwaMoses/DeepStack_ActionNET>`_


.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
