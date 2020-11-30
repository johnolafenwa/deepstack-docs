.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Face Match
==========

The face match api compares faces in two different pictures and tells the similarity between them. A typical use of this is matching identity documents with pictures of a person. 

**Example**

.. figure:: ../static/obama1.jpg

.. figure:: ../static/obama2.jpg

.. tabs::

    .. code-tab:: python

        import requests

        image_data1 = open("obama1.jpg","rb").read()
        image_data2 = open("obama2.jpg","rb").read()

        response = requests.post("http://localhost:80/v1/vision/face/match",files={"image1":image_data1,"image2":image_data2}).json()

        print(response)
    
    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")

        image_stream1 = fs.createReadStream("obama1.jpg")
        image_stream2 = fs.createReadStream("obama2.jpg")

        var form = {"image1":image_stream1,"image2":image_stream2}

        request.post({url:"http://localhost:80/v1/vision/face/match", formData:form},function(err,res,body){

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
                var image_data1 = File.OpenRead("obama1.jpg");
                var image_data2 = File.OpenRead("obama2.jpg");
                request.Add(new StreamContent(image_data1),"image1",Path.GetFileName("test-image6.jpeg"));
                request.Add(new StreamContent(image_data2),"image2",Path.GetFileName("test-image7.jpg"));
                var output = await client.PostAsync("http://localhost:80/v1/vision/face/match",request);
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

    {'similarity': 0.73975885, 'success': True}

**Example 2**

Here we shall compare a picture of Obama with that of Bradley Cooper.


.. figure:: ../static/obama1.jpg

.. figure:: ../static/brad.jpg

.. tabs::

    .. code-tab:: python

        import requests

        image_data1 = open("obama2.jpg","rb").read()
        image_data2 = open("brad.jpg","rb").read()

        response = requests.post("http://localhost:80/v1/vision/face/match",files={"image1":image_data1,"image2":image_data2}).json()

        print(response)
    
    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")

        image_stream1 = fs.createReadStream("obama2.jpeg")
        image_stream2 = fs.createReadStream("brad.jpg")

        var form = {"image1":image_stream1,"image2":image_stream2}

        request.post({url:"http://localhost:80/v1/vision/face/match", formData:form},function(err,res,body){

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
                var image_data1 = File.OpenRead("obama2.jpg");
                var image_data2 = File.OpenRead("brad.jpg");
                request.Add(new StreamContent(image_data1),"image1",Path.GetFileName("test-image6.jpeg"));
                request.Add(new StreamContent(image_data2),"image2",Path.GetFileName("test-image8.jpg"));
                var output = await client.PostAsync("http://localhost:80/v1/vision/face/match",request);
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

    {{'similarity': 0.4456827, 'success': True}

As seen above, the match for two different pictures of Obama was very high while the match for Obama and Bradley Cooper was very low.


Performance
-----------

DeepStack offers three modes allowing you to tradeoff speed for performance. During startup, you can specify performance mode to be , **High** , **Medium** and **Low**. 

The default mode is **Medium**.

You can specify a different mode during startup as seen below as seen below

**CPU Version**

.. code-block:: bash

   sudo docker run -e MODE=High VISION-FACE=True -v localstorage:/datastore -p 80:5000 \
   deepquestai/deepstack


**GPU Version**

.. code-block:: bash

   sudo docker run --gpus all -e MODE=High -e VISION-FACE=True -v localstorage:/datastore \
   -p 80:5000 deepquestai/deepstack:gpu


Note the **-e MODE=High** above

On Windows, you can easily select the High mode in the UI.

.. figure:: ../static/windows-mode.jpg

Note the **High** radio button selected above.

**Speed Modes are not available on the Raspberry PI Version**




.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
