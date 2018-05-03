import os, sys
from context import *

runner = Runner

print('Should be able to return fizzbuzz results from 1 to 15')
Expect(runner.print_results(10)).to_equal("1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzbuzz")
