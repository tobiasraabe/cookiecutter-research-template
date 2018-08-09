.. image:: https://travis-ci.com/tobiasraabe/cookiecutter-research-template.svg?branch=master
    :target: https://travis-ci.com/tobiasraabe/cookiecutter-research-template

.. image:: https://pyup.io/repos/github/tobiasraabe/cookiecutter-research-template/shield.svg
    :target: https://pyup.io/repos/github/tobiasraabe/cookiecutter-research-template/
    :alt: Updates

Introduction
============

This repository lays out the structure for a reproducible research project
based on the Waf framework.

It is derived from https://github.com/hmgaudecker/econ-project-template and the
authors of this project deserve all the credit for the implementation of Waf as
a framework for reproducible research. My contribution in this project is to
add several helpers around the project which are common in software engineering
and should help researchers to write better code.


Installation
============

This is a `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ template.
To use it, you need to install ``cookiecutter`` by running

.. code-block:: bash

    $ pip install cookiecutter

After that, you can quickly set up a new research project with this template by
typing

.. code-block:: bash

    $ cookiecutter https://github.com/tobiasraabe/cookiecutter-research-template.git

Answer all the questions and a folder with your research template is created.
Rename the folder to your liking and initialize a repo within. Happy research!


Features
========

The template offers several features:

Automatic dependency update with `pyup <https://pyup.io>`_
    Connect your Github repository with pyup.io and you get automatic PRs if
    one of your dependency is outdated.

Automatic testing with `Travis <https://travis-ci.com>`_
    Connect your Github repository with travis-ci.com and the master branch and
    PRs are automatically tested and you can see the results online.

Testing with `tox <https://github.com/tox-dev/tox>`_
    Tox is a framework which allows you to define tests and run them in
    isolated environments. To run all tests defined in ``tox.ini``, hit

    .. code-block:: bash

        $ tox

Code Formatting with `black <https://github.com/ambv/black>`_ and `isort <https://github.com/timothycrosley/isort>`_
    Both tools will quickly improve the code quality of your project. Just run

    .. code-block:: bash

        $ python format_python_files.py

    and black will improve your code whereas isort will change the order of
    imports in a more readable way.

Linting
    Linting is the process of checking the syntax in code or documentation
    files for errors. This template offers three ways to lint your project.

    ``flake8`` and its extensions check your Python files for potential errors,
    violations of naming conventions, warn of ``TODO`` directives, etc.. Run
    the tests with

    .. code-block:: bash

        $ tox -e flake8


    To check your documentation files and other ``.rst`` files in your project,
    run

    .. code-block:: bash

        $ tox -e docs

    To test whether the documentation is built successfully, run

    .. code-block:: bash

        $ tox -e sphinx

Customizing matplotlib
    If you are tired to set the same old options like ``figsize=(12, 8)`` for
    every graph, you are lucky. There is a solution called ``matplotlibrc``.
    This is a configuration file for matplotlib which lets you define the
    defaults. The file resides in ``src/figures/matplotlibrc`` and is copied
    over to ``bld`` as this is the root directory of the Python interpreter
    running your project. The ``matplotlibrc`` and its settings are
    automatically picked up. (`More information
    <https://matplotlib.org/users/customizing.html>`_.)

Downloading data for the project
    Data cannot be committed with the repository on Github because of
    confidentiality or because the files are to big.
    ``prepare_data_for_project.py`` offers a way to download files, resume
    downloads and validate downloaded files. Add the file to ``FILES`` with the
    filename on the disk as the key and the url as the first element of the
    list and the hash value as the second. Hashes are needed to validate that
    the downloaded file is identical the source. This seems unnecessary and
    nit-picky, but it takes ages to recognize that your source files changed
    when you are debugging your project and look for usual mistakes.

Cleaning the project
    ``clean.py`` offers a way to clean your project from artifacts and unused
    files. Running

    .. code-block:: bash

        $ python clean.py

    performs a dry-run, so you can be sure that only useless files are deleted.
    Then, run

    .. code-block:: bash

        $ python clean.py --force

    to actually delete the files.

Others
    - `Waf Tips and Tricks <https://github.com/tobiasraabe/cookiecutter-research-
      template/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/WAF.rst>`_
    - Writing documentation with Jupyter notebooks (`nbsphinx
      <https://github.com/spatialaudio/nbsphinx>`_ )
    - Beautiful visualization of the project's DAG.
    - Auxiliary scripts for figures in ``src/figures/auxiliaries.py``.
