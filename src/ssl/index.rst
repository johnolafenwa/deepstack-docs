.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SSL Support
============

From version *2022.01.1* , you can now run DeepStack with SSL support, ensuring all API connections to DeepStack are encrypted and secured.


Create a Certificate
--------------------
First, you need to create a valid SSL certificate for a Domain with which you will access DeepStack. (SKIP THIS STEP IF YOU ALREADY HAVE A CERTIFICATE)



-  You can create a free certificate with **Let's Encrypt** as detailed in this `tutorial <https://dzone.com/articles/create-wildcard-ssl-certificate-with-lets-encrypt>`_ or by using another certificate authority (CA). The supported certificate format for DeepStack is **.pem**. 
-  Once you have the certificate files, save the certificate file as `fullchain.pem` and `key.pem`


Run DeepStack with SSL
----------------------

Take the following steps to run DeepStack with SSL

-  Create a directory and move the certificate files into this directory
-  Run the command below to mount this directory to DeepStack


.. tabs::

  .. code-tab:: bash Docker CPU

    sudo docker run -e VISION-DETECTION=True -v localstorage:/datastore -v absolute/path/to/certificate-directory:/cert -p 443:443 deepquestai/deepstack
  
  .. code-tab:: bash Docker GPU

    sudo docker run --gpus all -e VISION-DETECTION=True -v localstorage:/datastore -v absolute/path/to/certificate-directory:/cert -p 443:443 deepquestai/deepstack:gpu

  .. code-tab:: bash Windows OS

    deepstack --VISION-DETECTION True --CERT-PATH absolute/path/to/certificate-directory --PORT 443
  
  .. code-tab:: bash NVIDIA Jetson

    sudo docker run --runtime nvidia -e VISION-DETECTION=True -v absolute/path/to/certificate-directory:/cert -p 443:443 deepquestai/deepstack:jetpack


*Basic Parameters*

**-v absolute/path/to/certificate-directory:/cert** This mounts the directory where the certificate files are to DeepStack.

**-p 443:443** This specifies the port with which DeepStack will run with SSL support. By default, DeepStack uses port 443 internal when valid SSL certificates are provided. You can map another port to the internal 443 but it is recommended you keep the mapping port 443:443.


- To confirm DeepStack is running via HTTPS, visit **https://localhost** or **https://machine-ip**. And look at the certificate information from the padlock sign. You will find the domain in the certificate information.
    - **NB:** Browsers and HTTP clients might reject sending your request to DeepStack API if you don't map the corresponding domain to the machine IP, because of mismatch of the certificate's domain and the machine IP.



.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
