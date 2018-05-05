import click
from .about import about
from .init import init
from .test import test
from testrunner import run

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        run()
    else:
        pass

cli.add_command(about)
cli.add_command(init)
cli.add_command(test)
