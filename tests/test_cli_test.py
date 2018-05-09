import click, os

from click.testing import CliRunner
from context import *

def test_cli_command_test_exit_code_should_be_zero():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(test)

    return Expect(result.exit_code).to_equal(0)

def test_cli_command_test_executes_all_tests():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        runner.invoke(example)

        result = runner.invoke(test)

    return Expect(result.output).to_include('No tests found.')

def test_cli_command_test_executes_a_certain_test():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        runner.invoke(example)

        result = runner.invoke(test, ['hello.py'])

    return Expect(result.output).to_include('hello.py')
