import os, sys
from broken_context import *

def test_fail():
    return Expect(Fizzbuzz.run(3)).to_equal('HEY')

def test_error():
    raise Exception('this failed deliberately')

def test_no_return():
    Expect(Fizzbuzz.run(5)).to_equal('YES')
