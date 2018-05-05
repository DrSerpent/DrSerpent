import click
import emoji

@click.group()
def about():
    pass

@about.command()
def about():
    click.echo(emoji.emojize('Made with :snake: by Alex, Tom, Ricky, Hemesh (Feb 2018 Cohort - Makers Academy)'))

#
# # @click.group(invoke_without_command=True)
# # @click.pass_context
# # def cli(ctx):
# #     if ctfilx.invoked_subcommand is None:
# #         click.echo('I was invoked without subcommand')
# #     else:
# #         click.echo('I am about to invoke %s' % ctx.invoked_subcommand)
# #
# # @cli.command()
# # @click.argument('filename')
# # def loadfile(filename):
# #     click.echo(filename)
#
#
# # ## WORKS
# # @click.group()
# # def cli():
# #     pass
# #
# # @click.command()
# # def init():
# #     if not os.path.exists('tests'):
# #         os.makedirs('tests')
# #         os.makedirs('tests/tests')
# #         click.echo('    create  test/')
# #         click.echo('    create  test/test')
# #     else:
# #         click.echo('    exists   test/')
# #         click.echo('    exists   test/test')
# #
# # @click.command()
# # def about():
# #     click.echo(emoji.emojize('Made with :snake: by Alex, Tom, Ricky, Hemesh (Feb 2018 Cohort - Makers Academy)'))
# #
# # cli.add_command(init)
# # cli.add_command(about)
