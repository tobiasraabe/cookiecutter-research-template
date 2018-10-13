import os

from pathlib import Path

import click


def cli():
    """Starts reformatting with isort and black.

    The order is currently important as black does not insert commas to single
    line from imports. Should be fixed in the next version and then we can also
    include flake8-isort to tox.

    """
    click.echo("Start reformatting files with isort.")

    files = (
        list(Path(".").glob("**/wscript"))
        + list(Path(".").glob("*.py"))
        + list(Path(".").glob("src/**/*.py"))
    )
    files = " ".join([str(i) for i in files])

    os.system(f"isort {files} -sp tox.ini")

    click.echo("Start reformatting files with black.")
    os.system("black .")

    click.echo("End reformatting files.")


if __name__ == "__main__":
    cli()
