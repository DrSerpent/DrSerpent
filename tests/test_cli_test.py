from click.testing import CliRunner
from context import *

def test_CLI_command_should_run_all_tests():
    runner = CliRunner()
    with runner.isolated_filesystem() as tempdir:
        result = runner.invoke(test)

    return Expect(result.output).to_equal('No tests found.')
