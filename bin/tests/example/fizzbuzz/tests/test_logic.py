import os, sys
from context import *

fizz_buzz = Fizzbuzz
print('Fizzbuzz')

print('Should return fizz for multiples of 3')
print(Expect(fizz_buzz.fizz(3)).to_equal('Fizz'))

print('Should return buzz for multiples of 5')
print(Expect(fizz_buzz.buzz(5)).to_equal('Buzz'))

print('Should return fizzbuzz for multiples of 15')
print(Expect(fizz_buzz.fizzbuzz(15)).to_equal('Fizzbuzz'))
