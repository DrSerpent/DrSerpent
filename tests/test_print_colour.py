import sys
from context import *

def test_print_green_adds_correct_ANSI_codes():
    return Expect(lambda: print_green('Passed')).to_output_to_stdout('\033[92mPassed\u001b[0m')

def test_print_red_adds_correct_ANSI_codes():
    return Expect(lambda: print_red('Failed')).to_output_to_stdout('\u001b[31mFailed\u001b[0m')
