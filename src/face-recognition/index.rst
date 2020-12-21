.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Face Recognition
================

In the `Getting Started <../getting-started/index.html>`_ , we had an overview of the face recognition API. In this section, we shall explore all the functionalities of the API.


Starting DeepStack on Docker
----------------------------

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
  
  .. code-tab:: bash Raspberry Pi

    sudo deepstack start "VISION-FACE=True"


*Basic Parameters*

**-e VISION-FACE=True** This enables the face recognition APIs.

**-v localstorage:/datastore** This specifies the local volume where DeepStack will store all data.

**-p 80:5000** This makes DeepStack accessible via port 80 of the machine.


Face Registration
-----------------

The face registration endpoint allows you to register pictures of person and associate it with a **userid**.
You can specify multiple pictures per person during registration.

**Example**

.. tabs::


   .. code-tab:: python

      import requests

      user_image1 = open("image1.jpg","rb").read()
      user_image2 = open("image2.jpg","rb").read()

      response = requests.post("http://localhost:80/v1/vision/face/register",
      files={"image1":user_image1,"image2":user_image2},data={"userid":"User Name"}).json()

      print(response)
   
   .. code-tab:: js

      const request = require("request")
      const fs = require("fs")

      run_prediction("image1.jpg","User Name")

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
            request.Add(new StreamContent(image_data),"image1",Path.GetFileName(image_path));
            request.Add(new StringContent(userid),"userid");
            var output = await client.PostAsync("http://localhost:80/v1/vision/face/register",request);
            var jsonString = await output.Content.ReadAsStringAsync();

            Console.WriteLine(jsonString);

         }

         static void Main(string[] args){

            registerFace("User Name ","userimage-path").Wait();

         }

      }

      }


**Response**

.. code-block:: json

   {'message': 'face added', 'success': True}


The response above indicates the call was successful. You should always check for the ** success ** status. If there is an error in your request, you will receive a response like

.. code-block:: json

   {'error': 'user id not specified', 'success': False}

This indicates that you omitted the userid in your request. If you omitted the image, the response will be

.. code-block:: json

   {'error': 'No valid image file found', 'success': False}


Face Recognition
-----------------

The face recognition endpoint detects all faces in an image and returns the **userid** for each face. Note that the **userid** was specified during the registration phase. If a new face is encountered, the **userid** will be unknown.

We shall test this on the image below.

.. figure:: ../static/idriselba2.jpg

.. tabs::

   .. code-tab:: python

      import requests

      image_data = open("test-image2.jpg","rb").read()

      response = requests.post("http://localhost:80/v1/vision/face/recognize",
      files={"image":image_data}).json()

      for user in response["predictions"]:
         print(user["userid"])

      print("Full Response: ",response)
   
   .. code-tab:: js

      const request = require("request")
      const fs = require("fs")

      image_stream = fs.createReadStream("test-image2.jpg")

      var form = {"image":image_stream}

      request.post({url:"http://localhost:80/v1/vision/face/recognize", formData:form},function(err,res,body){

         response = JSON.parse(body)
         predictions = response["predictions"]
         for(var i =0; i < predictions.length; i++){

            console.log(predictions[i]["userid"])

         }

         console.log(response)

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

            Console.WriteLine(jsonString);

         }

         static void Main(string[] args){

            recognizeFace("test-image2.jpg").Wait();

         }

      }

      }

.. code-block:: json

   Idris Elba
   unknown
   Full Response:  {'success': True, 'predictions': [{'x_min': 215, 'confidence': 0.76965684, 'x_max': 264, 'y_max': 91, 'y_min': 20, 'userid': 'Idris Elba'}, {'x_min': 115, 'confidence': 0, 'x_max': 162, 'y_max': 97, 'y_min': 31, 'userid': 'unknown'}]}


As you can see above, the first face is unknown since we did not previously register her, however, Idris Elba was detected as we registered a picture of him in the previous tutorial. Note also that the full response contains the coordinates of the faces.


Extracting Faces
----------------
The face coordinates allows you to easily extract the detected faces. Here we shall use PIL to extract the faces and save them

