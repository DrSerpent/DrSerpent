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
    from test_broken import test_fail
    return Expect(lambda: execute_test(test_fail)).to_output_to_stdout('\u001b[31mtest_fail:\nExpected: HEY\nGot: Fizz\u001b[0m\n')

def test_provides_reason_if_test_returns_nothing():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(broken_fizzbuzz_directory)
    from test_broken import test_no_return
    return Expect(lambda: execute_test(test_no_return)).to_output_to_stdout(f'\u001b[31mtest_no_return:\nThis test has returned nothing. Please return the Expect.matcher pattern.\u001b[0m\n')
