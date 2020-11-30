.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Custom Models
=================


While DeepStack provides many functionalities out of the box, it allows you to also deploy image recognition models trained on your own dataset.

For example, you can train a model on a dataset of different classes of plants. With **DeepStack**, you can deploy this model to actually classify plants in a production environment.

**DeepStack** supports custom image classification models in **ONNX**, **Tensorflow** and **Keras**. With the **ONNX** support, you can train a model in any deep learning framework including **Pytorch**, **MxNet**, **Chainer**, **CNTK** and more. and deploy them to production with **DeepStack**.

In this guide, we shall walk through deploying a custom model using the three supported formats. The model we are deploying here is trained to recognize different classes of professions by their mode of dressing.


Starting DeepStack on Docker
----------------------------

Below we start DeepStack with with no prebuilt API enabled, since we are using only custom models here.

**CPU Version**

.. code-block:: bash

    sudo docker run -v localstorage:/datastore -p 80:5000 \
    deepquestai/deepstack


**GPU Version**

.. code-block:: bash

    sudo docker run --gpus all -v localstorage:/datastore \
    -p 80:5000 deepquestai/deepstack:gpu


Starting DeepStack on Raspberry PI
----------------------------------

.. code-block:: bash

    sudo deepstack start "VISION-SCENE=True"


Starting DeepStack on Windows
-----------------------------

Start the **DeepStack App**, Click **Start Server**, deselect any selected API and click *Start Now*


Deploying ONNX Models with DeepStack
------------------------------------

ONNX is a universal model format supported by the most popular deep learning frameworks. A model trained in a framework like Pytorch can be easily exported to onnx.

**Step 1**

Download the trained `IdenProf <https://s3.us-east-2.amazonaws.com/commons-models/idenprof.onnx>`_ onnx model

**Step 2 - CONFIG File**

The configuration file contains all the information about the preprocessing and labels for your model.

.. code-block:: json

    {"sys-version": "1.0",
    "framework":"ONNX","mean":0.5,"std":255,"width":224,"height":224,
    "map": {"0": "chef", "1": "doctor", "2": "engineer", "3": "farmer",
    "4": "firefighter", "5": "judge", "6": "mechanic",
    "7": "pilot", "8": "police", "9": "waiter"}}


*Config Parameters*

**sys-version** This is a constant used internally by DeepStack.

**framework** This specifies the model format, supported values are ONNX, TF AND KERAS

**std** The input image is divided by this value, (Standard Deviation)

**mean** This is subtracted from the image after dividing by the std 

**map** This is a mapping of the class indexes to the actual labels.


**Step 3 : Register Your Model**

.. tabs:: 

    .. code-tab:: python

        import requests
        from io import  open

        model = open("idenprof.onnx","rb").read()
        config = open("config.json","rb").read()

        response = requests.post("http://localhost:80/v1/vision/addmodel",
        files={"model":model,"config":config},data={"name":"profession"}).json()
        print(response)
    
    .. code-tab:: js

        const request = require("request")
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
                var model = File.OpenRead("idenprof.onnx");
                var config = File.OpenRead("config.json");
                request.Add(new StreamContent(model),"model",Path.GetFileName("idenprof.onnx"));
                request.Add(new StreamContent(config),"config",Path.GetFileName("config.json"));
                request.Add(new StringContent("profession"),"name");
                var output = await client.PostAsync("http://localhost:80/v1/vision/addmodel",request);
                var jsonString = await output.Content.ReadAsStringAsync();

                Console.WriteLine(jsonString);

            }


            static void Main(string[] args){

                makeRequest().Wait();

            }

            }

        }

The code above, uploads the model and the config file to your local DeepStack server, also, the **{'name':'profession'}** specifies the unique name for the model. This model will be served on the endpoint **http://localhost:80/v1/vision/custom/profession**


**Restart DeepStack and your model will start serving**

Testing Your Custom Model
-------------------------

.. figure:: ../static/farmer.jpg

Below, we shall attempt to use our custom model to predict the class of the image below

.. tabs::

    .. code-tab:: python

        import requests

        image_data = open("test-custom-image.jpg","rb").read()

        response = requests.post("http://localhost:80/v1/vision/custom/profession",
        files={"image":image_data}).json()
        print("Label:",response["label"])
        print(response)
    
    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")

        image_stream = fs.createReadStream("test-custom-image.jpg")

        var form = {"image":image_stream}

        request.post({url:"http://localhost:80/v1/vision/custom/profession", formData:form},function(err,res,body){

            response = JSON.parse(body)
            console.log(response)
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

            public static async Task makeRequest(){

                var request = new MultipartFormDataContent();
                var image_data = File.OpenRead("test-custom-image.jpg");
                request.Add(new StreamContent(image_data),"image",Path.GetFileName("test-custom-image.jpg"));
                var output = await client.PostAsync("http://localhost:80/v1/vision/custom/profession",request);
                var jsonString = await output.Content.ReadAsStringAsync();

                Console.WriteLine(jsonString);

            }

            static void Main(string[] args){

                makeRequest().Wait();

            }

            }

        }

**Response**

