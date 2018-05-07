from collector import *
from executor import *
import emoji


def run():
    orignal_sys_path = set(sys.path)

    directory_dictionaries = get_tests('.', 'tests')

    module_dictionaries = []

    for directory_dictionary in directory_dictionaries:
        list_of_dictionaries = extract_module_dictionaries(directory_dictionary)
        for module_dictionary in list_of_dictionaries:
            module_dictionaries.append(module_dictionary)
        reset_sys_path(orignal_sys_path)

    # if len(tests) == 0:
    #     no_tests_found()

    for module_dictionary in module_dictionaries:
        print(f'\n\U0001F40D module: {module_dictionary["module"]}')
        print('-------------------------------------------')
        for test in module_dictionary['tests']:
            execute_test(test)

    # for t in tests:
    #     execute_test(t)
