import os, sys
from context import *

## TEST ONE

print('return relative paths of those directories named /tests')

example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
example_directories = [broken_fizzbuzz_directory,fizzbuzz_directory]

(test_directories, test_modules) = get_tests(example_directory_path, 'example_tests')

print(Expect(example_directories).to_equal(test_directories))

## TEST TWO

print('get files/modules in test directory')

example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
(test_directories, test_modules) = get_tests(example_directory_path, 'example_tests')

print(Expect(['test_broken_logic','test_logic']).to_equal(test_modules))

## TEST THREE

print('add directory_paths to sys.path')
add_directory_paths(['hello'])

print(Expect(sys.path).to_include('hello'))

## TEST FOUR

print('extracts test methods from modules')

example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
(test_directories, test_modules) = get_tests(example_directory_path, 'example_tests')

add_directory_paths(test_directories)

from test_logic import test_fizz

example_tests = extract_tests(test_modules)

print(Expect(example_tests).to_include(test_fizz))
