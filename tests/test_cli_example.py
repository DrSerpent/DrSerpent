import click, os

from click.testing import CliRunner
from context_src import *

def test_example_CLI_command_exit_code_should_be_zero():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        result = runner.invoke(example)

    return Expect(result.exit_code).to_equal(0)

def test_example_CLI_command_should_create_a_new_directory_called_test():
    runner = CliRunner()

    with runner.isolated_filesystem() as tempdir:
        runner.invoke(example)
        result = os.path.isdir(tempdir + '/tests')

    return Expect(result).to_equal(True)

def test_example_CLI_command_should_warn_if_test_dir_exists():
    runner = CliRunner()

    with runner.isolated_filesystem() as tempdir:
        runner.invoke(example)
        result = runner.invoke(example)

    return Expect(result.output).to_equal('Initialising fizzbuzz example\n\t\texists\ttest/\n')

def test_example_CLI_command_should_create_fizzbuzz_example_file():
    runner = CliRunner()

    with runner.isolated_filesystem() as tempdir:
        runner.invoke(example)
        result = os.path.isfile(tempdir + '/fizzbuzz.py')

    return Expect(result).to_equal(True)

def test_example_CLI_command_should_create_fizzbuzz_example_test_file():
    runner = CliRunner()

    with runner.isolated_filesystem() as tempdir:
        runner.invoke(example)
        result = os.path.isfile(tempdir + '/tests/test_fizzbuzz.py')

    return Expect(result).to_equal(True)

def test_init_CLI_command_should_create_a_fizzbuzz_context_file_within_test_folder():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        runner.invoke(example)
        result = os.path.isfile(tempdir + '/tests/context.py')

    return Expect(result).to_equal(True)
