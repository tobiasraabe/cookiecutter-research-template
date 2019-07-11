Installation
============

This is a `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ template. To
use it, you need to install ``cookiecutter`` by running

.. code-block:: bash

    $ pip install cookiecutter

After that, you can quickly set up a new research project with this template by typing

.. code-block:: bash

    $ cookiecutter https://github.com/tobiasraabe/cookiecutter-research-template.git

Answer all the prompts and a folder ``cookiecutter-research-template`` is created in
your current directory. Rename the folder initialize a repository.

One of the last prompts is about whether the template should create a conda environment
from the pre-configured `environment.yml`. If that is not what you want, stick to the
default answer. You can fetch it later by running

.. code-block:: bash

    $ conda env create -f environment.yml -n <env-name>

Happy research!
