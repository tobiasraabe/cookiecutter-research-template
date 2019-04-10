Tips and Tricks for Waf
=======================

Here is a list of tips and tricks you might want to use for your research project. Some
of the things are only suggestions to solve some problems, but are not further
explained.

Compiling the reports with LaTeX
--------------------------------

1. Compiling pollutes the command line interface. To shut it off, change ``prompt`` to 0
   in ``src/paper/wscript``. Unfortunately, if an error happens, you have to switch back
   to find the source.

2. (Windows) Sometimes changes in the dependencies of the report are not recognized and
   the document is not compiled. Maybe this is related to `a similar issue with
   LatexTools <https://github.com/SublimeText/
   LaTeXTools/issues/884#issuecomment-258092032>`_. In this case, type ``rm
   bld/src/paper`` to delete all built artifacts.

Copying files
-------------

Do not use the ``rule`` argument with ``cp`` or ``copy`` as those operations tend out to
be extremely slow. Use one of the following instead.

- To copy a file from the source to the build directory, use

  .. code-block:: python

      ctx(
          features="subst",
          source=ctx.path_to(ctx, "IN_DATA", "file.pkl"),
          target=ctx.path_to(ctx, "OUT_DATA", "file.pkl"),
          is_copy=True,
      )

- To copy a directory use ``buildcopy`` (`Link <https://stackoverflow.com/
  questions/45652196/copying-multiple-files-in-waf-using-only-a-single- target>`_)


Running interactive commands
----------------------------

Apparently, this should be possible with `this <https://stackoverflow.com/
questions/44141704/can-i-run-an-interactive-command>`_. Should test it with the debug
script.


Type annotations with Monkeytype
--------------------------------

`MonkeyType <https://github.com/Instagram/MonkeyType>`_ allows you to collect
information on variable types at runtime and store the results in a SQLite database.
After that, you are able apply the type annotations to your code.

For that, we need to replace plain Python as the executor of the scripts with MonkeyType
in ``run_py_script.py``. Of course, it is possible to create another runner named
``run_monkeytype_script.py``, but it would be more tiresome. Instead locate the variable
``run_str`` in ``class run_py_script()`` and replace ``${PYCMD}`` with ``monkeytype
run``.

Running Waf will execute all scripts with MonkeyType and store the results in
``bld/monkeytype.sqlite3``. Use ``monkeytype apply some.module`` to apply the type
annotations to the module.

Maybe the procedure messes with your prepended arguments, but I have not used them so
far. Feedback welcome!
