import click, os, shutil


TEST_SRC_FILE = os.path.dirname(__file__) + '/../tests/example_projects/fizzbuzz/example_tests/test_logic.py'
TEST_DST_ROOT = './tests'
SRC_FILE = os.path.dirname(__file__) + '/../tests/example_projects/fizzbuzz/logic.py'
DST_ROOT = '.'

@click.group()
def example():
    pass

@example.command()
def example():
    click.echo("Initialising fizzbuzz example")
    create_test_dir()
    create_fizzbuzz_file()
    create_fizzbuzz_test_file()

def create_test_dir():
    if not os.path.exists('tests'):
        os.makedirs('tests')
        click.echo('\t\tcreated\ttest/')
    else:
        click.echo('\t\texists\ttest/')

def create_fizzbuzz_test_file():
    if not os.path.isfile('tests/test_logic.py'):
        shutil.copy(TEST_SRC_FILE, TEST_DST_ROOT)

def create_fizzbuzz_file():
    if not os.path.isfile('logic.py'):
        shutil.copy(SRC_FILE, DST_ROOT)
