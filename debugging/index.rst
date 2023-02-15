.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Debugging
==============

DeepStack logs all errors that may occur, in a case where your requests are returning 500 error codes, you can check the error logs as Below

DeepStack Docker
================
When running DeepStack docker versions, do the following

Step 1: Get the DeepStack container name 

.. code-block:: bash

  sudo docker ps

Step 2: Open a terminal in the Container

.. code-block:: bash

  sudo docker exec -it container-name /bin/bash 

Step 3: CD to the logs folder and Open Error Logs

.. code-block:: bash

  cd /app/logs && cat stderr.txt

This will open the file stderr.txt and would contain information about what went wrong in DeepStack

DeepStack Windows
==================
When running the windows version of DeepStack, do the following

You will find the file stderr.txt in C:/Users/username/AppData/Local/DeepStack

.. toctree::
   :maxdepth: 2
   :caption: Contents:


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
