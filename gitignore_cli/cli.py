import base64
import click
import sys

from github import Github, GithubException


try:
    g = Github()
    repo = g.get_repo('github/gitignore')
except GithubException:
    click.echo('Github API rate limit exceeded for your IP.')
    sys.exit()

PATHS = [
    '/',
    '/Global/',
    '/community/',
]


def get_gitignores():
    files = []
    for path in PATHS:
        files += repo.get_contents(path)

    contents = [(c.path, c) for c in files if c.name.endswith('.gitignore')]
    return dict((name.replace('.gitignore', ''), content) for name, content in contents)


def save_gitignore(text):
    with open('.gitignore', 'a') as f:
        f.write('# added by gitignore-cli\n\n')
        f.write(text)


@click.group()
def cli():
    pass


@cli.command()
def list():
    """Return a list of the available .gitignores"""
    for name in get_gitignores().keys():
        click.echo(name)


@cli.command()
@click.argument('param')
def search(param):
    """Search a .gitignore"""
    for name in get_gitignores().keys():
        if param in name.lower():
            click.echo(name)


@cli.command(short_help="Downloads a .gitignore given its name (append if .gitignore already exist")
@click.argument('name')
def download(name):
    original_name = name
    name = name.lower()
    for gitignore, content in get_gitignores().items():
        if name == gitignore.lower():
            txt = base64.b64decode(content.content).decode('utf8')
            save_gitignore(txt)
            break
    else:
        click.echo('Unable to locate ' + original_name)
        sys.exit(-1)


if __name__ == '__main__':
    cli()
