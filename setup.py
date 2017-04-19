#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='gitignore-cli',
    version='0.1',
    url='https://github.com/aron-bordin/gitignore-cli',
    description='gitignore cli downloader',
    author='Aron Bordin',
    packages=find_packages(exclude=('tests', 'tests.*')),

    entry_points={
        'console_scripts': ['gitignore-cli=gitignore_cli.cli:cli']
    }
)
