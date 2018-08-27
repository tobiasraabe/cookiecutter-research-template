Code Conventions
================

Code conventions are rules to follow during coding to prevent mistakes and
ensure readability. The last point is crucial and cannot be stressed enough.

..

    Code is far more often read than written.

Therefore, one has a huge incentive to write as readable as possible to reduce
one's own mental effort, to reduce it for others who then are more willing to
contribute and use readability as a mean to replicability.

There are two different kind of programs included in the template to achieve
this goal.


Formatters
----------

Formatters are tools which take the code and transform it to something else
without influencing the way the code works.

The project contains two different formatters.


`Black <https://github.com/ambv/black>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Black is relatively new in the Python ecosystem and calls itself the
uncompromising Python code formatter. The slogan is true. There are almost no
options to choose a different style except line length and whether you want to
use single quotes, ``'``, or double quotes, ``"``, for strings. But, it
definitely produces more readable code and helps you to learn what good code
looks like.

The default line length is set to 79. Other common values are 80, 88, 120. 80
characters can be displayed on most devices and most of the time it is possible
to have to files side-by-side to cross-read. 79 is chosen because if the last
character is close to the border of the screen we might want to have a little
offset. 88 seems to produce much shorter files by only increasing the width by
10%.

There is a heated debate about single versus double quotes. Single quotes seem
to produce less visual noise for readers. Double quotes anticipate apostrophes
in English text. Some others use single quotes for data and double quotes for
real language. Black settles on double quotes only and despite that I am more
inclined to use single quotes myself, I think standardization is a good thing.
Therefore, the formatter will recode all strings to double quotes. If you want
to keep it your way, insert ``skip-string-normalization = true`` in the
``pyproject.toml``


`isort <https://github.com/timothycrosley/isort>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

isort sorts your imports alphabetically and into sections, so that you do not
have to do it.


Linters
-------

To lint a file means to check the file for errors. The errors can be stylistic
errors, warning if you do not follow code conventions, etc.. One example is
that unused variables like loop counters are referenced with an ``_`` like
this:

.. code-block:: python

    for _ in range(3):
        print("Hey")


flake8
~~~~~~

flake8 is common tool to lint Python files. It does not only recognize
stylistic issues which should be fixed with Black anyway, but it also makes
comments on the naming of variables, suggestions for rewriting code segments
and more.


doc8
~~~~

doc8 helps you to avoid errors in restructured-text files which are hard to
debug using the sphinx error log.


restructuredtext_lint
~~~~~~~~~~~~~~~~~~~~~

This tool validates your ``README.rst`` in case you want to publish your
project as a package on PyPI.
