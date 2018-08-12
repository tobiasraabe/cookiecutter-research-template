pyup.io
=======

`pyup.io <https://pyup.io/>`_ is a service which helps you to keep your
dependencies up-to-date. When connected to your Github repository, a pyup-bot
will automatically create pull-requests in pre-defined interval to update
``requirements.txt`` or ``environment.yml`` to the latest package versions.


Installation
------------

Just go to https://pyup.io/ and choose login via Github in the upper right
corner of the website. You will be redirected to Github to allow the service to
read your repositories, etc..

After that, when logged in on pyup.io, choose add repository in the upper right
corner to add your repository. You are asked about how you would like to
schedule updates, but that does not matter as the service is already configured
by ``.pyup.yml`` in your project folder. If you want to change the settings,
have a look at https://pyup.io/docs/bot/config/ to see all possible options.
