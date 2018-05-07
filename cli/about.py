import click

SNAKE_EMOJI = '\U0001F40D'

@click.group()
def about():
    pass

@about.command()
def about():
    print(f"Made with {SNAKE_EMOJI} by Alexandra McCarroll, Tom Betts, Richard Hewitt, Hemesh Unka (February 2018 Cohort - Makers Academy)")
