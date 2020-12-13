.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Training Your Dataset
=======================
The [DeepStack Trainer](https://github.com/johnolafenwa/deepstack-trainer) provides all of the functions needed to train on your local machine
or in the cloud.
Once your dataset is prepared, you can use any of the options below to train your model 

Option 1: Training on Google Colab with Free GPUS
==================================================
This is the recommended option unless you have a computer with Nvidia GPUS.
Simply click the link below to train your model. All needed instructions are included.

[DeepStack Trainer Colab Notebook](https://colab.research.google.com/drive/1gbTr_4xpDk3cpnbAVbMVxtyp-3XuUPix?usp=sharing)

Option 2: Training Locally
==========================
To do this, ensure your system has a CUDA capable Nvidia GPU.

Step 1 : Install CUDA and CUDNN
--------------------------------
If you don't already have cuda and cudnn, install them 
* [Install CUDA](https://developer.nvidia.com/cuda-downloads)
* [Install CUDNN](https://developer.nvidia.com/cudnn)

Step 2 : Install Pytorch
-------------------------
Install the latest Version of Pytorch, visit https://pytorch.org for install instructions,
ensure you select your version of CUDA on the install page

Step 3 : Clone DeepStack Trainer
----------------------------------
Now, you are done installing the pre-requisites, clone the DeepStack trainer

.. code-block:: bash

   git clone https://github.com/johnolafenwa/deepstack-trainer

Once cloned, CD to the DeepStack trainer repo 

Step 4: Run your Training
--------------------------

.. code-block:: bash

   python3 train.py --dataset-path "/path-to/my-dataset"

When you start training your model, you will find a folder created on the path, ```train-runs/my-dataset/exp/weights```, 
If you run your training multiple times, you will find exp1, exp2 folders and so on as you run, each folder corresponding to each run, the first run is just exp

As your training progresses, you will find the best.pth file in the ```weights``` folder above, for best results, you can wait till the end 
of your training to copy the file. This is the file you will deploy with DeepStack.


Important Parameters
--------------------

The following parameters can be set to optimize your model to suit you better

* ```--model``` DeepStack trainer supports five model types, in order of increasing accuracy they are ```"yolov5s"```, ```"yolov5m"```, ```"yolov5l"```, ```"yolov5x"```. The default is yolov5m, the highest accuracy onces like yolov5l and yolov5x are much slower and will require higher end compute to deploy. The fastest yolov5s is highly recommended if deploying on the nvidia jetson. 

* ```--batch-size``` This is the number of images processed at once, you can set this to a higher number like 32 or 64 as your gpu memory allows, if you use a gpu with lower memory, you can set this to a lower number like 8 or less if you run into memory problems. The default value is 16

* ```epochs``` This is the number of iterations over your entire dataset, the default value is 300. You can always run with lesser epochs or more epochs, accuracy increases as you run more epochs.
