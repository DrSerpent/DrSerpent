import click
import os
import shutil

from .about import about
from .example import example
from .test import test
from runner import run

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
        create_test_dir()
        create_context_file()

    # --run tests
    elif ctx.invoked_subcommand is None:
        run()

    # get subcommands
    else:
        pass

cli.add_command(about)
cli.add_command(test)
cli.add_command(example)

def create_test_dir():
    if not os.path.exists('tests'):
        os.makedirs('tests')
        click.echo('\t\tcreated\ttest/')
    else:
        click.echo('\t\texists\ttest/')

def create_context_file():
    if not os.path.isfile('tests/context.py'):
        shutil.copy(CONTEXT_SRC_FILE, TEST_DST_ROOT)
