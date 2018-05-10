from click.testing import CliRunner
from context_src import *

version = {}
with open('./version.py') as fp:
    exec(fp.read(), version)


def test_version_cli_command_exit_code_should_equal_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])

    return Expect(result.exit_code).to_equal(0)

def test_version_cli_should_print_current_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])


    print(version['__version__'])
    return Expect(result.output).to_equal(f"Serpent {version['__version__']}\n")

def test_init_cli_command_exit_code_should_equal_zero():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ['--init'])

    return Expect(result.exit_code).to_equal(0)

def test_init_cli_command_should_create_a_test_folder():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        runner.invoke(cli, ['--init'])
        result = os.path.isdir(tempdir + '/tests')

    return Expect(result).to_equal(True)

def test_init_cli_command_should_create_a_test_folder_with_a_context_file():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        runner.invoke(cli, ['--init'])
        result = os.path.isfile(tempdir + '/tests/context.py')

    return Expect(result).to_equal(True)

def test_serpent_cli_command_should_run_all_tests():
    runner = CliRunner()
    with runner.isolated_filesystem():
        runner.invoke(cli, ['--example'])
        result = runner.invoke(cli)
        print(result.output)

    return Expect(result.output).to_include(
        'test_fizz',
        'test_buzz',
        'test_fizzbuzz',
        'test_number'
    )

def test_serpent_cli_command_should_run_even_if_no_tests_found():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli)

    return Expect(result.output).to_include('No tests have been found')
