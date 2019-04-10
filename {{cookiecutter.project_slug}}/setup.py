from setuptools import setup


setup(
    name="{{ cookiecutter.project_name }}",
    author="{{ cookiecutter.author }}",
    packages=["bld", "src"],
)
