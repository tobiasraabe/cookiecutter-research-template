Travis-CI
=========

Travis-CI is a service which allows you to test and deploy your projects. We
are only interested in the first aspect, testing, as Travis-CI allows us to run
a complete battery of tests every time a new commit is made on the master
branch or every time a pull-request is updated. This ensures that we are
gradually improving the project and do not introduce bugs or style issues in
areas where we already have tests.

Broadly speaking, there are two categories of tests we are implementing in a
research project. The first category is about testing our data to ensure that
the source files are the same, intermediate results did not change, etc.. Most
of the time, researchers are bounded by confidentiality agreements to keep
their data private. In this case you cannot use Travis-CI to test your data
and you need to skip this part of the testing battery.

The second category of tests concerns the code which does not normally fall
under the former constraint and can be given into the hands of private company.


Installation
------------

To enable testing on travis-ci.com, go to https://travis-ci.com and choose log
in with Github in the upper right corner. Then, you have to agree that
Travis-CI is allowed to have access to your repositories. There is nothing to
do afterwards as Travis-CI will automatically check your repositories for a
``.travis.yml`` which includes all the build information.

To get an impression of a configuration file, take the following example of the
Travis-CI configuration of this template.

.. literalinclude:: ../.travis.yml

- ``notifications`` lets you define whether you want to be notified if a tests
  fails for some commit. My personal opinion is to disable notifications as
  they will flood your email inbox. You can also send notifications to Slack or
  other services.
- ``language`` defines the main language of your project. Depending on this
  choice, there are several other tools pre-installed.
- ``python`` sets the Python version of your test environment. The default is
  3.6, but you are free to change. Furthermore, you can test your project
  against multiple python versions by using:

  .. code-block:: yaml

      python:
        - 3.5
        - 3.6

  Note that for each Python version a different build is created meaning the
  same tests would run in a Python 3.5 and 3.6 environment in parallel.

The next three steps define the `build lifecycle <https://docs.travis-ci.com/
user/customizing-the-build/>`_. There are several ways to differentiate between
different stages of the build process. Here is one.

- In ``before_install`` we download pandoc to be able to use the latex builder
  for our documenation.
- In ``install`` we make sure that tox is installed and has the latest version
  to run our tests.
- In ``script`` we actually run the tests. As mentioned before, if you only
  want to run a subset of tests defined in tox, change the config to

  .. code-block:: yaml

      install:
        - tox -e flake8
        - tox -e black

  or something similar. Maybe you want to exclude ``pytest`` as some tests
  depend on data. In this case, I would recommend that you still include
  ``pytest`` and `mark tests which cannot succeed for different reasons
  <https://docs.pytest.org/en/latest/skipping.html>`_.

- ``branches`` includes a current fix so that commits on PRs are not built
  twice.

There are a lot of things you can do. See `this document <https://docs.travis-
ci.com/user/customizing-the-build/>`_ if need to have a different
configuration.
