.. image:: https://travis-ci.com/tobiasraabe/research_template.svg?branch=master
    :target: https://travis-ci.com/tobiasraabe/research_template

.. image:: https://pyup.io/repos/github/tobiasraabe/research_template/shield.svg
     :target: https://pyup.io/repos/github/tobiasraabe/research_template/
     :alt: Updates

Introduction
============

This repository lays out the structure for a research project and includes
useful helpers.

Todo
====

- Add cookiecutter support
- Add automation framework from Gaudecker

Managing the environment
========================

The framework relies on ``conda`` to manage the environment. To have support
for activation/deactivation with Powershell on Windows, type the following
command while staying in your base environment:

.. code-block:: bash

    $ conda install -c pscondaenvs pscondaenvs

You need ``conda`` to create the environment. Then, run

.. code-block:: bash

    $ conda env create -n <env-name> -f environment.yml

To activate the environment, type

.. code-block:: bash

    $ activate <env-name>

To delete the environment, type

.. code-block:: bash

    $ conda env remove -n <env-name>
