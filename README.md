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

## How to use:

### Getting Started:

`pip install drserpent`

Initialise file structure: `$ serpent --init`
Run all tests: `$ serpent`
Check PyPi version: `$ serpent --version`
Information about DrSerpent: `$ serpent about`

* Important to note: all tests must start with `test_`

### File Structure:



### Matchers:

* `to_equal` matcher returns result true or false:
    ```
    def test_to_equal():
        return Expect(Expect(x).to_equal(x)["result"]).to_equal(True)
    ```
* `to_include` matcher returns true if in the list, false if not, and error message if it is not a list:
    ```
    def test_to_include():
        return Expect(Expect(['x','y']).to_include('x')["result"]).to_equal(True)
    ```
* `to_not_include` matcher returns true if not in the list, false if it is, and error message if it is not a list :
    ```
    def test_to_not_include():
        return Expect(Expect(['x','y']).to_not_include('z')["result"]).to_equal(True)
    ```
* `to_output_to_stdout` matcher returns true if an output is callable, an error message if not callable, or output is wrong:
    ```
    test_to_output_to_stdout():
        return Expect(Expect('Hello World').to_output_to_stdout('Hello World')['reason']).to_equal('Expected: hello to be callable')
    ```

## Contributors:
* **[Alex McCarroll](https://github.com/AlexMcCarroll)**
* **[Ricky Hewitt](https://github.com/rewitt94)**
* **[Tom Betts](https://github.com/T-Betts)**
* **[Hemesh Unka](https://github.com/Hemesh-Unka)**

## How to contribute to this project:

See `CONTRIBUTING.md <https://github.com/DrSerpent/DrSerpent-Core/blob/master/CONTRIBUTING.md>`_

## Licence:

Distributed under the terms of the `MIT <https://github.com/DrSerpent/DrSerpent-Core/blob/master/LICENSE.txt>`_  license, DrSerpent is free and open source software.
