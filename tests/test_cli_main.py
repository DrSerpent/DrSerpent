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

def test_init_CLI_command_exit_code_should_equal_zero():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        result = runner.invoke(cli, ['--init'])

    return Expect(result.exit_code).to_equal(0)

def test_init_CLI_command_should_create_a_test_folder():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        runner.invoke(cli, ['--init'])
        result = os.path.isdir(tempdir + '/tests')

    return Expect(result).to_equal(True)

# def test_init_CLI_command_should_create_a_test_folder_with_a_context_file():
#     runner = CliRunner()
#     with runner.isolated_filesystem() as tempdir:
#         runner.invoke(cli, ['--init'])
#         result = os.path.isdir(tempdir + '/tests.context.py')
#
#     return Expect(result).to_equal(True)
