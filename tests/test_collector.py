import os, sys
from context_src import *

def test_reset_sys_path():
    original_sys_path = set(sys.path)
    sys.path.append('helloworld, this will be removed')
    reset_sys_path(original_sys_path)
    return Expect(sys.path).to_not_include('helloworld, this will be removed')

def test_get_directories_and_their_modules():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    directory_dictionaries = get_tests(example_directory_path, 'example_tests')
    return Expect(directory_dictionaries).to_equal([
            {"directory": broken_fizzbuzz_directory, "modules": ['test_broken']},
            {"directory": fizzbuzz_directory, "modules": ['test_logic']}
        ])

def test_print_intelligent_error_message_if_no_tests_found():
    intelligent_error_message = """
        No tests have been found -
        please note that there are strict naming conventions:
        1. Directories are named "tests"
        2. Test files start with "test_"
        3. Test functions start with "test_"
        e.g. repository_path/src/tests/test_descriptive_name.py contains def test_describe
        """
    return Expect(lambda: no_tests_found()).to_output_to_stdout(intelligent_error_message)

def test_directory_dictionary_to_module_dictionaries():
    original_sys_path = set(sys.path)
    list = []
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    from test_logic import test_fizz, test_buzz, test_fizzbuzz, test_number
    module_dictionaries = extract_module_dictionaries(
        { "directory": fizzbuzz_directory, "modules": ['test_logic']},
        original_sys_path
        )
    return Expect(module_dictionaries).to_equal([
        {"module": 'test_logic', "tests": [test_buzz, test_fizz, test_fizzbuzz, test_number]}
    ])

def test_extracting_module_dictionaries_does_not_change_sys_path():
    original_sys_path = set(sys.path)
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    module_dictionaries = extract_module_dictionaries(
        { "directory": fizzbuzz_directory, "modules": ['test_logic']},
        original_sys_path
        )
    return Expect(set(sys.path)).to_equal(original_sys_path)

def test_collect_module_returns_module():
    original_sys_path = set(sys.path)
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    module_dictionary = collect_module(
        example_directory_path, 'fizzbuzz/example_tests/test_logic.py',
        original_sys_path
        )
    import test_logic
    return Expect(module_dictionary['module']).to_equal('test_logic')

def test_collect_module_returns_module_containing_tests():
    original_sys_path = set(sys.path)
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    module_dictionary = collect_module(
        example_directory_path, 'fizzbuzz/example_tests/test_logic.py',
        original_sys_path
        )
    from test_logic import test_fizz, test_buzz
    return Expect(module_dictionary['tests']).to_include(test_fizz, test_buzz)

def test_collect_module_does_not_change_sys_path():
    original_sys_path = set(sys.path)
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    module_dictionary = collect_module(
        example_directory_path, 'fizzbuzz/example_tests/test_logic.py',
        original_sys_path
        )
    return Expect(set(sys.path)).to_equal(original_sys_path)
