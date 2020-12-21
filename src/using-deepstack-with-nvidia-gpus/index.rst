.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Using DeepStack with NVIDIA GPUs
================================

DeepStack GPU Version serves requests 5 - 20 times faster than the CPU version if you have an NVIDIA GPU.

 **NOTE: THE GPU VERSION IS ONLY SUPPORTED ON LINUX, WINDOWS SUPPORT IS COMING SOON.**

Before you install the GPU Version, you need to follow the steps below.


Step 1: Install Docker
----------------------

If you already have docker installed, you can skip this step.

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install curl
    curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

Step 2: Setup NVIDIA Drivers
----------------------------

Install the NVIDIA Driver

`Nvidia Driver Install <http://www.linuxandubuntu.com/home/how-to-install-latest-nvidia-drivers-in-linux/>`_


Step 3: Install NVIDIA Container Toolkit
----------------------------------------

Run the commands below

.. code-block:: bash

    # Add the package repositories
    distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

    sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
    sudo systemctl restart docker

If you run into issues, you can refer to this `GUIDE <https://github.com/NVIDIA/nvidia-docker>`_

Step 4: Install DeepStack GPU Version
-------------------------------------

.. code-block:: bash

    sudo docker pull deepquestai/deepstack:gpu

If you are running an old system without modern cpu instructions such as AVX, please use the **Legacy System Version**


Step 5: RUN DeepStack with GPU Access
-------------------------------------

Once the above steps are complete, when you run deepstack, add the args **–gpus all**

.. code-block:: bash

    sudo docker run --gpus all -e VISION-SCENE=True -v localstorage:/datastore \
    -p 80:5000 deepquestai/deepstack:gpu


*Basic Parameters*

**--gpus all** This enables gpu access to the DeepStack container

**-e VISION-SCENE=True** This enables the scene recognition API, all apis are disabled by default.

**-v localstorage:/datastore** This specifies the local volume where DeepStack will store all data.

**-p 80:5000** This makes DeepStack accessible via port 80 of the machine.

Once installed, run the example scene recognition code to verify your installation is working.

RUN with All APIs
------------------

You can run DeepStack with all the APIs enabled. Use the command below

.. code-block:: bash

    sudo docker run --gpus all -e VISION-SCENE=True -e VISION-DETECTION=True -e VISION-FACE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu


.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
