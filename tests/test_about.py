import click

from click.testing import CliRunner
from context import *

def test_CLI_exit_code_should_be_zero():
    runner = CliRunner()
    result = runner.invoke(about)

    return Expect(result.exit_code).to_equal(0)

def test_CLI_output_from_cli_command_about():
    runner = CliRunner()
    result = runner.invoke(about)

    return Expect(result.output).to_equal('Made with \U0001F40D by Alexandra McCarroll, Tom Betts, Richard Hewitt, Hemesh Unka (February 2018 Cohort - Makers Academy)\n')
