#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='gitignore-cli',
    version='1.0.3',
    url='https://github.com/aron-bordin/gitignore-cli',
    description='gitignore cli downloader',
    long_description=long_description,
    author='Aron Bordin',
    author_email='aron.bordin@gmail.com',
    packages=find_packages(exclude=('tests', 'tests.*')),
    license='GPL',
    install_requires=['PyGithub', 'click'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Utilities'],
    keywords='git gitignore generate download',
    entry_points={
        'console_scripts': ['gitignore-cli=gitignore_cli.cli:cli']
    }
)
