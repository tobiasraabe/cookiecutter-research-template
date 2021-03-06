{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if cookiecutter.add_azure == "yes" %}.. image:: https://dev.azure.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/_apis/build/status/{{ cookiecutter.github_username }}.{{ cookiecutter.project_slug }}?branchName=master
    :target: https://dev.azure.com/{{ cookiecutter.github_username }}/cookiecutter-research-template/_build/latest?definitionId=1&branchName=master
{% endif %}
{% if cookiecutter.add_pyup == "yes" %}.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
    :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
    :alt: Updates
{% endif %}
{% if cookiecutter.add_readthedocs == "yes" %}.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
    :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
{% endif %}
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black


`TODO <src/documentation/TODO.rst>`_
------------------------------------


Managing the environment
------------------------

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


Enforce quality checks befire every commit
------------------------------------------

You can automatically enforce quality checks before every commit by using
``pre-commit``. Run

.. code-block:: bash

    pre-commit install

to install the checks and

.. code-block:: bash

    pre-commit run

to run the checks manually.


Credits
-------

This package was created with Cookiecutter_ and the
`tobiasraabe/cookiecutter-research-template`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`tobiasraabe/cookiecutter-research-template`:
   https://github.com/tobiasraabe/cookiecutter-research-template
