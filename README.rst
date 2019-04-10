.. raw:: html

    | <b><a href="https://github.com/tobiasraabe/cookiecutter-research-template#installation">Installation</a></b>
    | <b><a href="https://github.com/tobiasraabe/cookiecutter-research-template#features">Features</a></b>
    | <b><a href="https://cookiecutter-research-template.readthedocs.io/en/latest/index.html">Documentation</a></b>
    |

    <h1>cookiecutter-research-template</h1>

.. image:: https://travis-ci.com/tobiasraabe/cookiecutter-research-template.svg?branch=master
    :target: https://travis-ci.com/tobiasraabe/cookiecutter-research-template

.. image:: https://ci.appveyor.com/api/projects/status/6etx3nu4vqgr9f30/branch/master?svg=true
    :target: https://ci.appveyor.com/project/tobiasraabe/cookiecutter-research-template

.. image:: https://pyup.io/repos/github/tobiasraabe/cookiecutter-research-template/shield.svg
    :target: https://pyup.io/repos/github/tobiasraabe/cookiecutter-research-template/
    :alt: Updates

.. image:: https://readthedocs.org/projects/cookiecutter-research-template/badge/?version=latest
    :target: https://cookiecutter-research-template.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black


Introduction
------------

This repository lays out the structure for a reproducible research project based on the
Waf framework.

It is derived from https://github.com/hmgaudecker/econ-project-templates and the authors
of this project deserve all the credit for the implementation of Waf as a framework for
reproducible research. My contribution is to add several helpers around the project
which are common in software engineering and should help researchers to write better
code.


Installation
------------

This is a `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ template. Install it
by running

.. code-block:: bash

    $ pip install cookiecutter

After that, you can quickly set up a new research project with this template by
typing

.. code-block:: bash

    $ cookiecutter https://github.com/tobiasraabe/cookiecutter-research-template.git

Answer all the prompts and a folder ``<project-name>`` is created in your current
directory.

One of the last prompts is about whether the template should create a conda environment
from the pre-configured `environment.yml`. If that is not what you want, stick to the
default answer. You can fetch it later by running

.. code-block:: bash

    $ conda env create -f environment.yml -n <env-name>

At last, type

.. code-block:: bash

    $ conda activate <env-name>     # to activate the environment.
    $ git init                      # to initialize a git repository.
    $ pre-commit install            # to install pre-commit hooks.

Happy research!


Features
--------

The template offers several features:

Automatic dependency updates with `pyup <https://pyup.io>`_
    Connect your Github repository with https://pyup.io and you get automatic PRs if one
    of your dependency is outdated.

Automatic testing with `Travis <https://travis-ci.com>`_
    Connect your Github repository with https://travis-ci.com and the master branch and
    PRs are automatically tested and you can see the results online.

Testing with `tox <https://github.com/tox-dev/tox>`_
    Tox is a framework which allows you to define tests and run them in isolated
    environments. To run all tests defined in ``tox.ini``, hit

    .. code-block:: bash

        $ tox

Quality checks on commits with `pre-commit <https://pre-commit.com>`_
    pre-commit runs checks before every commit and aborts the process if a violation is
    found.

Code Formatting with `black`_ and `reorder-python-imports`_
    Both tools will quickly improve the code quality of your project. Just run

    .. code-block:: bash

        $ pre-commit run black reorder-python-imports --all-files (-a).

.. _black: https://github.com/ambv/black
.. _reorder-python-imports: https://github.com/asottile/reorder_python_imports

Linting
    Linting is the process of validating the syntax in code or documentation files. This
    template offers three ways to lint your project.

    ``flake8`` and its extensions check your Python files for potential errors,
    violations of naming conventions, ``TODO`` directives, etc.. To check your
    documentation files and other ``.rst`` files in your project, use ``doc8`` and
    ``restructuredtext-lint``. All three tests are included as pre-commits, but you can
    also run them with

    .. code-block:: bash

        $ pre-commit run flake8 doc8 restructuredtext-lint -a

    To test whether the documentation is built successfully, run

    .. code-block:: bash

        $ tox -e sphinx.

Customizing matplotlib
    If you are tired to set the same old options like ``figsize=(12, 8)`` for every
    graph, you are lucky. There is a solution called ``matplotlibrc`` (`predefined
    template <https://github.com/tobiasraabe/cookiecutter-
    research-template/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/src/
    figures/matplotlibrc>`_). This is a configuration file for matplotlib which lets you
    define the your personal defaults. The file resides in ``src/figures/matplotlibrc``
    and is copied over to ``bld`` as this is the root directory of the Python
    interpreter running your project. The ``matplotlibrc`` and its settings are
    automatically picked up. (`More information
    <https://matplotlib.org/users/customizing.html>`_.)

Downloading data for the project
    Data cannot be committed to the repository because the files are big and changing or
    because of confidentiality. ``prepare_data_for_project.py`` offers a way to download
    files, resume downloads and validate downloaded files. Add the file to ``FILES``
    with the filename on the disk as the key and the url as the first element of the
    list and the hash value as the second. Hashes are needed to validate that the
    downloaded file is identical the source. This seems unnecessarily nit-picky, but it
    takes ages to recognize that your source files are corrupt when you are debugging
    your project and look for typical mistakes.

Cleaning the project
    ``clean.py`` offers a way to clean your project from artifacts and unused files.
    Basically, it is a wrapper around `git clean`, but with more convenience.

    .. code-block:: bash

        $ python clean.py

    performs a dry-run, so you can be sure that only unnecessary files are deleted.
    Then, run

    .. code-block:: bash

        $ python clean.py --force

    to delete the files.

Visualization of the DAG
    A graphic of the DAG is compiled at the end of the Waf build process and serves as a
    nice picture of the complexity of the project (a little bit of bragging is ok
    :wink:) or allows for visual debugging.

    .. raw:: html

        <p align="center">
            <img src="docs/_static/dag.png">
        </p>

Others
    - `Waf Tips and Trick <https://github.com/tobiasraabe/cookiecutter-
      research-template/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/ WAF.rst>`_
    - Writing documentation with Jupyter notebooks (`nbsphinx
      <https://github.com/spatialaudio/nbsphinx>`_ )
    - Auxiliary scripts for figures in ``src/figures/auxiliaries.py``.
    - `Anaconda on Windows
      <https://cookiecutter-research-template.readthedocs.io/en/latest/
      anaconda-on-windows.html>`_
