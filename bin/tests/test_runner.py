# return relative paths of those directories
import os
from context import Expect
from context import get_test_directories

# print(os.path.dirname('.'))

directory_path = os.path.dirname(os.path.realpath(__file__))
test_directory = directory_path + '/example/fizz_buzz/tests'

file_paths = get_test_directories(directory_path)

print(Expect([directory_path,test_directory]).to_equal(file_paths))
