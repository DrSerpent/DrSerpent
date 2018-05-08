import sys
from context import *

def test_executor_passes_succesful_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    sys.path.append(fizzbuzz_directory)
    from test_logic import test_fizz
    return Expect(lambda: Executor.test(test_fizz)).to_output_to_stdout('\033[92mtest_fizz\n\u001b[0m')

def test_executor_fails_broken_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(broken_fizzbuzz_directory)
    from test_broken import test_fail
    return Expect(lambda: Executor.test(test_fail)).to_output_to_stdout('\u001b[31mtest_fail:\nExpected: HEY\nGot: Fizz\n\u001b[0m')

def test_provides_reason_if_test_returns_nothing():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(broken_fizzbuzz_directory)
    from test_broken import test_no_return
    return Expect(lambda: Executor.test(test_no_return)).to_output_to_stdout(f'\u001b[31mtest_no_return:\nThis test has returned nothing. Please return the Expect.matcher pattern.\n\u001b[0m')

def test_module_calls_excute_test_the_correct_amount_of_times():
    test_module = {"module": 'test_logic', "tests": [1,2,3,4]}
    print(dir(Executor.test))
    Executor.test = Spy(Executor.test, 'Executor.test')
    Executor.module(test_module)
    return Expect(Executor.test).to_have_been_called_times(4)
