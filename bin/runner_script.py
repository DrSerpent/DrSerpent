from runner import *

# (test_directories, test_filenames) = get_tests('.')

example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/tests/example'
(test_directories, test_modules) = get_tests(example_directory_path)

add_directory_paths(test_directories)
tests = extract_tests(test_modules)
