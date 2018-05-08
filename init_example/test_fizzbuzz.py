import os, sys

# import the matcher expect
from expect import Expect

# import the source code to be tested
from context import *

def test_fizz():
    return Expect(Fizzbuzz.run(3)).to_equal('Fizz')

def test_buzz():
    return Expect(Fizzbuzz.run(5)).to_equal('Buzz')

def test_fizzbuzz():
    return Expect(Fizzbuzz.run(15)).to_equal('Fizzbuzz')

def test_number():
    return Expect(Fizzbuzz.run(1)).to_equal(1)
