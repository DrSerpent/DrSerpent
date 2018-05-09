# Documentation:

## Getting Started:

`pip install drserpent`

- Initialise file structure: `$ serpent --init`
- Initialise dummy file structure (FizzBuzz): `$ serpent --example`
- Run all tests: `$ serpent`
- Run specific test file: `$ serpent test_[FILENAME]`
- Check PyPi version: `$ serpent --version`
- Information about DrSerpent: `$ serpent --about`

## Conventions:
**The following are strict conventions that need to be adhered to**

- All test files start `test_[FILENAME]`.
- All test functions start `test_[FILENAME]`.
- Test directories are named `tests`.
- The `context.py` file establishes the file route and is necessary in order to import the code from the parent directory that needs to be tested. Run `$ serpent example` for a clearer understanding of how to use DrSerpent.

### File Structure:

```
.
|–– code.py
|–– tests
    |
    |–– context.py
    |–– test_code.py
```

## Matchers:


#### `to_equal`
##### Checks if one element equals another and returns result true or false.
Passing Example:
```python
def test_to_equal():
    return Expect('foo').to_equal('foo')
```
#### `to_be_truthy`
##### Passes if object is truthy (not False or not 0).
Passing Example:
```python
def test_to_be_truthy():
    return Expect('foo').to_be_truthy()
```
#### `to_be_falsey`
##### Passes if object is falsey (False or 0).
Passing Example:
```python
def test_to_be_falsey():
    return Expect(False).to_be_falsey()
```
#### `to_be_none`
##### Passes if there is no object (None).
Passing Example:
```python
def test_to_be_none():
    return Expect(None).to_be_none()
```
#### `to_be_greater_than`
##### Passes if object A is greater than object B.
Passing Example:
```python
def test_to_be_greater_than():
    return Expect(2).to_be_greater_than(1)
```
#### `to_be_less_than`
##### Passes if object A is less than object B.
Passing Example:
```python
def test_to_be_less_than():
    return Expect(1).to_be_less_than(2)
```
#### `to_include`
##### Returns true if in the list, false if not, and reason if object is not a list. Can check for multiple elements in a list or string.
Passing Example:
```python
def test_to_include():
    return Expect(['foo','bar']).to_include('foo', 'bar')
```
#### `to_not_include`
##### Returns true if not in the list, false if it is, and reason if object is not a list.
Passing Example:
```python
def test_to_not_include():
    return Expect(['foo','bar']).to_not_include('baz')
```
#### `to_output_to_stdout`
##### Returns true if an output is callable, and a reason if not callable, or output is wrong.
Passing Example:
```python
test_to_output_to_stdout():
    return Expect('Hello World').to_output_to_stdout('Hello World'))
```
#### `to_throw_error`
##### Specifies if a block of code raises an error.
Passing Example:
```python
def test_to_throw_error():
    def raise_(ex):
        raise ex
    return Expect(lambda: raise_(Exception('foobar'))).to_throw_error('foobar'))
```
