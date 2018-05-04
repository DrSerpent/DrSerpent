class ANSI:
    RED = '\u001b[31m'
    GREEN = '\033[92m'
    RESET = '\u001b[0m'

def execute_test(test):
    if test()['result'] == True:
        print('\033[92mPassed\u001b[0m')
    else:
        print('\u001b[31mFailed\u001b[0m')

def print_green(string):
    print(ANSI.GREEN + string + ANSI.RESET)

def print_red(string):
    print(ANSI.RED + string + ANSI.RESET)
