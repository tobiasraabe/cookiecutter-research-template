import os
import subprocess

import click


def cli():
    """Starts formatting with black, blacken-docs and isort.

    The order is currently important as black does not insert commas to single
    line from imports. Should be fixed in the next version and then we can also
    include flake8-isort to tox.

    """
    click.echo("Start formatting python files with black.")
    os.system("black .")
    click.echo("Start formatting docs with blacken-docs.")
    os.system(".format_docs.sh")
    click.echo("Start formatting python files with isort.")
    os.system("isort . --recursive")
    click.echo("End formatting files.")


if __name__ == "__main__":
    cli()
