#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("src/documentation/authors.rst")

    if "{{ cookiecutter.create_history_file }}" != "y":
        remove_file("HISTORY.rst")
        remove_file("src/documentation/history.rst")

    if "{{ cookiecutter.add_pytest }}" != "y":
        # TODO
        remove_file("tests/__init__.py")

    if "{{ cookiecutter.add_pyup }}" != "y":
        remove_file(".pyup.yml")

    if "{{ cookiecutter.add_tox }}" != "y":
        remove_file("tox.ini")

    if "{{ cookiecutter.add_travis }}" != "y":
        remove_file(".travis.yml")

    if "{{ cookiecutter.add_downloader }}" != "y":
        remove_file("prepare_data_for_project.py")

    if "{{ cookiecutter.add_cleaner }}" != "y":
        remove_file("clean.py")

    if "{{ cookiecutter.add_debugger }}" != "y":
        remove_file("debug.ps1")

    if "{{ cookiecutter.add_formatter }}" != "y":
        remove_file("format_project.py")
        remove_file(".format_docs.sh")
        remove_file("pyproject.toml")
