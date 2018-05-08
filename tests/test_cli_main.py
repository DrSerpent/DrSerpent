import click

from click.testing import CliRunner
from context import *

def test_version_CLI_command_exit_code_should_equal_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])

    return Expect(result.exit_code).to_equal(0)

def test_version_CLI_should_print_current_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])

    return Expect(result.output).to_equal('Serpent 1.0\n')
