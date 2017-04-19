# gitignore-cli
A simple CLI (Command Line Interface) to download .gitignore from http://github.com/github/gitignore/

## Install

Install it using:
    pip install gitignore-cli


## Usage

Usage: gitignore-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show the help message and exit.

Commands:
  download  Downloads a .gitignore given its name (append if a .gitignore already exist)
  list      Return a list of the available .gitignores
  search    Search a .gitignore
  
## Examples

* gitignore-cli download python
* gitignore-cli search py
