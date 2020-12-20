.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Scene Recognition
=================

The scene recognition api classifies an image into one of 365 scenes.

To use this API, you need to enable the scene API when starting DeepStack.


Starting DeepStack on Docker
----------------------------

Below we start DeepStack with only the Scene APIs enabled.

**CPU Version**

.. code-block:: bash

    sudo docker run -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 \
    deepquestai/deepstack


**GPU Version**

.. code-block:: bash

    sudo docker run --gpus all -e VISION-SCENE=True -v localstorage:/datastore \
    -p 80:5000 deepquestai/deepstack:gpu


Starting DeepStack on other Platforms
-------------------------------------

`DeepStack on Windows (CPU and GPU) <windows>`_

`DeepStack on Raspberry PI <raspberry-pi>`_



**Example**

.. figure:: ../static/office.jpg

.. tabs::

   .. code-tab:: python

      import requests

      image_data = open("office.jpg","rb").read()

      response = requests.post("http://localhost:80/v1/vision/scene",files={"image":image_data}).json()
      print("Label:",response["label"])
      print(response)
   
   .. code-tab:: js

      const request = require("request")
      const fs = require("fs")

      image_stream = fs.createReadStream("office.jpg")

      var form = {"image":image_stream}

      request.post({url:"http://localhost:80/v1/vision/scene", formData:form},function(err,res,body){

         response = JSON.parse(body)
         console.log(response)
      })
   
   .. code-tab:: c#

      using System;
      using System.IO;
      using System.Net.Http;
      using System.Threading.Tasks;


      namespace app
      {

         class App {

         static HttpClient client = new HttpClient();

         public static async Task makeRequest(){

            var request = new MultipartFormDataContent();
            var image_data = File.OpenRead("office.jpg");
            request.Add(new StreamContent(image_data),"image",Path.GetFileName("office.jpg"));
            var output = await client.PostAsync("http://localhost:80/v1/vision/scene",request);
            var jsonString = await output.Content.ReadAsStringAsync();

            Console.WriteLine(jsonString);

         }

         static void Main(string[] args){

            makeRequest().Wait();

         }

         }

      }



**Response**

.. code-block:: text

   Label: conference_room
   {'success': True, 'confidence': 0.7373981, 'label': 'conference_room'}




.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
