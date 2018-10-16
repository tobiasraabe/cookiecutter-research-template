Usage
-----

After the installation, here is the manual for running the project.

Waf
^^^

The general research project must be configured in advance with

.. code-block:: bash

    $ python waf.py configure

Make sure that all steps pass successfully. Otherwise determine what is
missing, fix it and rerun the command. After that, run

.. code-block:: bash

    $ python waf.py (build)

where ``build`` is optional, but it executes the same action. If you want to
delete everything created in ``bld`` and restart the project from the source
files, run

.. code-block:: bash

    $ python waf.py distclean configure


Formatting
^^^^^^^^^^

Making the code readable is as easy as typing

.. code-block:: bash

    $ python format_python_files.py

and all the files will be formatted according to the configuration of ``black``
and ``isort``.


Testing
^^^^^^^

Before committing changes, make sure that everything works fine. Run

.. code-block:: bash

    $ tox

and the whole test suite will be run.
