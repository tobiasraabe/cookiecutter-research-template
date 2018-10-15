import os


def test_bake_project(cookies):
    python_version = os.environ["TRAVIS_PYTHON_VERSION"]
    print(python_version)

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
    result = cookies.bake(extra_context={"add_downloader": "n"})

    downloader = result.project.join("prepare_data_for_project.py")

    assert result.exit_code == 0
    assert downloader.check(exists=0)


def test_remove_formatter(cookies):
    result = cookies.bake(extra_context={"add_formatter": "n"})

    formatter = result.project.join("format_python_files.py")
    pyproject = result.project.join("pyproject.toml")
    tox = result.project.join("tox.ini").read()

    assert result.exit_code == 0
    assert formatter.check(exists=0)
    assert pyproject.check(exists=0)
    assert "[isort]" not in tox
