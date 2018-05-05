import click
import os

@click.group()
def init():
    pass

@init.command()
def init():
    if not os.path.exists('tests'):
        os.makedirs('tests')
        click.echo('    created  test/')
    else:
        click.echo('    exists   test/')
