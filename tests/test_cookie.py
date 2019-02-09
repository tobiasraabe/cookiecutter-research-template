import os
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


def test_remove_readthedocs(cookies):
    result = cookies.bake(extra_context={"add_readthedocs": "no"})

    readthedocs = result.project.join("readthedocs.yml")
    readme = result.project.join("README.rst").read()

    assert result.exit_code == 0
    assert result.exception is None

    assert readthedocs.check(exists=0)
    assert "readthedocs" not in readme


def test_remove_pyup(cookies):
    result = cookies.bake(extra_context={"add_pyup": "no"})

    pyup = result.project.join(".pyup.yml")
    readme = result.project.join("README.rst").read()

    assert result.exit_code == 0
    assert result.exception is None

    assert pyup.check(exists=0)
    assert "pyup" not in readme


def test_remove_travis(cookies):
    result = cookies.bake(extra_context={"add_travis": "no"})

    travis = result.project.join("travis.yml")
    readme = result.project.join("README.rst").read()

    assert result.exit_code == 0
    assert result.exception is None

    assert travis.check(exists=0)
    assert "travis" not in readme


@pytest.mark.skipif(
    "CI" not in os.environ,
    reason="The environment is only created on Travis-CI or Appveyor.",
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
