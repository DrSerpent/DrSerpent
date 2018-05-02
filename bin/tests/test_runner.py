import os, sys
from context import Expect
from context import get_test_directories

# return relative paths of those directories

directory_path = os.path.dirname(os.path.realpath(__file__))
test_directory = directory_path + '/example/fizz_buzz/tests'

file_paths = get_test_directories(directory_path)

print(Expect([directory_path,test_directory]).to_equal(file_paths))

# add directory_paths to sys.path

add_directory_paths(['hello'])

print(Expect(sys.path).to_include('hello'))
