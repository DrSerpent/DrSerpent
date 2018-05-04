from collector import *
from executor import *

def run():
    # orignal_sys_path = set(sys.path)
    tests = []

    directory_dictionaries = get_tests('.', 'tests')

    for directories in directory_dictionaries:
        extract_tests(directories, tests)
        # reset_sys_path(orignal_sys_path)

    for t in tests:
        execute_test(t)
