import sys

import pytest


def test_bake_project(cookies):
    major, minor = sys.version_info[:2]
    python_version = "{}.{}".format(major, minor)

    result = cookies.bake(
        extra_context={
            "project_slug": "helloworld",
            "python_version": python_version,
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "helloworld"
    assert result.project.isdir()


def test_remove_downloader(cookies):
    result = cookies.bake(extra_context={"add_downloader": "no"})

    downloader = result.project.join("prepare_data_for_project.py")

    assert result.exit_code == 0
    assert result.exception is None
    assert downloader.check(exists=0)


def test_remove_formatter(cookies):
    result = cookies.bake(extra_context={"add_formatter": "no"})

    formatter = result.project.join("format_python_files.py")
    pyproject = result.project.join("pyproject.toml")
    tox = result.project.join("tox.ini").read()

    assert result.exit_code == 0
    assert formatter.check(exists=0)
    assert pyproject.check(exists=0)
    assert "[isort]" not in tox


@pytest.mark.skipif(
    sys.version_info[:2] != (3, 7),
    reason="Miniconda is only installed for Python 3.7",
)
def test_check_conda_environment_creation(cookies):
    result = cookies.bake(
        extra_context={
            "create_conda_environment_at_finish": "yes",
            "conda_environment_name": "test",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None

    # TODO: Test that the environment can be activated. Currently, the
    # following test fails as the extracted prefix is "pytest". Maybe the
    # activation is not working.

    # if platform.system() == "Windows":
    #   os.system("activate test")
    # else:
    #   os.system("source activate test")

    # assert sys.prefix.split(os.path.sep)[-1] == "test"
