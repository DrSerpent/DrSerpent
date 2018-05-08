import os, sys
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
        if result['result'] == True:
            print_green(f'{test.__name__}\n')
        else:
            print_red(f'{test.__name__}:\n{result["reason"]}\n')
    except BaseException as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print_red(f'{test.__name__}:\nERROR: {e}\n')

def execute_module(module_dictionary):
    print(f'\n\U0001F40D  module: {module_dictionary["module"]}\n-------------------------------------------')
    if (len(module_dictionary['tests']) is 0):
        print('No tests found.')
    return
