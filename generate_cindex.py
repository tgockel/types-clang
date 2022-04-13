#!/usr/bin/env python3
"""This script generates ``cindex.pyi`` from clang.cindex."""

import argparse
import jinja2
import sys
import typing
from clang import cindex

def filter_startswith(value: typing.Sequence[str], search: str) -> typing.Sequence[str]:
    return (x for x in value if x.startswith(search))


def filter_not_none(value: typing.Sequence[typing.Any]) -> typing.Sequence[typing.Any]:
    return (x for x in value if x is not None)


class Context(typing.NamedTuple):
    output: typing.TextIO

    @classmethod
    def from_args(cls) -> 'Context':
        p = argparse.ArgumentParser()
        p.add_argument('--output', '-o', type=str, default='-')

        args = p.parse_args()

        return cls(output=sys.stdout if args.output == '-' else open(args.output, 'w+'))

    def __enter__(self) -> 'Context':
        return self

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        if self.output != sys.stdout:
            self.output.close()


def main() -> None:
    with Context.from_args() as context:
        env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
        # Expose all builtins to the Jinja environment
        env.globals.update({name: getattr(__builtins__, name) for name in dir(__builtins__)})
        env.filters['startswith'] = filter_startswith
        env.filters['not_none'] = filter_not_none

        template = env.get_template('cindex.pyi.jinja2')

        context.output.write(template.render(cindex=cindex))
        context.output.write('\n')

if __name__ == '__main__':
    sys.exit(main())
