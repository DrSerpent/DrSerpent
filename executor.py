import os, sys
from io import StringIO
import traceback

class ANSI:
    RED = '\u001b[31m'
    GREEN = '\033[92m'
    RESET = '\u001b[0m'

def print_green(string):
    print(ANSI.GREEN + string + ANSI.RESET)

def print_red(string):
    print(ANSI.RED + string + ANSI.RESET)

def execute_test(test):
    try:
        result = test()
        if result == None:
            print_red(f'{test.__name__}:\nNothing returned.\n')
            return False
        elif result['result'] == True:
            print_green(f'{test.__name__}\n')
            return True
        else:
            print_red(f'{test.__name__}:\n{result["reason"]}\n')
            return False
    except BaseException as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print_red(f'{test.__name__}:\nERROR: {e}\n')
            print_red(f'{traceback.format_list(traceback.extract_tb(exc_tb))[-1]}\n')
            return False

def execute_module(module_dictionary):
    print(f'\n\U0001F40D  module: {module_dictionary["module"]}\n-------------------------------------------')
    if (len(module_dictionary['tests']) is 0):
        print('No tests found.\n\n')
    else:
        pass_count = 0
        fail_count = 0
        for test in module_dictionary["tests"]:
            if execute_test(test):
                pass_count += 1
            else:
                fail_count += 1
        print(f'\U0001F6A8  Passed: {pass_count}, Failed: {fail_count}\n\n')

        return {"Passed": pass_count, "Failed": fail_count}
