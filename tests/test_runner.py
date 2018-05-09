from io import StringIO
import os, sys
from runner import *
from expect import *

def test_run_all_collects_and_executes_all_tests():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    original_stdout = sys.stdout
    sys.stdout = output = StringIO()
    run_all(example_directory_path,'example_tests')
    sys.stdout = original_stdout
    return Expect(output.getvalue()).to_include(
        'test_fizz',
        'test_buzz',
        'test_fizzbuzz',
        'test_number',
        'test_fail',
        'test_error',
        'test_no_return',
        'Passed: 4, Failed: 3'
    )

def test_run_module_collects_and_executes_all_tests_in_module():
    example_directory_path = os.path.dirname(os.path.realpath(__file__)) + '/example_projects'
    original_stdout = sys.stdout
    sys.stdout = output = StringIO()
    run_module(example_directory_path,'fizzbuzz/example_tests/test_logic.py')
    sys.stdout = original_stdout
    return Expect(output.getvalue()).to_include(
        'test_fizz',
        'test_buzz',
        'test_fizzbuzz',
        'test_number',
        'Passed: 4, Failed: 0'
    )
