import click
import emoji

@click.group()
def about():
    pass

@about.command()
def about():
    click.echo(emoji.emojize('Made with :snake: by Alex, Tom, Ricky, Hemesh (Feb 2018 Cohort - Makers Academy)'))
