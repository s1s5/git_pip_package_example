# coding: utf-8
from setuptools import setup, find_packages
from git_pip_package_example import __author__, __version__, __license__

setup(
    name='git_pip_package_example',
    version=__version__,
    description='pip package example',
    license=__license__,
    author=__author__,
    keywords='pip example',
    packages=find_packages(),
    install_requires=[],
)
