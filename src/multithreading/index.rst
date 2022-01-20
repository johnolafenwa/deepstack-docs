.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Multithreading
==============

By default, previous versions of DeepStack ran each endpoint on a single thread, this was changed to 5 threads in version 2022.01.1. To take full advantage of multiple cpu cores and threads,
DeepStack allows you to specify the number of threads each endpoint will run with. This provides singificant performance boost, 
especially when running multiple requests often.

Run DeepStack on Multiple Threads
-----------------------------------

Run the command below as it applies to the version you have installed

.. tabs::

  .. code-tab:: bash Docker CPU

    sudo docker run -e THREADCOUNT=10 -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack
  
  .. code-tab:: bash Docker GPU

    sudo docker run --gpus all run -e THREADCOUNT=10 -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu

  .. code-tab:: bash Windows OS

    deepstack --VISION-SCENE True --PORT 80 --THREADCOUNT 10
  
  .. code-tab:: bash NVIDIA Jetson

    sudo docker run -e THREADCOUNT=10 --runtime nvidia -e VISION-SCENE=True -p 80:5000 deepquestai/deepstack:jetpack

  .. code-tab:: bash ARM64

    sudo docker run -e THREADCOUNT=10 -e VISION-SCENE=True -p 80:5000 deepquestai/deepstack:arm64

  .. code-tab:: bash ARM64 Server

    sudo docker run -e THREADCOUNT=10 -e VISION-SCENE=True -p 80:5000 deepquestai/deepstack:arm64-server

The command **-e THREADCOUNT=10** sets the number of threads used by each endpoint to 10

.. toctree::
   :maxdepth: 2
   :caption: Contents:


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
