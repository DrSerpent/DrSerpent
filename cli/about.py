import click
import emoji

@click.group()
def about():
    pass

@about.command()
def about():
    click.echo(emoji.emojize('Made with :snake: by Alexandra McCarroll, Tom , Ricky, Hemesh Unka (February 2018 Cohort - Makers Academy)'))
