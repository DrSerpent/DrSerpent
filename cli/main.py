import click
import os

from .about import about
from .test import test
from runner import run

@click.group(invoke_without_command=True, no_args_is_help=False)
@click.pass_context
@click.version_option(version=None, help='Display the current version.', message='Serpent %(version)s')
@click.option('--init', help='Initialize your project with Serpent.', is_flag=True)
def cli(ctx, init):
    # --init
    if ctx.invoked_subcommand is None and init:
        if not os.path.exists('tests'):
            os.makedirs('tests')
            click.echo('    created  test/')
        else:
            click.echo('    exists   test/')

    # --run tests
    elif ctx.invoked_subcommand is None:
        run()

    # get subcommands
    else:
        pass

cli.add_command(about)
cli.add_command(test)
