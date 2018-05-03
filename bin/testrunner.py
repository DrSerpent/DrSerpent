from collector import *
from executor import *

orignal_sys_path = set(sys.path)
tests = []

directory_dictionaries = get_tests('.', 'tests')

for dict in directory_dictionaries:
    extract_tests(dict,tests)
    reset_sys_path(orignal_sys_path)

print(tests)

for t in tests:
    execute_test(t)
