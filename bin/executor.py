def execute_test(test):
    if test()['result'] == True:
        print('Passed')
    else:
        print('Failed')
