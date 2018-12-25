import os

from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_file(*filepath):
    try:
        Path(PROJECT_DIRECTORY, *filepath).unlink()
    except FileNotFoundError:
        pass


if __name__ == "__main__":  # noqa: C901

    if "{{ cookiecutter.create_author_file }}" == "no":
        remove_file("AUTHORS.rst")
        remove_file("src", "documentation", "authors.rst")

    if "{{ cookiecutter.create_history_file }}" == "no":
        remove_file("HISTORY.rst")
        remove_file("src", "documentation", "history.rst")

    if "{{ cookiecutter.add_pyup }}" == "no":
        remove_file(".pyup.yml")

    if "{{ cookiecutter.add_tox }}" == "no":
        remove_file(".travis.yml")
        remove_file("tox.ini")

    if "{{ cookiecutter.add_travis }}" == "no":
        remove_file(".travis.yml")

    if "{{ cookiecutter.add_downloader }}" == "no":
        remove_file("prepare_data_for_project.py")

    if "{{ cookiecutter.add_cleaner }}" == "no":
        remove_file("clean.py")

    if "{{ cookiecutter.add_debugger }}" == "no":
        remove_file("debug.ps1")

    if "{{ cookiecutter.add_readthedocs }}" == "no":
        remove_file("readthedocs.yml")

    if "{{ cookiecutter.create_conda_environment_at_finish }}" == "yes":
        os.system(
            "conda env create "
            "--file environment.yml "
            "--name {{ cookiecutter.conda_environment_name }}"
        )
