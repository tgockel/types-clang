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
