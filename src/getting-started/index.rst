.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Getting Started
================

In this tutorial, we shall go through the complete process of using DeepStack to build a Face Recognition system.

Setting Up DeepStack
--------------------

Install and Setup DeepStack Using the `Install Guide <../index.html#installation-guide-for-cpu-version>`_ . If you have a system with Nvidia GPU, follow instruction on Using DeepStack with NVIDIA GPU to install the GPU Version of DeepStack


Starting DeepStack
------------------

Run the command below as it applies to the version you have installed

.. tabs::

  .. code-tab:: bash Docker CPU

    docker run -e VISION-FACE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack
  
  .. code-tab:: bash Docker GPU

    sudo docker run --gpus all -e VISION-FACE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu

  .. code-tab:: bash Windows OS

    deepstack --VISION-FACE True --PORT 80
  
  .. code-tab:: bash NVIDIA Jetson

    sudo docker run --runtime nvidia -e VISION-FACE=True -p 80:5000 deepquestai/deepstack:jetpack

 .. code-tab:: bash ARM64

    docker run -e VISION-FACE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:arm64
   
 .. code-tab:: bash ARM64 Server

    docker run -e VISION-FACE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:arm64-server
  
  .. code-tab:: bash Raspberry Pi

    sudo deepstack start "VISION-FACE=True"


*Basic Parameters*

**-e VISION-FACE=True** This enables the face recognition APIs.

**-v localstorage:/datastore** This specifies the local volume where deepstack will store all data.

**-p 80:5000** This makes deepstack accessible via port 80 of the machine.




Face Recognition
----------------

Think of a software that can identify known people by their names. Face Recognition does exactly that. Register a picture of a number of people and the system will be able to recognize them again anytime. Face Recognition is a two step process: The first is to register a known face and second is to recognize these faces in new pictures.


**REGISTERING A FACE**

Here we are building an application that can tell the names of a number of popular celebrities. First we collect pictures of a number of celebrities and we register them with **DeepStack**.


.. figure:: ../static/tomcruise.jpg

.. figure:: ../static/adele.jpg

.. figure:: ../static/idriselba.jpg

.. figure:: ../static/perri.jpg


Below we will register the faces with their names

.. tabs::

   .. code-tab:: python

      import requests

      def register_face(img_path,user_id):
         image_data = open(img_path,"rb").read()
         response = requests.post("http://localhost:80/v1/vision/face/register",
         files={"image":image_data}, data={"userid":user_id}).json()
         print(json)

      register_face("cruise.jpg","Tom Cruise")
      register_face("adele.jpg","Adele")
      register_face("elba.jpg","Idris Elba")
      register_face("perri.jpg","Christina Perri")
   
   .. code-tab:: js

      const request = require("request")
      const fs = require("fs")

      run_prediction("cruise.jpg","Tom Cruise")
      run_prediction("elba.jpg","Idris Elba")
      run_prediction("perri.jpg","Christina Perri")
      run_prediction("adele.jpg","Adele")

      function run_prediction(image_path,userid){

         image_stream = fs.createReadStream(image_path)

         var form = {"image":image_stream,"userid":userid}

         request.post({url:"http://localhost:80/v1/vision/face/register", formData:form},function(err,res,body){

            response = JSON.parse(body)
            console.log(response)

         })

      }
   
   .. code-tab:: c#

      using System;
      using System.IO;
      using System.Net.Http;
      using System.Threading.Tasks;

      namespace app
      {

      class App {

         static HttpClient client = new HttpClient();

         public static async Task registerFace(string userid, string image_path){

            var request = new MultipartFormDataContent();
            var image_data = File.OpenRead(image_path);
            request.Add(new StreamContent(image_data),"image",Path.GetFileName(image_path));
            request.Add(new StringContent(userid),"userid");
            var output = await client.PostAsync("http://localhost:80/v1/vision/face/register",request);
            var jsonString = await output.Content.ReadAsStringAsync();

            Console.WriteLine(jsonString);

         }

         static void Main(string[] args){

            registerFace("Tom Cruise","cruise.jpg").Wait();
            registerFace("Adele","adele.jpg").Wait();
            registerFace("Idris Elba","elba.jpg").Wait();
            registerFace("Christina Perri","perri.jpg").Wait();

         }

      }

      }



**RECOGNITION**

.. figure:: ../static/adele2.jpg

.. tabs::

   .. code-tab:: python

      import requests

      test_image = open("test-image.jpg","rb").read()

      res = requests.post("http://localhost:80/v1/vision/face/recognize",
      files={"image":test_image}).json()

      for user in res["predictions"]:
         print(user["userid"])
   
   .. code-tab:: js

      const request = require("request")
      const fs = require("fs")

      image_stream = fs.createReadStream("test-image.jpg")

      var form = {"image":image_stream}

      request.post({url:"http://localhost:80/v1/vision/face/recognize", formData:form},function(err,res,body){

         response = JSON.parse(body)
         predictions = response["predictions"]
         for(var i =0; i < predictions.length; i++){

         console.log(predictions[i]["userid"])

         }

      })
      
   .. code-tab:: c#

      using System;
      using System.IO;
      using System.Net.Http;
      using System.Threading.Tasks;
      using Newtonsoft.Json;


      namespace appone
      {

      class Response {

         public bool success {get;set;}
         public Face[] predictions {get;set;}

      }

      class Face {

         public string userid {get;set;}
         public float confidence {get;set;}
         public int y_min {get;set;}
         public int x_min {get;set;}
         public int y_max {get;set;}
         public int x_max {get;set;}

      }

      class App {

         static HttpClient client = new HttpClient();

         public static async Task recognizeFace(string image_path){

            var request = new MultipartFormDataContent();
            var image_data = File.OpenRead(image_path);
            request.Add(new StreamContent(image_data),"image",Path.GetFileName(image_path));
            var output = await client.PostAsync("http://localhost:80/v1/vision/face/recognize",request);
            var jsonString = await output.Content.ReadAsStringAsync();
            Response response = JsonConvert.DeserializeObject<Response>(jsonString);

            foreach (var user in response.predictions){

                  Console.WriteLine(user.userid);

            }

         }

         static void Main(string[] args){

            recognizeFace("test-image.jpg").Wait();

         }

      }

      }



**Response**

.. code-block:: text

   Adele


We have just created a face recognition system. You can try with different people and test on different pictures of them.

The `next tutorial <../face-recognition.html>`_ is dedicated to the full power of the face recognition api as well as best practices to make the best out of it.


Performance
-----------

DeepStack offers three modes allowing you to tradeoff speed for performance. During startup, you can specify performance mode to be , **High** , **Medium** and **Low**.

The default mode is **Medium**

You can specify a different mode during startup as seen below.

**CPU Version**

.. code-block:: bash

   sudo docker run -e MODE=High -e VISION-FACE=True -v localstorage:/datastore \
   -p 80:5000 deepquestai/deepstack

**GPU Version**

.. code-block:: bash

   sudo docker run --rm --runtime=nvidia -e MODE=High -e VISION-FACE=True \
   -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu

Note the **-e MODE=High** above.


.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
