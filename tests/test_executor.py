import sys
from context_src import *

def test_print_green_adds_correct_ANSI_codes():
    return Expect(lambda: print_green('Passed')).to_output_to_stdout('\033[92mPassed\u001b[0m')

def test_print_red_adds_correct_ANSI_codes():
    return Expect(lambda: print_red('Failed')).to_output_to_stdout('\u001b[31mFailed\u001b[0m')

def test_execute_warns_if_test_has_no_return_value():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(broken_fizzbuzz_directory)
    from test_broken import test_no_return
    return Expect(lambda: execute_test(test_no_return)).to_output_to_stdout('\u001b[31mtest_no_return:\nNothing returned.\n\u001b[0m')

def test_execute_passes_succesful_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    sys.path.append(fizzbuzz_directory)
    from test_logic import test_fizz
    return Expect(lambda: execute_test(test_fizz)).to_output_to_stdout('\033[92mtest_fizz\n\u001b[0m')

def test_execute_fails_broken_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(broken_fizzbuzz_directory)
    from test_broken import test_fail
    return Expect(lambda: execute_test(test_fail)).to_output_to_stdout('\u001b[31mtest_fail:\nExpected: HEY\nGot: Fizz\n\u001b[0m')

def test_execute_shows_stacktrace_for_errors():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(broken_fizzbuzz_directory)
    from test_broken import test_error
    old_stdout = sys.stdout
    sys.stdout = output = StringIO()
    execute_test(test_error)
    sys.stdout = old_stdout
    return Expect(output.getvalue()).to_include('ERROR: this failed deliberately')

def test_module_warns_if_test_file_is_empty():
    module_dictionary = {"module":"empty_module", "tests":[]}
    return Expect(lambda: execute_module(module_dictionary)).to_output_to_stdout(f'\n\U0001F40D  module: empty_module\n-------------------------------------------\nNo tests found.\n')

def test_module_counts_passes_and_fails():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    sys.path.append(fizzbuzz_directory)
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    sys.path.append(broken_fizzbuzz_directory)
    from test_logic import test_fizz, test_buzz
    from test_broken import test_fail, test_error
    module_dictionary = {"module":"empty_module", "tests":[test_fizz, test_buzz, test_fail, test_error]}
    old_stdout = sys.stdout
    sys.stdout = output = StringIO()
    results = execute_module(module_dictionary)
    sys.stdout = old_stdout
    return Expect(results).to_equal({"Passed":2,"Failed":2})