.. tabs::

   .. code-tab:: python

      import requests
      from PIL import Image

      image_data = open("test-image2.jpg","rb").read()
      image = Image.open("test-image2.jpg").convert("RGB")

      response = requests.post("http://localhost:80/v1/vision/face/recognize",
      files={"image":image_data}).json()

      for face in response["predictions"]:

         userid = face["userid"]
         y_max = int(face["y_max"])
         y_min = int(face["y_min"])
         x_max = int(face["x_max"])
         x_min = int(face["x_min"])
         cropped = image.crop((x_min,y_min,x_max,y_max))
         cropped.save("{}.jpg".format(userid))
   
   .. code-tab:: js

      const request = require("request")
      const fs = require("fs")
      const easyimage = require("easyimage")

      image_stream = fs.createReadStream("test-image2.jpg")

      var form = {"image":image_stream}

      request.post({url:"http://localhost:80/v1/vision/face/recognize", formData:form},function(err,res,body){

         response = JSON.parse(body)
         predictions = response["predictions"]
         for(var i =0; i < predictions.length; i++){
            pred = predictions[i]
            userid = pred["userid"]
            y_min = pred["y_min"]
            x_min = pred["x_min"]
            y_max = pred["y_max"]
            x_max = pred["x_max"]

            easyimage.crop(
                  {
                     src: "test-image2.jpg",
                     dst: userid+".jpg",
                     x: x_min,
                     cropwidth: x_max - x_min,
                     y: y_min,
                     cropheight: y_max - y_min,
                  }
            )
         }
      })
   
   .. code-tab:: c#

      using System;
      using System.IO;
      using System.Net.Http;
      using System.Threading.Tasks;
      using Newtonsoft.Json;
      using SixLabors.ImageSharp;
      using SixLabors.ImageSharp.Processing;
      using SixLabors.Primitives;

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

            var width = user.x_max - user.x_min;
            var height = user.y_max - user.y_min;

            var crop_region = new Rectangle(user.x_min,user.y_min,width,height);

            using(var image = Image.Load(image_path)){

                  image.Mutate(x => x
                  .Crop(crop_region)
                  );
                  image.Save(user.userid + ".jpg");

            }

         }

         }

         static void Main(string[] args){

            recognizeFace("test-image2.jpg").Wait();

         }

      }

      }


.. figure:: ../static/idriselba3.jpg

.. figure:: ../static/unknown.jpg


Setting Minimum Confidence
--------------------------

DeepStack recognizes faces by computing the similarity between the embedding of a new face and the set of embeddings of previously registered faces. By default, the minimum confidence is 0.67. The confidence ranges between 0 and 1. If the similarity for a new face falls below the min_confidence, unknown will be returned.

The min_confidence parameter allows you to increase or reduce the minimum confidence.

We lower the confidence allowed below.

.. tabs::

   .. code-tab:: python

      import requests

      image_data = open("test-image2.jpg","rb").read()

      response = requests.post("http://localhost:80/v1/vision/face/recognize",
      files={"image":image_data},data={"min_confidence":0.40}).json()

      for user in response["predictions"]:
         print(user["userid"])

      print("Full Response: ",response)
   
   .. code-tab:: js

      const request = require("request")
      const fs = require("fs")

      image_stream = fs.createReadStream("test-image2.jpg")

      var form = {"image":image_stream,"min_confidence":0.30}

      request.post({url:"http://localhost:80/v1/vision/face/recognize", formData:form},function(err,res,body){

         response = JSON.parse(body)
         predictions = response["predictions"]
         for(var i =0; i < predictions.length; i++){
            pred = predictions[i]
            console.log(pred["userid"])
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
         request.Add(new StringContent("0.30"),"min_confidence");
         var output = await client.PostAsync("http://localhost:80/v1/vision/face/recognize",request);
         var jsonString = await output.Content.ReadAsStringAsync();
         Response response = JsonConvert.DeserializeObject<Response>(jsonString);

         foreach (var user in response.predictions){

            Console.WriteLine(user.userid);

         }

         Console.WriteLine(jsonString);

      }

      static void Main(string[] args){

         recognizeFace("test-image2.jpg").Wait();

      }

      }

      }


.. code-block:: text

   Idris Elba
   Adele
   Full Response:  {'success': True, 'predictions': [{'userid': 'Idris Elba', 'y_min': 154, 'x_min': 1615, 'x_max': 1983, 'confidence': 0.76965684, 'y_max': 682}, {'userid': 'Adele', 'y_min': 237, 'x_min': 869, 'x_max': 1214, 'confidence': 0.6044803, 'y_max': 732}]}


