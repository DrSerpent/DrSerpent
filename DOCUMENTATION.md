## Matchers:


#### `to_equal`
###### Checks if one element equals another and returns result true or false.
Example:
```python
def test_to_equal():
    return Expect(Expect('foo').to_equal('foo')['result']).to_equal(True)
```
#### `to_be_truthy`
###### Passes if object is truthy (not false).
Example:
```python
def test_to_be_truthy():
    return Expect(Expect('foo').to_be_truthy()['result']).to_equal(True)
```
#### `to_be_falsey`
###### Passes if object is false.
Example:
```python
def test_to_be_falsey():
    return Expect(Expect(False).to_be_falsey()['result']).to_equal(True)
```
#### `to_be_none`
###### Passes if there is no object.
Example:
```python
def test_to_be_none():
    return Expect(Expect(None).to_be_none()['result']).to_equal(True)
```
#### `to_be_greater_than`
###### Passes if object A is greater than object B.
Example:
```python
def test_to_be_greater_than():
    return Expect(Expect(x).to_be_greater_than(y)['result']).to_equal(True)
```
#### `to_be_less_than`
###### Passes if object A is less than object B.
Example:
```python
def test_to_be_less_than():
    return Expect(Expect(x).to_be_less_than(y)['result']).to_equal(True)
```
#### `to_include`
###### Returns true if in the list, false if not, and reason if object is not a list. Can check for multiple elements in a list or string.
Example:
```python
def test_to_include():
    return Expect(Expect(['foo','bar']).to_include('x')['result']).to_equal(True)
```
#### `to_not_include`
###### Returns true if not in the list, false if it is, and reason if object is not a list.
Example:
```python
def test_to_not_include():
    return Expect(Expect(['foo','bar']).to_not_include('baz')['result']).to_equal(True)
```
#### `to_output_to_stdout`
###### Returns true if an output is callable, an reason if not callable, or output is wrong.
Example:
```python
test_to_output_to_stdout():
    return Expect(Expect('Hello World').to_output_to_stdout('Hello World')['reason']).to_equal('Expected: hello to be callable')
```
#### `to_throw_error`
###### Use this matcher to specify that a block of code raises an error.
Example:
```python
def test_to_throw_error_method_works():
    def raise_(ex):
        raise ex
    return Expect(Expect(lambda: raise_(Exception('foobar'))).to_throw_error('foobar')['result']).to_equal(True)
```
