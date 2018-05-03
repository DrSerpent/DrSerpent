from context import *

example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
(test_directories, test_modules) = get_tests(example_directory_path, 'example_tests')
add_directory_paths(test_directories)

def test_executor_passes_succesful_tests():
    from test_logic import test_fizz
    result = execute_test(test_fizz)
    return Expect(result).to_equal('Passed')
