from setuptools import setup, find_packages

setup(
    name='drserpent',
    version='2.4',
    packages=['cli','init','init_example'],
    py_modules=['expect','runner','collector','executor'],
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
