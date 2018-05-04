import click
from testrunner import run

@click.command()
def cli():
    click.echo(run())
