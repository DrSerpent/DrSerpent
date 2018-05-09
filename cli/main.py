import click
import os
import shutil

from runner import *
# from .about import about
# from .example import example

CONTEXT_SRC_FILE = os.path.dirname(__file__) + '/../init/context.py'
TEST_DST_ROOT = './tests'

@click.group(invoke_without_command=True)
@click.pass_context

@click.version_option(
    version=None,
    help='Display the current version.',
    message='Serpent %(version)s')

@click.option(
    '--init',
    help='Initialize your project with Serpent.',
    is_flag=True)

@click.option(
    '--about',

)

@click.argument('filepath', required=False)

def cli(ctx, filepath, init):

    # cli.add_command(about)
    # cli.add_command(example)

    # --init
    if ctx.invoked_subcommand is None and init:
        create_test_dir()
        create_context_file()


    elif ctx.invoked_subcommand is None and filepath:
        if filepath:
            run_specific_file(filepath)

    # --run all tests
    elif ctx.invoked_subcommand is None:
        run_all()

    # get subcommands
    else:
        pass


def create_test_dir():
    if not os.path.exists('tests'):
        os.makedirs('tests')
        click.echo('\t\tcreated\ttest/')
    else:
        click.echo('\t\texists\ttest/')

def create_context_file():
    if not os.path.isfile('tests/context.py'):
        shutil.copy(CONTEXT_SRC_FILE, TEST_DST_ROOT)

def run_specific_file(filepath):
    click.echo("running specfic test file")
    run_test(filepath)
