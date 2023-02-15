.. DeepStack documentation master file, created by
   sphinx-quickstart on Sun Nov  8 22:05:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Backup
======

You can backup your DeepStack data including registered faces and custom models. At any time, you can restore your data back.

Backups
-------

The code below downloads your entire DeepStack data as a single zip file

.. code-block:: python

    import requests
    from io import  open
    import shutil

    data = requests.post("http://localhost:80/v1/backup",stream=True)

    with open("backupdeepstack.zip", "wb") as file:
        shutil.copyfileobj(data.raw, file)
    del data


Restore
-------

The code below restores your DeepStack data from a saved backup.

.. code-block:: python

    import requests
    from io import  open
    import time

    image_data = open("backupdeepstack.zip","rb").read()

    response = requests.post("http://localhost:80/v1/restore",files={"file":image_data}).json()
    print(response)


.. toctree::
   :maxdepth: 2
   :caption: Contents:



* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
