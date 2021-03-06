#!/usr/bin/env python
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='concoctr',
      version=version,
      description="Package for managing the CONCOCT package",
      long_description="""\
To be done""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Python Scilifelab Metagenomics Binning Clustering Contig',
      author='Johannes Alneberg',
      author_email='johannes.alneberg@scilifelab.se',
      maintainer='Johannes Alneberg',
      maintainer_email='johannes.alneberg@scilifelab.se',
      url='www.github.com/alneberg/concoctr',
      license='FreeBSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=['argparse==1.2.1',
                        'nose==1.3.0'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
