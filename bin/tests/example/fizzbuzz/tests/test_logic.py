import os, sys
from context import *

print('Fizzbuzz')

print('Should return fizz for multiples of 3')
print(Expect(Fizzbuzz.run(3)).to_equal('Fizz'))

print('Should return buzz for multiples of 5')
print(Expect(Fizzbuzz.run(5)).to_equal('Buzz'))

print('Should return fizzbuzz for multiples of 15')
print(Expect(Fizzbuzz.run(15)).to_equal('Fizzbuzz'))

print('Should return a number if not divisible by 3 or 5')
print(Expect(Fizzbuzz.run(1)).to_equal(1))
