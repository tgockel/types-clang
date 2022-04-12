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

.. image:: https://raw.githubusercontent.com/tgockel/clang-stubs/trunk/doc/before.png

to:

.. image:: https://raw.githubusercontent.com/tgockel/clang-stubs/trunk/doc/after.png

To utilize this, add it globally with::

    pip3 install types-clang

Or add ``types-clang`` to ``dev-requirements.txt`` or ``pyproject.toml`` or whatever you use for dependency management.