By reducing the allowed confidence, the system detects the first face as Adele. The lower the confidence, the more likely for the system to make mistakes. When the confidence level is high, mistakes are extremely rare, however, the system may return unknown always if the confidence is too high.

**For security related processes such as authentication, set the min_confidence at 0.7 or higher** .


Managing Registered Faces
-------------------------

The face recognition API allows you to retrieve and delete faces that have been previously registered with DeepStack.

**Listing faces**

.. tabs::

   .. code-tab:: python

      import requests
      faces = requests.post("http://localhost:80/v1/vision/face/list").json()

      print(faces)
   
   .. code-tab:: js

      const request = require("request")

      request.post("http://localhost:80/v1/vision/face/list",function(err,res,body){

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

         public static async Task listFaces(){

            var output = await client.PostAsync("http://localhost:80/v1/vision/face/list",null);
            var jsonString = await output.Content.ReadAsStringAsync();

            Console.WriteLine(jsonString);

         }

         static void Main(string[] args){

            listFaces().Wait();

         }

      }

      }


**Response**

.. code-block:: json

   {'success': True, 'faces': ['Tom Cruise', 'Adele', 'Idris Elba', 'Christina Perri']}



**Deleting a face**

.. tabs::

   .. code-tab:: python

      import requests

      response = requests.post("http://localhost:80/v1/vision/face/delete",
      data={"userid":"Idris Elba"}).json()

      print(response)
   
   .. code-tab:: js

      const request = require("request")

      var form = {"userid":"Idris Elba"}

      request.post({url:"http://localhost:80/v1/vision/face/delete", formData:form},function(err,res,body){

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

         public static async Task registerFace(string userid){

            var request = new MultipartFormDataContent();
            request.Add(new StringContent(userid),"userid");
            var output = await client.PostAsync("http://localhost:80/v1/vision/face/delete",request);
            var jsonString = await output.Content.ReadAsStringAsync();

            Console.WriteLine(jsonString);

         }

         static void Main(string[] args){

            registerFace("Idris Elba").Wait();

         }

      }

      }

**Reponse**

.. code-block:: json

   {'success': True}

Having deleted Idris Elba from our database, we shall now attempt to recognize him in our test image.


.. tabs::

   .. code-tab:: python

      import requests

      image_data = open("test-image2.jpg","rb").read()

      response = requests.post("http://localhost:80/v1/vision/face/recognize",
      files={"image":image_data}).json()

      for user in response["predictions"]:
         print(user["userid"])
   
   .. code-tab:: js

      const request = require("request")
      const fs = require("fs")

      image_stream = fs.createReadStream("test-image2.jpg")

      var form = {"image":image_stream}

      request.post({url:"http://localhost:80/v1/vision/face/recognize", formData:form},function(err,res,body){

         response = JSON.parse(body)
         predictions = response["predictions"]
         for(var i =0; i < predictions.length; i++){
            pred = predictions[i]
            console.log(pred["userid"])
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

            recognizeFace("test-image2.jpg").Wait();

         }

      }

      }


**Response**

.. code-block:: text

   unknown
   unknown


Performance
-----------

DeepStack offers three modes allowing you to tradeoff speed for performance. During startup, you can specify performance mode to be , **High** , **Medium** and **Low**. 

The default mode is **Medium**.

You can specify a different mode during startup as seen below as seen below

.. tabs::

  .. code-tab:: bash Docker CPU

    docker run -e VISION-FACE=True -e MODE=High -v localstorage:/datastore -p 80:5000 deepquestai/deepstack
  
  .. code-tab:: bash Docker GPU

    sudo docker run --gpus all -e VISION-FACE=True -e MODE=High -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu

  .. code-tab:: bash Windows OS

    deepstack --VISION-FACE True --MODE High --PORT 80
  
  .. code-tab:: bash NVIDIA Jetson

    sudo docker run --runtime nvidia -e VISION-FACE=True -e MODE=High -p 80:5000 deepquestai/deepstack:jetpack


**Speed Modes are not available on the Raspberry PI Version**


.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
