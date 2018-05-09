from collector import *
from executor import *

def run_all():
    original_sys_path = set(sys.path)

    directory_dictionaries = get_tests('.', 'tests')

    module_dictionaries = []

    for directory_dictionary in directory_dictionaries:
        list_of_dictionaries = extract_module_dictionaries(directory_dictionary,original_sys_path)
        for module_dictionary in list_of_dictionaries:
            module_dictionaries.append(module_dictionary)

    pass_count = 0
    fail_count = 0

    for module_dictionary in module_dictionaries:
        count = execute_module(module_dictionary)
        try:
            pass_count += count['Passed']
            fail_count += count['Failed']
        except:
            pass

    if pass_count is 0 and fail_count is 0:
        no_tests_found()
    else:
        print(f"""
    \U0001F40D  Test count:
    -------------------------------------------
    \U0001F6A8  Passed: {pass_count}, Failed: {fail_count}
    \n\n""")

def run_test(path_to):
    original_sys_path = set(sys.path)

    module_dictionary = collect_module('.',path_to,original_sys_path)

    execute_module(module_dictionary)
