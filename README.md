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

| Matcher | Explanation | Example |
|-----|-----|------|
| `to_equal` | Checks if one element equals another and returns result true or false. | `def test_to_equal():`<br>`return Expect(Expect('foo').to_equal('foo')['result']).to_equal(True)` |
| `to_be_truthy` | Passes if object is truthy (not false). | `def test_to_be_truthy():`<br>`return Expect(Expect('foo').to_be_truthy()['result']).to_equal(True)` |
| `to_be_falsey` | Passes if object is false. | `def test_to_be_falsey():`<br>`return Expect(Expect(False).to_be_falsey()['result']).to_equal(True)` |
| `to_be_none` | Passes if there is no object. | `def test_to_be_none():`<br>`return Expect(Expect(None).to_be_none()['result']).to_equal(True)`|
| `to_be_greater_than` | Passes if object A is greater than object B. | `def test_to_be_greater_than():`<br>`return Expect(Expect(x).to_be_greater_than(y)['result']).to_equal(True)` |
| `to_be_less_than` | Passes if object A is less than object B. | `def test_to_be_less_than():`<br>`return Expect(Expect(x).to_be_less_than(y)['result']).to_equal(True)` |
| `to_include` | Returns true if in the list, false if not, and reason if object is not a list. Can check for multiple elements in a list or string. | `def test_to_include():`<br>`return Expect(Expect(['foo','bar']).to_include('x')["result"]).to_equal(True)` |
| `to_not_include` | Returns true if not in the list, false if it is, and reason if object is not a list. | `def test_to_not_include():`<br>`return Expect(Expect(['x','y']).to_not_include('z')["result"]).to_equal(True)`|
| `to_output_to_stdout` | Returns true if an output is callable, an reason if not callable, or output is wrong. | `test_to_output_to_stdout():`<br>`return Expect(Expect('Hello World').to_output_to_stdout('Hello World')['reason']).to_equal('Expected: hello to be callable')`|
| `to_throw_error` | Use this matcher to specify that a block of code raises an error. | `def test_to_throw_error_method_works():`<br>`def raise_(ex):`<br>`raise ex`<br>`return Expect(Expect(lambda: raise_(Exception('foobar'))).to_throw_error('foobar')['result']).to_equal(True)` |


## Contributors:
* [Alex McCarroll](https://github.com/AlexMcCarroll)
* [Ricky Hewitt](https://github.com/rewitt94)
* [Tom Betts](https://github.com/T-Betts)
* [Hemesh Unka](https://github.com/Hemesh-Unka)

## How to contribute to this project:

See [CONTRIBUTING.md](https://github.com/DrSerpent/DrSerpent-Core/blob/master/CONTRIBUTING.md)

## Licence:

Distributed under the terms of the [MIT](https://github.com/DrSerpent/DrSerpent-Core/blob/master/LICENSE.txt) license, DrSerpent is free and open source software.
