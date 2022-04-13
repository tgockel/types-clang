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
    This project is still ``0.x``, so this section is more about the *plans* for how to version.

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

Development utilizes `Poetry <https://python-poetry.org/>`_ for dependency fetching and package publishing and
`tox <https://tox.wiki/en/latest/>`_ for testing.
The ``clang-stubs/cindex.py`` file is generated with the ``generate_cindex.py`` script, which reads the installed
``clang.cindex`` module and generates code with `Jinja <https://palletsprojects.com/p/jinja/>`_.

My personal workflow looks like this::

    $> poetry shell
    (env-py3.9) $> poetry install
    (env-py3.9) $> ./generate_cindex.py --output clang-stubs/cindex.py
    (env-py3.9) $> ^D
    $> tox
