import sys
from context import *

def test_executor_passes_succesful_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    sys.path.append(fizzbuzz_directory)
    from test_logic import test_fizz
    return Expect(lambda: execute_test(test_fizz)).to_output_to_stdout('Passed')

def test_executor_fails_broken_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(fizzbuzz_directory)
    from test_broken_logic import test_broken_fizz
    return Expect(lambda: execute_test(test_broken_fizz)).to_output_to_stdout('Failed')
