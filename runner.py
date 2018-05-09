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

    for module_dictionary in module_dictionaries:
        execute_module(module_dictionary)

def run_test():
    return
