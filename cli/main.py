import click
import os
import shutil

from runner import *

CONTEXT_SRC_FILE = os.path.dirname(__file__) + '/../init/context.py'
TEST_DST_ROOT = './tests'
SNAKE_EMOJI = '\U0001F40D'

@click.group(invoke_without_command=True)
@click.pass_context

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

@click.argument('filepath', required=False)

def cli(ctx, filepath, init, about, example):

    # --init
    if ctx.invoked_subcommand is None and init:
        create_test_dir()
        create_context_file()

    elif ctx.invoked_subcommand is None and about:
        print_about()

    elif ctx.invoked_subcommand is None and example:
        click.echo('hello')

    elif ctx.invoked_subcommand is None and filepath:
        if filepath:
            run_specific_file(filepath)

    # --run all tests
    elif ctx.invoked_subcommand is None:
        run_all()

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

def print_about():
    print(f"Made with {SNAKE_EMOJI} by Alexandra McCarroll, Tom Betts, Richard Hewitt, Hemesh Unka (February 2018 Cohort - Makers Academy)")
