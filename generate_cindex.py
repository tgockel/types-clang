#!/usr/bin/env python3
"""This script generates ``cindex.pyi`` from clang.cindex."""

import jinja2
import sys
import typing
from clang import cindex

def filter_startswith(value: typing.Sequence[str], search: str) -> typing.Sequence[str]:
    return (x for x in value if x.startswith(search))


def filter_not_none(value: typing.Sequence[typing.Any]) -> typing.Sequence[typing.Any]:
    return (x for x in value if x is not None)


def main() -> None:
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    # Expose all builtins to the Jinja environment
    env.globals.update({name: getattr(__builtins__, name) for name in dir(__builtins__)})
    env.filters['startswith'] = filter_startswith
    env.filters['not_none'] = filter_not_none
    template = env.get_template('cindex.pyi.jinja2')
    print(template.render(cindex=cindex))

if __name__ == '__main__':
    sys.exit(main())
