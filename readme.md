# python package example
## create package
```sh
$ mkdir git_pip_package_example
```
## add informations
```py
__author__ = 'Shogo Sawai'
__version__ = '0.0.1'
__license__ = 'MIT'
```

## add setup.py
```py
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
```

## git push

## install from others
```sh
$ pip install git+https://github.com/s1s5/git_pip_package_example.git
```
