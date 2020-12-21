.. deepstack-python documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Face Detection
==============

The face detection API detects faces and returns their coordinates. It functions similarly to the face recognition API except that it does not perform recognition.

**Example**

.. figure:: ../static/family.jpg

.. tabs::

    .. code-tab:: python

        import requests

        image_data = open("family.jpg","rb").read()

        response = requests.post("http://localhost:80/v1/vision/face",files={"image":image_data}).json()

        print(response)
    
    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")

        image_stream = fs.createReadStream("family.jpg")

        var form = {"image":image_stream}

        request.post({url:"http://localhost:80/v1/vision/face", formData:form},function(err,res,body){

            response = JSON.parse(body)
            predictions = response["predictions"]

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

            public string gender {get;set;}
            public float confidence {get;set;}
            public int y_min {get;set;}
            public int x_min {get;set;}
            public int y_max {get;set;}
            public int x_max {get;set;}

        }

        class App {

            static HttpClient client = new HttpClient();

            public static async Task detectFace(string image_path){

                var request = new MultipartFormDataContent();
                var image_data = File.OpenRead(image_path);
                request.Add(new StreamContent(image_data),"image",Path.GetFileName(image_path));
                var output = await client.PostAsync("http://localhost:80/v1/vision/face",request);
                var jsonString = await output.Content.ReadAsStringAsync();
                Response response = JsonConvert.DeserializeObject<Response>(jsonString);

                Console.WriteLine(jsonString);

            }

            static void Main(string[] args){

                detectFace("family.jpg").Wait();

            }

        }

        }

**Response**

.. code-block:: json

    {'predictions': [{'x_max': 712, 'y_max': 261, 'x_min': 626, 'confidence': 0.99990666, 'y_min': 145}, {'x_max': 620, 'y_max': 288, 'x_min': 543, 'confidence': 0.99986553, 'y_min': 174}, {'x_max': 810, 'y_max': 242, 'x_min': 731, 'confidence': 0.99986434, 'y_min': 163}, {'x_max': 542, 'y_max': 279, 'x_min': 477, 'confidence': 0.99899536, 'y_min': 197}], 'success': True}

We can use the coordinates returned to extract the faces from the image.

.. tabs::

    .. code-tab:: python

        import requests
        from PIL import Image

        image_data = open("family.jpg","rb").read()
        image = Image.open("family.jpg").convert("RGB")

        response = requests.post("http://localhost:80/v1/vision/face",files={"image":image_data}).json()
        i = 0
        for face in response["predictions"]:

            y_max = int(face["y_max"])
            y_min = int(face["y_min"])
            x_max = int(face["x_max"])
            x_min = int(face["x_min"])
            cropped = image.crop((x_min,y_min,x_max,y_max))
            cropped.save("image{}.jpg".format(i))

            i += 1

    .. code-tab:: js

        const request = require("request")
        const fs = require("fs")
        const easyimage = require("easyimage")

        image_stream = fs.createReadStream("family.jpg")

        var form = {"image":image_stream}

        request.post({url:"http://localhost:80/v1/vision/face", formData:form},function(err,res,body){

            response = JSON.parse(body)
            predictions = response["predictions"]
            for(var i =0; i < predictions.length; i++){

                pred = predictions[i]
                gender = pred["gender"]
                y_min = pred["y_min"]
                x_min = pred["x_min"]
                y_max = pred["y_max"]
                x_max = pred["x_max"]

                easyimage.crop(
                    {
                    src: "family.jpg",
                    dst: i.toString() + "_.jpg",
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

        public string gender {get;set;}
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
            var output = await client.PostAsync("http://localhost:80/v1/vision/face",request);
            var jsonString = await output.Content.ReadAsStringAsync();
            Response response = JsonConvert.DeserializeObject<Response>(jsonString);

            var i = 0;

            foreach (var user in response.predictions){

                var width = user.x_max - user.x_min;
                var height = user.y_max - user.y_min;

                var crop_region = new Rectangle(user.x_min,user.y_min,width,height);

                using(var image = Image.Load(image_path)){

                    image.Mutate(x => x
                    .Crop(crop_region)
                    );
                    image.Save(i.ToString() + "_.jpg");

                }

                i++;

            }

            }

            static void Main(string[] args){

                recognizeFace("family.jpg").Wait();

            }

        }

        }
    
    

.. figure:: ../static/family1.jpg

.. figure:: ../static/family2.jpg

.. figure:: ../static/family3.jpg

.. figure:: ../static/family4.jpg




.. toctree::
   :maxdepth: 2
   :caption: Contents:


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
