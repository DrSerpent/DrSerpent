from collector import *
from executor import *

# (test_directories, test_filenames) = get_tests('.')

(test_directories, test_modules) = get_tests('.', 'tests')


add_directory_paths(test_directories)
extracted_tests = extract_tests(test_modules)

print('----------')
print(test_modules)
print('----------')

print('----------')
print(extracted_tests)
print('----------')

for t in extracted_tests:
    print(execute_test(t))
