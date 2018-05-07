import sys
from context import *

def test_print_green_adds_correct_ANSI_codes():
    return Expect(lambda: print_green('Passed')).to_output_to_stdout('\033[92mPassed\u001b[0m')

def test_print_red_adds_correct_ANSI_codes():
    return Expect(lambda: print_red('Failed')).to_output_to_stdout('\u001b[31mFailed\u001b[0m')

def test_executor_passes_succesful_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    sys.path.append(fizzbuzz_directory)
    from test_logic import test_fizz
    return Expect(lambda: execute_test(test_fizz)).to_output_to_stdout('\033[92mtest_fizz\u001b[0m\n')

def test_executor_fails_broken_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(broken_fizzbuzz_directory)
    from test_broken_logic import test_broken_fizz
    return Expect(lambda: execute_test(test_broken_fizz)).to_output_to_stdout('\u001b[31mtest_broken_fizz:\nExpected: HEY\nGot: Fizz\u001b[0m\n')
