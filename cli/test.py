import click
from runner import run

@click.group()
def test():
    pass

@test.command()
@click.argument('filename', required=False)
def test(filename):
    if filename:
        click.echo("running specfic test file")
        click.echo(filename)
        #run(filname)
    else:
        run()
