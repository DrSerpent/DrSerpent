import os, sys
from context import *

## TEST ONE

print('return relative paths of those directories named /tests')

example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example'
test_directory = example_directory_path + '/fizzbuzz/tests'

(test_directories, test_modules) = get_tests(example_directory_path)

print(Expect([test_directory]).to_equal(test_directories))

## TEST TWO

print('get files/modules in test directory')

example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example'
(test_directories, test_modules) = get_tests(example_directory_path)

print(Expect(['test_logic']).to_equal(test_modules))

## TEST THREE

print('add directory_paths to sys.path')
add_directory_paths(['hello'])

print(Expect(sys.path).to_include('hello'))

## TEST FOUR

print('extracts test methods from modules')

example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example'
(test_directories, test_modules) = get_tests(example_directory_path)

add_directory_paths(test_directories)

from test_logic import test_fizz

tests = extract_tests(test_modules)

print(Expect(tests).to_include(test_fizz))
