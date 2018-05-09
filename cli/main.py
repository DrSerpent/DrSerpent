import click
import os
import shutil

from .about import about
from .example import example
from .test import test
from runner import *

CONTEXT_SRC_FILE = os.path.dirname(__file__) + '/../init/context.py'
TEST_DST_ROOT = './tests'

@click.group(
    invoke_without_command=True,
    no_args_is_help=False)
@click.pass_context

@click.version_option(
    version=None,
    help='Display the current version.',
    message='Serpent %(version)s')

@click.option(
    '--init',
    help='Initialize your project with Serpent.',
    is_flag=True)

def cli(ctx, init):
    # --init
    if ctx.invoked_subcommand is None and init:
        init_folder_creation()
    # --run tests
    elif ctx.invoked_subcommand is None:
        run_all()

    # get subcommands
    else:
        pass

cli.add_command(about)
cli.add_command(test)
cli.add_command(example)

# --init cli test dir creation
def init_folder_creation():
    if not os.path.exists('tests'):
        os.makedirs('tests')
        shutil.copy(CONTEXT_SRC_FILE, TEST_DST_ROOT)
        click.echo('    created  test/')
    else:
        click.echo('    exists   test/')
