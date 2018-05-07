import click

@click.group()
def example():
    pass

@example.command()
def example():
    click.echo("Initializing some examples")
