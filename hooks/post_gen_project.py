#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":  # noqa: C901

    if "{{ cookiecutter.create_author_file }}" == "no":
        remove_file("AUTHORS.rst")
        remove_file("src/documentation/authors.rst")

    if "{{ cookiecutter.create_history_file }}" == "no":
        remove_file("HISTORY.rst")
        remove_file("src/documentation/history.rst")

    if "{{ cookiecutter.add_pytest }}" == "no":
        # TODO
        remove_file("tests/__init__.py")

    if "{{ cookiecutter.add_pyup }}" == "no":
        remove_file(".pyup.yml")

    if "{{ cookiecutter.add_tox }}" == "no":
        remove_file("tox.ini")

    if "{{ cookiecutter.add_travis }}" == "no":
        remove_file(".travis.yml")

    if "{{ cookiecutter.add_downloader }}" == "no":
        remove_file("prepare_data_for_project.py")

    if "{{ cookiecutter.add_cleaner }}" == "no":
        remove_file("clean.py")

    if "{{ cookiecutter.add_debugger }}" == "no":
        remove_file("debug.ps1")

    if "{{ cookiecutter.add_formatter }}" == "no":
        remove_file("format_python_files.py")
        remove_file("pyproject.toml")

    if "{{ cookiecutter.create_conda_environment_at_finish }}" == "yes":
        os.system(
            "conda env create "
            "-f {{ cookiecutter.project_slug }}/environment.yml "
            "-n {{ cookiecutter.conda_environment_name }}"
        )
