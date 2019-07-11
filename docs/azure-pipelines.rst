Azure-Pipelines
===============

Azure-Pipelines is a service which allows you to test and deploy your projects. We are
only interested in the first aspect, testing, as Azure-Pipelines allows us to run a
complete battery of tests every time a new commit is made on the master branch or every
time a pull-request is updated. This ensures that we are gradually improving the project
and do not introduce bugs or style issues in areas where we already have tests. Also, we
can run the test battery on the three major operating system, Linux, MacOS and Windows.

Broadly speaking, there are two categories of tests we are implementing in a research
project. The first category is about testing our data to ensure that the source files
are the same, intermediate results did not change, etc.. Most of the time, researchers
are bounded by confidentiality agreements to keep their data private. In this case you
cannot use Azure-Pipelines to test your data and you need to skip this part of the
testing battery.

The second category of tests concerns the code which does not normally fall under the
former constraint and can be given into the hands of private company.


Installation
------------

To enable testing, go to https://azure.microsoft.com/de-de/services/devops/pipelines/
and choose to log in with Github. Then, create a project. After that, choose to create
pipeline based on an existing ``.yaml`` in one of your repositories. Now, link to that
repository and navigate to the configuration file via branch and path. That's it!

To get an impression of a configuration file, take the following example of the
Azure-Pipelines configuration of this template.

.. literalinclude:: ../{{cookiecutter.project_slug}}/.azure-pipelines.yaml
    :language: yaml
