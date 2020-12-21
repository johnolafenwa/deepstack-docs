.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Security
========

DeepStack allows you to protect your api endpoints with keys to prevent unauthorized access.

You can set two types of keys: **API Key** and **Admin Key**.

The API Key protects all recognition and detection endpoints including face, scene, object detection and custom models. The admin key protects admin apis such as adding models, deleting models, list models, backup and restore.


Setting API Key
---------------

Run the command below as it applies to the version you have installed

.. tabs::

  .. code-tab:: bash Docker CPU

    sudo docker run -e API-KEY=Mysecretkey -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack
  
  .. code-tab:: bash Docker GPU

    sudo docker run --gpus all -e API-KEY=Mysecretkey -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu

  .. code-tab:: bash Windows OS

    deepstack --VISION-SCENE True --PORT 80 --API-KEY Mysecretkey
  
  .. code-tab:: bash NVIDIA Jetson

    sudo docker run -e API-KEY=Mysecretkey --runtime nvidia  -e VISION-SCENE=True -p 80:5000 deepquestai/deepstack:jetpack
  
  .. code-tab:: bash Raspberry Pi

    sudo deepstack start "VISION-SCENE=True API-KEY=Mysecretkey"


The command **-e API-KEY=Mysecretkey** sets **Mysecretkey** as the api key.

Below we shall attempt to classify the scene of the image below without specifying the key.

.. tabs::

    .. code-tab:: python

        import requests

        image_data = open("test-image10.jpg","rb").read()

        response = requests.post("http://localhost:80/v1/vision/scene",
        files={"image":image_data}).json()
        print(response)
    
    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")

        image_stream = fs.createReadStream("test-image10.jpg")

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
                var image_data = File.OpenRead("test-image5.jpg");
                request.Add(new StreamContent(image_data),"image",Path.GetFileName("test-image5.jpg"));
                var output = await client.PostAsync("http://localhost:80/v1/vision/scene",request);
                var jsonString = await output.Content.ReadAsStringAsync();

                Console.WriteLine(jsonString);

            }

            static void Main(string[] args){

                makeRequest().Wait();

            }

            }

        }


**Response:**

.. code-block:: json

    {'success': False, 'error': 'Incorrect api key'}

As seen above, the prediction fails returning incorrect api key.

Below, we make the request with the api key specified

.. tabs::

    .. code-tab:: python

        import requests

        image_data = open("test-image10.jpg","rb").read()

        response = requests.post("http://localhost:80/v1/vision/scene",
        files={"image":image_data}, data={"api_key":"Mysecretkey"}).json()
        print(response)
    
    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")

        image_stream = fs.createReadStream("test-image10.jpg")

        var form = {"image":image_stream,"api_key":"Mysecretkey"}

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
                var image_data = File.OpenRead("test-image5.jpg");
                request.Add(new StreamContent(image_data),"image",Path.GetFileName("test-image5.jpg"));
                request.Add(new StringContent("Mysecretkey"),"api_key");
                var output = await client.PostAsync("http://localhost:80/v1/vision/scene",request);
                var jsonString = await output.Content.ReadAsStringAsync();

                Console.WriteLine(jsonString);

            }

            static void Main(string[] args){

                makeRequest().Wait();

            }

            }

        }

**Response:**

.. code-block:: json

    {'success': True, 'label': 'hospital_room', 'confidence': 0.4538608}


Setting Admin keys
------------------

Admin keys are set similarly to API Keys, see example below.

You can specify the admin key during startup of deepstack.


Run the command below as it applies to the version you have installed

.. tabs::

  .. code-tab:: bash Docker CPU

    sudo docker run -e ADMIN-KEY=Secretadminkey -e API-KEY=Mysecretkey -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack
  
  .. code-tab:: bash Docker GPU

    sudo docker run --gpus all -e ADMIN-KEY=Secretadminkey -e API-KEY=Mysecretkey -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack:gpu

  .. code-tab:: bash Windows OS

    deepstack --VISION-SCENE True --PORT 80 --API-KEY Mysecretkey --ADMIN-KEY Secretadminkey
  
  .. code-tab:: bash NVIDIA Jetson

    sudo docker run -e ADMIN-KEY=Secretadminkey -e API-KEY=Mysecretkey --runtime nvidia  -e VISION-SCENE=True -p 80:5000 deepquestai/deepstack:jetpack

  .. code-tab:: bash Raspberry Pi

    sudo deepstack start "VISION-SCENE=True ADMIN-KEY=Secretadminkey API-KEY=Mysecretkey"



The command **-e ADMIN-KEY=Secretadminkey sets** **Secretadminkey** as the admin key. In this example, the API key is also set, note that you can set either without setting the other.


Once you set an Admin key, you need to specify it when making admin calls such as backup, restore and model management.

Example below is for adding models.

.. tabs::

    .. code-tab:: python

        import requests
        from io import  open

        model = open("idenprof.pb","rb").read()
        config = open("config.json","rb").read()

        response = requests.post("http://localhost:80/v1/vision/addmodel",
        files={"model":model,"config":config},data={"name":"profession","admin_key":"Secretadminkey"}).json()

    .. code-tab:: js

        iconst request = require("request")
        const fs = require("fs")

        model = fs.createReadStream("idenprof.onnx")
        config = fs.createReadStream("config.json")

        var form = {"model":image_stream, "config":config,"name":"profession"}

        request.post({url:"http://localhost:80/v1/vision/addmodel", formData:form},function(err,res,body){

            response = JSON.parse(body)
            predictions = response["predictions"]

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
                var model = File.OpenRead("idenprof.pb");
                var config = File.OpenRead("config.json");
                request.Add(new StreamContent(model),"model",Path.GetFileName("idenprof.pb"));
                request.Add(new StreamContent(config),"config",Path.GetFileName("config.json"));
                request.Add(new StringContent("profession"),"name");
                request.Add(new StringContent("Secretadminkey"),"admin_key");
                var output = await client.PostAsync("http://localhost:80/v1/vision/addmodel",request);
                var jsonString = await output.Content.ReadAsStringAsync();

                Console.WriteLine(jsonString);

            }


            static void Main(string[] args){

                makeRequest().Wait();

            }

            }

        }
        

.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
