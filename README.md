# Dr Serpent Documentation

## Description:
Dr Serpent 🐍 in an easy to use testing framework for Python focusing on Behaviour Driven Development and Test Driven Development processes.

## Example:

```python
# file
def run():
    return 1 + 1

# test_file
def test_number():
    Expect(run(2)).to_equal(2)
```

## How to use:

[Click Here](https://pypi.org/project/drserpent/) to visit the PyPi URL.

### Getting Started:

`pip install drserpent`

- Initialise file structure: `$ serpent --init`
- Initialise dummy file structure (FizzBuzz): `$ serpent example`
- Run all tests: `$ serpent`
- Check PyPi version: `$ serpent --version`
- Information about DrSerpent: `$ serpent about`

**Important to note: all tests must start with `test_`**

### File Structure:

```
.
|–– code.py
|–– tests
    |
    |–– context.py
    |–– test_code.py
```

The `context.py` file establishes the file route. Run `$ serpent example` for a clearer understanding of how to use DrSerpent.


### Matchers:

[`to_equal`]()
[`to_be_truthy`]()
[`to_be_falsey`]()
[`to_be_none`]()
[`to_be_greater_than`]()
[`to_be_less_than`]()
[`to_include`]()
[`to_not_include`]()
[`to_output_to_stdout`]()
[`to_throw_error`]()

## Contributors:
* [Alex McCarroll](https://github.com/AlexMcCarroll)
* [Ricky Hewitt](https://github.com/rewitt94)
* [Tom Betts](https://github.com/T-Betts)
* [Hemesh Unka](https://github.com/Hemesh-Unka)

## How to contribute to this project:

See [CONTRIBUTING.md](https://github.com/DrSerpent/DrSerpent-Core/blob/master/CONTRIBUTING.md)

## Licence:

Distributed under the terms of the [MIT](https://github.com/DrSerpent/DrSerpent-Core/blob/master/LICENSE.txt) license, DrSerpent is free and open source software.