.. code-block:: json

    {'label': 'farmer', 'success': True, 'confidence': 0.584346}


Deploying Keras Models with DeepStack
-------------------------------------

Keras is a popular deep learning framework focussed on ease of use.

Deploying keras models follows the same process as onnx models.

**Step 1**

You can download the keras model here `Idenprof Keras Model <https://s3.us-east-2.amazonaws.com/commons-models/idenprof.h5>`_.

*Note that when using your custom keras models, the model file must contain both the weights and the architecture*.

In your keras code, you can save the weights and architecture by using

.. code-block:: python

    model.save("model.h5")


**Step 2 :The config file**

The config file is essentially the same, except that the framework should be changed to KERAS

.. code-block:: json

    {"sys-version": "1.0",
    "framework":"KERAS","mean":0.5,"std":255,"width":224,"height":224,
    "map": {"0": "chef", "1": "doctor", "2": "engineer", "3": "farmer",
    "4": "firefighter", "5": "judge", "6": "mechanic",
    "7": "pilot", "8": "police", "9": "waiter"}}

*Config Parameters*


**sys-version** This is a constant used internally by DeepStack.

**framework** This specifies the model format, supported values are ONNX, TF AND KERAS

**std** The input image is divided by this value, (Standard Deviation)

**mean** This is subtracted from the image after dividing by the std 

**map** This is a mapping of the class indexes to the actual labels.


Now, we can register the model in the same way.

.. tabs::

    .. code-tab:: python

        import requests
        from io import  open

        model = open("idenprof.h5","rb").read()
        config = open("config.json","rb").read()

        response = requests.post("http://localhost:80/v1/vision/addmodel",
        files={"model":model,"config":config},data={"name":"profession"}).json()
        print(response)

    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")

        model = fs.createReadStream("idenprof.h5")
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
                var model = File.OpenRead("idenprof.h5");
                var config = File.OpenRead("config.json");
                request.Add(new StreamContent(model),"model",Path.GetFileName("idenprof.h5"));
                request.Add(new StreamContent(config),"config",Path.GetFileName("config.json"));
                request.Add(new StringContent("profession"),"name");
                var output = await client.PostAsync("http://localhost:80/v1/vision/addmodel",request);
                var jsonString = await output.Content.ReadAsStringAsync();

                Console.WriteLine(jsonString);

            }


            static void Main(string[] args){

                makeRequest().Wait();

            }

            }

        }


You can test your Keras model using the Example Code in previous section (Testing Your Custom Model)


Deploying Tensorflow Models with DeepStack
------------------------------------------

Tensorflow is a very popular DL framework from Google.

Deploying tensorflow models follows the same process as onnx and keras.

**Step 1**

You can download the tensorflow model here `Idenprof Tensorflow Model <https://s3.us-east-2.amazonaws.com/commons-models/idenprof.pb>`_


**Step 2 : The config file**

The config file for tensorflow models must contain the **input_name** and the **output_name**

.. code-block:: json

    {"sys-version": "1.0",
    "framework":"TF","mean":0.5,"std":255,"width":224,"height":224,
    "input_name":"input_1:0","output_name":"output_1:0",
    "map": {"0": "chef", "1": "doctor", "2": "engineer", "3": "farmer",
    "4": "firefighter", "5": "judge", "6": "mechanic",
    "7": "pilot", "8": "police", "9": "waiter"}}

*Config Parameters*

**sys-version** This is a constant used internally by DeepStack.

**framework** This specifies the model format, supported values are ONNX, TF AND KERAS

**input_name** The name of the input node in the Tensorflow model

**output_name** The name of the output node in the Tensorflow model

**std** The input image is divided by this value, (Standard Deviation)

**mean** This is subtracted from the image after dividing by the std 

**map** This is a mapping of the class indexes to the actual labels.

Now, we can register the model in the same way.

**Step 3 : Register Your Model**

.. tabs::

    .. code-tab:: python

        import requests
        from io import  open

        model = open("idenprof.pb","rb").read()
        config = open("config.json","rb").read()

        response = requests.post("http://localhost:80/v1/vision/addmodel",
        files={"model":model,"config":config},data={"name":"profession"}).json()
        print(response)

    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")

        model = fs.createReadStream("idenprof.pb")
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
                var output = await client.PostAsync("http://localhost:80/v1/vision/addmodel",request);
                var jsonString = await output.Content.ReadAsStringAsync();

                Console.WriteLine(jsonString);

            }


            static void Main(string[] args){

                makeRequest().Wait();

            }

            }

        }

You can test your Tensorflow model using the Example Code in previous sections (Testing Your Custom Model)

**NOTE**

Unlike the prebuilt APIs, custom models are auto started the moment you run DeepStack. When you add, delete or update a model, you need to restart the server for these changes to take effect.


Deleting Custom Models
----------------------

You can delete registered custom models as shown below.

.. code-block:: python

    import requests

    response = requests.post("http://localhost:80/v1/vision/deletemodel",
    data={"name":"profession"}).json()
    print(response)

These works the same for ONNX, Tensorflow and Keras models. 

For the delete to come into effect, you need to restart deepstack.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
