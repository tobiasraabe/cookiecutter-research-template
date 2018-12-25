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


Quality Checks
^^^^^^^^^^^^^^

The quality of the code base is ensured by `pre-commit-hooks
<https://pre-commit.com>`_  which are automatically executed before changes are
committed. If a check fails, the commit is aborted. To install the hooks, type

.. code-block:: bash

    $ pre-commit install

After that, run

.. code-block:: bash

    $ pre-commit run --all-files

to execute the checks without making a commit. Currently, the following hooks
are installed:

- `black - The Uncomprimising Python Formatter
  <https://github.com/ambv/black>`_
- `blacken-docs - Black for Documentation
  <https://github.com/asottile/blacken-docs>`_
- `flake8 - Linting <https://gitlab.com/pycqa/flake8>`_
- `isort - Sorting Python Imports <https://github.com/timothycrosley/isort>`_
- `doc8 <https://github.com/openstack/doc8>`_
- `check-yaml - Validating .yaml files
  <https://github.com/pre-commit/pre-commit-hooks>`_


Testing
^^^^^^^

Before committing changes, make sure that everything works fine. Run

.. code-block:: bash

    $ tox

and the whole test suite will be run.
