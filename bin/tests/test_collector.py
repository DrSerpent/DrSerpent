import os, sys
from context import *

def test_get_directories_and_their_modules():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    fizzbuzz_directory = example_directory_path + '/fizzbuzz/example_tests'
    broken_fizzbuzz_directory = example_directory_path + '/broken_fizzbuzz/example_tests'
    directory_dictionaries = get_tests(example_directory_path, 'example_tests')
    return Expect(directory_dictionaries).to_equal([
            { "directory": broken_fizzbuzz_directory, "modules": ['test_broken_logic']},
            { "directory": fizzbuzz_directory, "modules": ['test_logic']}
        ])

def test_extract_adds_directory_to_sys_path():
    extract_tests({ "directory": 'hello', "modules":[]},[])
    return Expect(sys.path).to_include('hello')

def test_extract_tests_adds_tests_in_directory_to_list():
    list = []
    extract_tests({ "directory": fizzbuzz_directory, "modules": ['test_logic']},list)
    from test_logic import test_fizz
    return Expect(list).to_include(test_fizz)

def test_reset_sys_path():
    original_sys_path = set(sys.path)
    sys.path.append('helloworld, this will be removed')
    reset_sys_path(original_sys_path)
    return Expect(sys.path).to_not_include('helloworld, this will be removed')
