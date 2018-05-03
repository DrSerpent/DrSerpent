import os, sys
from context import *

print('Fizzbuzz')

print('Should return fizz for multiples of 3')
print(Expect(fizz(3)).to_equal('Fizz'))
