Anaconda on Windows
===================

This cookiecutter is designed to work with `Anaconda <https://anaconda.org/>`_ , a
scientific Python distribution for managing environments and packages. Especially for
Windows users this made everything much easier as pre-compiled packages are distributed
with Anaconda's own packages manager conda. However, the programming community is still
extremely focused on use cases with Linux or MacOS and sometimes things get harder for
us Windows users. Therefore, the following is a step-by-step installation and user guide
for Anaconda on Windows.

Installation
------------

1. Download the latest graphical installer from `anaconda.org
   <https://www.anaconda.com/distribution/>`_. If you do not know whether you need the
   32-bit or 64-bit installer, look at this `FAQ
   <https://support.microsoft.com/en-us/help/15056/windows-32-64-bit-faq>`_.

2. Start the installer. Choose whether to install Anaconda for all users which requires
   administrator privileges or for a single user. I prefer to install Python system-wide
   so it is available to all users. But then, you have to be careful as every time you
   interact with the base environment you have to use an elevated shell (a shell with
   administrator privileges.)

3. Tick "Add Anaconda to my PATH environment variable" and also "Register Anaconda as my
   default Python 3.x". Finish installation.

Which console?
--------------

The Powershell is the preferred way console on Windows as it provides a better interface
and better tab-completion. Unlike CMD and "Anaconda Prompt" it is not really supported.
The activation and deactivation of environments is broken. For that, we have to install
an additional packages. If you installed Anaconda with administrator privileges, start a
powershell as described `here
<https://www.digitalcitizen.life/ways-launch-powershell-windows-admin>`_. Then, type

.. code-block:: bash

    $ conda install pscondaenvs -c pscondaenvs

How to interact with the base environment?
------------------------------------------

The base environment is activated by default which means if you start a Powershell and
type python, you use the Python interpreter and the packages from the base environment.

My personal advice is to touch the base environment only if you want to do some small
programming or prototyping. In all other cases, create a separate environment.

The only two other things you can do here is to upgrade your base environment or conda.
Start a Powershell (with administrator privileges if you installed Anaconda for all
users). Type

.. code-block:: bash

    $ conda update conda

to update the package manager.

.. warning::

    Be aware that sometimes the developers of conda distribute buggy versions which
    usually forces you to reinstall Anaconda completely. Still, I recommend to upgrade
    from time to time. If you are extremely cautious, check the `latest versions
    <https://github.com/conda/conda/releases>`_ and update only if the latest version is
    a week old.

Then, update Anaconda with

.. code-block:: bash

    $ conda update anaconda

How to interact with an environments?
-------------------------------------

As I said before, I recommend to create a new environment for each of your projects. If
you do not know which packages you need later, start with a plain Python environment and
install packages along the way. Create a plain Python environment with

.. code-block:: bash

    $ conda create python=3.7 -c anaconda

or from a file with

.. code-block:: bash

    $ conda env create -n <env-name> -f <path-to-yml>

If you leave out the name, conda takes the name from the ``environment.yml``. If you
leave out the file, conda looks for a ``environment.yml`` in the current folder.

To install a package type

.. code-block:: bash

    $ conda install statsmodels=0.9.0

and to update

    .. code-block:: bash

        $ conda update statsmodels

To make your projects reproducible, you have to define an ``environment.yml``.

.. code-block:: bash

    $ conda env export -f environment.yml

Exporting the environment is one but maybe not the best way to create the environment
file. I would recommend that you do it yourself and add only packages you are importing
directly. The reason is that you only want to ensure that the results hold for the
specific versions of the main packages and you do not care about how they are using
their dependencies. An example looks like this:

.. code-block:: yaml

    # content of environment.yml
    name: cc
    channels:
        - defaults
        - pscondaenvs
    dependencies:
        - pscondaenvs=1.2.4
        - python=3.7
        - pip:
          - pandas==0.24.1

``name`` is the shortcut used to activate the environment later. ``channels`` contains
different sources for installing packages in order. During installation conda iterates
through the channels from top to bottom and looks for the specific package. In
``dependencies`` one can see first packages installed via conda. Notice the single
equality sign to pin a specific version. Under ``pip`` you can see a list of packages
which should be installed with pip. Here, you pin a package with two equality signs. I
would recommend to install as many packages with pip as possible, e.g. pandas, but not
Numpy, statsmodels, scikit-learn. First, every package is always up-to-date on PyPi, but
sometimes distributing to Anaconda takes longer. Second, pyup can only inform you about
updates under pip.

If you export the environment, there is a second entry after each package installed with
conda. The hashes make sure that packages have the same build instructions, but they are
not only compiler but also OS-specific. Thus, you cannot install a hashed package on
Windows and Linux.

What if you want to update the environment with a changed ``environment.yml``.

.. code-block:: bash

    $ conda env update -n <env-name> -f <path-to-yml>

Again, you can leave out ``-n`` and ``-f`` if the name is specified in the file or if
the file is in the current directory.

To remove an environment, use

.. code-block:: bash

    $ conda env remove -n <env-name>

The rest of the commands can be found in the `official conda documentation
<https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_.
