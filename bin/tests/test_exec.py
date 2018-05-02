# return relative paths of those directories
import os
from context import Expect

current_path = os.path.abspath(__file__)
test_directory = current_path + '/example/fizz_buzz/tests'

file_paths = get_test_directories(__file__)

print(Expect(file_paths).to_equal([test_directory]))
