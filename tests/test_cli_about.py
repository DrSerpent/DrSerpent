from click.testing import CliRunner
from context_src import *

def test_flag_about_CLI_command_exit_code_should_be_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ['--about'])

    return Expect(result.exit_code).to_equal(0)

def test_flag_about_CLI_command_output_from_cli_command_about():
    runner = CliRunner()
    result = runner.invoke(cli, ['--about'])

    return Expect(result.output).to_equal('Made with \U0001F40D by Alexandra McCarroll, Tom Betts, Richard Hewitt, Hemesh Unka (February 2018 Cohort - Makers Academy)\n')
