###########
types-clang
###########
==========================================
Type Information for Clang Python Bindings
==========================================

Have you used the `Clang Python Bindings <https://pypi.org/project/clang/>`_, but wanted type hints in your IDE?
Have you ever wanted to use `mypy <http://mypy-lang.org/>`_ tools on a project that uses Clang but gotten errors due to
lack of type annotations?
This package is a `PEP 561 <https://www.python.org/dev/peps/pep-0561>`_ stub package which provides type information for
Clang.

In other words, transform your IDE from:

.. image:: https://raw.githubusercontent.com/tgockel/types-clang/trunk/doc/before.png

to:

.. image:: https://raw.githubusercontent.com/tgockel/types-clang/trunk/doc/after.png

To utilize this, add it globally with::

    pip3 install types-clang

Or add ``types-clang`` to ``dev-requirements.txt`` or ``pyproject.toml`` or whatever you use for dependency management.

Versioning
==========

.. note::
    This project is still ``0.x``, so add a ``0.`` in front of the descriptions here.
    In other words, for ``clang`` ``12.0.1``, use ``types-clang`` ``0.12.2``.

The published ``types-clang`` packages correspond with the type information of the ``{major}.{minor}`` of the ``clang``
package.
The patch version of ``types-clang`` does not correspond with any patch version of ``clang``, as they use semantic
versioning correctly and will not add functionality in a patch release.
So, if you install ``clang==13.0.1``, then ``types-clang>=13.0, <13.1`` will have the appropriate stubs.

Best practice is to write the version specification for ``types-clang`` to be the same as the ``clang`` package, but
without the patch.
For `Poetry <https://python-poetry.org/>`_::

    [tool.poetry.dependencies]
    clang = "14.0"

    [tool.poetry.dev-dependencies]
    types-clang = "14.0"

Developing
==========

Development of this project is slightly indirect.
The root project is named ``gen-gen-types-clang``, which uses file copying and a bit of
`Jinja <https://palletsprojects.com/p/jinja/>`_ to create a couple of project files based on a version of Clang.
By default, these live in ``projects/${CLANG_VERSION}``.
These generated projects are all named ``gen-types-clang``, which contain a script named ``generate-cindex`` that will
generate ``types-clang/clang-stubs/cindex.pyi`` based on the installed ``clang.cindex`` module.
Once run, the ``types-clang`` project can be tested with ``tox``.

You can do all of this by running the ``./build-all`` script at the root of this repository.

This all seems a bit convoluted
-------------------------------

You are correct.

I want to be able to generate Clang bindings for versions of Clang from the past and be able to fix mistakes in the
generated stubs.
I was not able to find a Python project system capable of doing this out-of-the-box.

Another reason this is done is to support older versions of Python.
Jinja requires Python 3.7 and above, but I needed this project to work with Python 3.6 (even though it is past the end
of security fixes).
Since Jinja is only used at generation time, there is no need to restrict the published package to 3.7+.

I thought this was the best approach at the time.
If there is an easier way to do this, let me know.
