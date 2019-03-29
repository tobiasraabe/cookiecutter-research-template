How to debug the project
::::::::::::::::::::::::

When we want to debug our research project, we often want to run a single file within
the Waf framework repeatedly or we even want to dive into the debugger if an error
occurs. Normally, this is not possible as Waf controls the execution and places the
``bld`` or ``src`` on the ``PYTHONPATH``. Thus, if we execute a single file, an
``ImportError`` is raised. Adding the paths manually seems a little bit hacky and can be
circumvented much more elegantly. In addition to that, even if we insert a debug
statement in the file and the code reaches this line, Waf hides the prompt of the
debugger from the user. Then, it will silently run forever as the debugger is never
closed an execution continued.

Make ``bld`` and ``src`` importable
-----------------------------------

To place ``bld`` and ``src`` on ``PYTHONPATH`` we turn the project into a python
package. This can be accomplished by placing a file called ``setup.py`` in the root
directory of the project. This file is the entry point for every other Python package
you have ever installed with ``pip``. The file for our project contains only necessary
information as we will never upload our research project on PyPi. Here is what the file
looks like:

.. code-block:: python

    from setuptools import setup


    setup(
        name="project_name",
        packages=["bld", "src"]
    )

That is all. ``name`` is the name of the package which we can use to install or remove
the package. ``packages`` lists directories which will be added to ``PYTHONPATH``.

To install the package, we do **not** use ``pip install .`` as this will install the
package in its current form. Instead, we would like that the installed package changes
with our changes to the project. This can be done by making an editable install of the
package which registers our project as a moving target. For the editable install, go
into the root folder of the project where the ``setup.py`` lies and type

.. code-block:: bash

    $ pip install -e .

That is all. Now, you can run every single file withing the project.


Debugging
---------

As an example, let's say we have a file called ``src/data_management/create_dataset.py``
with the following content:

.. code-block:: python

    from bld.project_paths import project_paths_join as ppj


    def main():
        df = pd.read_stata(ppj("IN_DATA", "example.dta"))

        df.AGE = df.AGE.astype(int)

        df.to_pickle(ppj("OUT_DATA", "example.pkl"))


    if __name__ == "__main__":
        main()

The file loads ``example.dta``, turns variable ``AGE`` into an integer and saves the
file as a pickle object. Assume that running the program raises an error as the variable
``AGE`` is not defined in the data and is instead called ``ALTER`` (german word for
age). Then, Waf aborts the execution and returns a more or less readable report of the
error which is in this case quite clear. How can we jump into the debugger to inspect
the state of the program?

The first method is to insert a debug statement before the error occurs. Starting with
Python 3.7 this is even more simple.

.. code-block:: python

    ...

    def main():
        df = pd.read_stata(ppj("IN_DATA", "example.dta"))

        import pdb; pdb.set_trace()  # For Python < 3.7

        breakpoint()  # For Python >= 3.7

        df.AGE = df.AGE.astype(int)

    ...

Then, you can start to debug your program. For more information on how to use the Python
debugger ``pdb`` visit this `tutorial <https://realpython.com/python-debugging-pdb/>`_.

The second method to start the debugger is directly from the command line. Type

.. code-block:: bash

    $ python -m pdb -c continue src/data_management/create_dataset.py

to enter the debugger if an exception occurs. If you leave out ``-c continue`` you will
jump into the debugger right at the start.


Using a different debugger
--------------------------

The default debugger is not really visually appealing. Instead we can use `ipdb
<https://github.com/gotcha/ipdb>`_  which is the IPython debugger with tab-completion,
syntax highlighting, etc.. Install it with

.. code-block:: bash

    $ pip install ipdb

Then, use it with ``import ipdb; ipdb.set_trace()`` or register it as the default
debugger for ``breakpoint()`` by setting the environment variable

.. code-block:: bash

    $ export PYTHONBREAKPOINT=ipdb.set_trace  # Unix

    $ $env:PYTHONBREAKPOINT="ipdb.set_trace" # Windows

Or just run the file with ``ipdb`` by running

.. code-block:: bash

    python -m ipdb -c continue src/data_management/create_dataset.py
