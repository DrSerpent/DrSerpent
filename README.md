# Dr Serpent Documentation

## Aim:
To build a easy to use testing framework for Python.

## Example:
```
def run():
    return 1 + 1

def test_number():
    Expect(run(2)).to_equal(2)
```

## PyPi URL:

https://pypi.org/project/drserpent/

## Getting Started:

`pip install drserpent`


## How to use:

Initialise file structure: `serpent --init`
Run all tests: `serpent`
Check PyPi version: `serpent --version`
Information about DrSerpent: `serpent about`

* Important to note: all tests must start with `test_`

## Contributors:
* **[Alex McCarroll](https://github.com/AlexMcCarroll)**
* **[Ricky Hewitt](https://github.com/rewitt94)**
* **[Tom Betts](https://github.com/T-Betts)**
* **[Hemesh Unka](https://github.com/Hemesh-Unka)**

## How to contribute to this project:

See `CONTRIBUTING.md <https://github.com/DrSerpent/DrSerpent-Core/blob/master/CONTRIBUTING.md>`_

## Licence:

Distributed under the terms of the `MIT <https://github.com/DrSerpent/DrSerpent-Core/blob/master/LICENSE.txt>`_  license, DrSerpent is free and open source software.
