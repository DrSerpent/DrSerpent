import os, sys
from context import *

print('return relative paths of those directories named /tests')

directory_path = os.path.dirname(os.path.realpath(__file__))
test_directory = directory_path + '/example/fizzbuzz/tests'

file_paths = get_test_directories(directory_path)

print(Expect([directory_path,test_directory]).to_equal(file_paths))

print('add directory_paths to sys.path')
add_directory_paths(['hello'])

print(Expect(sys.path).to_include('hello'))

print('get files/modules in test directory')

test_directory = directory_path + '/example/fizzbuzz/tests'
test_files = get_test_files(test_directory)

print(Expect(['test_printer','test_logic']).to_equal(test_files))
