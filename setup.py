from setuptools import setup, find_packages

setup(
    name='drserpent',
    version='2.1',
    packages=[],
    include_package_data=True,
    install_requires=[
        'emoji',
        'Click',
    ],
    description='Python Testing Framework',
    url='https://github.com/DrSerpent/DrSerpent-Core',
    author='Tom Betts',
    author_email='tom.betts@live.co.uk',
    license='MIT',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'serpent=cli.main:cli'
        ],
    }
    )
