import click
import os
import shutil

from runner import *

TEST_SRC_FILE = os.path.dirname(__file__) + '/../init_example/test_fizzbuzz.py'
TEST_DST_ROOT = './tests'

TEST_LOGIC_SRC_FILE = os.path.dirname(__file__) + '/../init_example/fizzbuzz.py'
TEST_LOGIC_DST_ROOT = '.'

TEST_CONTEXT_SRC_FILE = os.path.dirname(__file__) + '/../init_example/context.py'
CONTEXT_SRC_FILE = os.path.dirname(__file__) + '/../init/context.py'

SNAKE_EMOJI = '\U0001F40D'

@click.group(invoke_without_command=True)
@click.pass_context

### Click flags
@click.version_option(
    version=None,
    help='Display the current version.',
    message='Serpent %(version)s')

@click.option(
    '--init',
    help='Initialise your project with DrSerpent.',
    is_flag=True)

@click.option(
    '--about',
    help='Show list names of DrSerpent creators',
    is_flag=True
)

@click.option(
    '--example',
    help='Ininitalise your project with an example fizzbuzz project',
    is_flag=True
)
### Click argument
@click.argument('filepath', required=False)

def cli(ctx, filepath, init, about, example):

    # Flag --init command
    if ctx.invoked_subcommand is None and init:
        create_test_dir()
        create_context_file()

    # Flag --about command
    elif ctx.invoked_subcommand is None and about:
        print_about_message()

    # Flag --example command
    elif ctx.invoked_subcommand is None and example:
        click.echo("Initialising fizzbuzz example...")
        create_test_dir()
        create_fizzbuzz_file()
        create_fizzbuzz_test_file()
        create_fizzbuzz_context_file()

    # Flag serpent <filename> argument command
    elif ctx.invoked_subcommand is None and filepath:
        if filepath:
            run_specific_file(filepath)

    # serpent command
    elif ctx.invoked_subcommand is None:
        run_all('.', 'tests')

##  Run specific file function
def run_specific_file(filepath):
    click.echo("running specfic test file")
    run_module('.', filepath)

## Init functions
def create_test_dir():
    if not os.path.exists('tests'):
        os.makedirs('tests')
        click.echo('\n\tcreated\ttests/')
    else:
        click.echo('\n\texists\ttests/')

def create_context_file():
    if not os.path.isfile('tests/context.py'):
        shutil.copy(CONTEXT_SRC_FILE, TEST_DST_ROOT)
        click.echo('\tcreated\ttests/context.py')
    else:
        click.echo('\texists\ttests/context.py')

## about function
def print_about_message():
    print(f"Made with {SNAKE_EMOJI} (Python) by Alexandra McCarroll, Tom Betts, Richard Hewitt, Hemesh Unka (February 2018 Cohort - Makers Academy)")

## fizzbuzz test functions
def create_fizzbuzz_test_file():
    if not os.path.isfile('tests/test_fizzbuzz.py'):
        shutil.copy(TEST_SRC_FILE, TEST_DST_ROOT)
        click.echo('\tcreated\ttests/test_fizzbuzz.py')
    else:
        click.echo('\texists\ttests/test_fizzbuzz.py')

def create_fizzbuzz_context_file():
    if not os.path.isfile('tests/context.py'):
        shutil.copy(TEST_CONTEXT_SRC_FILE, TEST_DST_ROOT)
        click.echo('\tcreated\ttests/context.py')
    else:
        click.echo('\texists\ttests/context.py')

def create_fizzbuzz_file():
    if not os.path.isfile('./fizzbuzz.py'):
        shutil.copy(TEST_LOGIC_SRC_FILE, TEST_LOGIC_DST_ROOT)
        click.echo('\tcreated\tfizzbuzz.py')
    else:
        click.echo('\texists\tfizzbuzz.py')
