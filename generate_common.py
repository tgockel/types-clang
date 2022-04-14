"""Common features for code generators."""

import jinja2
import typing

def filter_startswith(value: typing.Sequence[str], search: str) -> typing.Sequence[str]:
    return (x for x in value if x.startswith(search))


def filter_not_none(value: typing.Sequence[typing.Any]) -> typing.Sequence[typing.Any]:
    return (x for x in value if x is not None)


def create_jinja_env(searchpath: str = 'templates') -> jinja2.Environment:
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath))
    # Expose reasonable builtins to the Jinja environment
    env.globals.update(
        dir=dir,
        map=map,
        repr=repr,
        str=str,
    )

    env.filters['startswith'] = filter_startswith
    env.filters['not_none'] = filter_not_none

    return env
