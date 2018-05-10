from setuptools import setup, find_packages

version = {}
with open('./version.py') as fp:
    exec(fp.read(), version)
    
with open('PyPiREADME.rst') as f:
    long_description = f.read()
   
setup(
    name='drserpent',
    version=version['__version__'],
    packages=['scripts', 'init', 'init_example'],
    py_modules=['expect', 'runner', 'collector', 'executor'],
    include_package_data=True,
    install_requires=[
        'emoji',
        'Click',
    ],
    description='Python Testing Framework',
    long_description=long_description,
    url='https://github.com/DrSerpent/DrSerpent-Core',
    author='Tom Betts',
    author_email='tom.betts@live.co.uk',
    license='MIT',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'serpent=scripts.main:cli'
        ],
    }
    )
