from print_colour import *

class Executor:

    def test(test):
        result = test()
        if result is None:
            print_red(f'{test.__name__}:\nThis test has returned nothing. Please return the Expect.matcher pattern.\n')
        elif result['result'] == True:
            print_green(f'{test.__name__}\n')
        elif result['result'] == False:
            print_red(f'{test.__name__}:\n{result["reason"]}\n')

        try:
            recovery = result['recovery']

    def module(module):
        for test in module['tests']:
            Executor.test(test)
