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

[Click Here](https://pypi.org/project/drserpent/)

## How to use:

### Getting Started:

`pip install drserpent`

Initialise file structure: `$ serpent --init`
Initialise dummy file structure (FizzBuzz): `$ serpent example`
Run all tests: `$ serpent`
Check PyPi version: `$ serpent --version`
Information about DrSerpent: `$ serpent about`

* Important to note: all tests must start with `test_`

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

| Matcher | Result | Example |
|-----|-----|------|
| `to_equal` | Returns result true or false | `def test_to_equal(): <br> return Expect(Expect(x).to_equal(x)["result"]).to_equal(True)` |
| `to_include` | Returns true if in the list, false if not, and error message if object is not a list | `def test_to_include(): <br> return Expect(Expect(['x','y']).to_include('x')["result"]).to_equal(True)` |
| `to_not_include` | Returns true if not in the list, false if it is, and error message if object is not a list| `def test_to_not_include(): <br> return Expect(Expect(['x','y']).to_not_include('z')["result"]).to_equal(True)`|
| `to_output_to_stdout` | Returns true if an output is callable, an error message if not callable, or output is wrong | `test_to_output_to_stdout(): <br> return Expect(Expect('Hello World').to_output_to_stdout('Hello World')['reason']).to_equal('Expected: hello to be callable')`|

## Contributors:
* [Alex McCarroll](https://github.com/AlexMcCarroll)
* [Ricky Hewitt](https://github.com/rewitt94)
* [Tom Betts](https://github.com/T-Betts)
* [Hemesh Unka](https://github.com/Hemesh-Unka)

## How to contribute to this project:

See [CONTRIBUTING.md](https://github.com/DrSerpent/DrSerpent-Core/blob/master/CONTRIBUTING.md)

## Licence:

Distributed under the terms of the [MIT](https://github.com/DrSerpent/DrSerpent-Core/blob/master/LICENSE.txt) license, DrSerpent is free and open source software.
