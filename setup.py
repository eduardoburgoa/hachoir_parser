#!/usr/bin/env python

# This will try to import setuptools. If not here, it will reach for the embedded
# ez_setup (or the ez_setup package). If none, it fails with a message
try:
    from setuptools import setup
except ImportError:
    try:
        import ez_setup
        ez_setup.use_setuptools()
    except ImportError:
        raise ImportError("hachoir-parser is a package of most common file format "
                          "parsers written for Hachoir framework.")

from setuptools import setup, find_packages

setup(name='hachoir_parser',
      version='1.3.4',
      author='Hachoir team',
      description='Package of Hachoir parsers used to open binary files',
      long_description=open('README.rst').read(),
      url='https://github.com/eduardoburgoa/hachoir_parser',
      license='GNU GPL v2',
      keywords="file binary metadata",
      packages=find_packages(exclude='docs'),
      install_requires=[])
