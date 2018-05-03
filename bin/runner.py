import os, sys, importlib

def get_tests(top):
    test_directories = []
    test_files = []
    for (dirpath, dirnames, filenames) in os.walk(top):
        if dirpath[-6:] == "/tests":
            test_directories.append(dirpath)
            for filename in filenames:
                if filename[0:5] == "test_" and filename[-3:] == ".py":
                    print(f"adding: {dirpath}/{filename}")
                    test_files.append(filename[0:-3])
    return (test_directories,test_files)


def add_directory_paths(array):
    for path in array:
        sys.path.append(path)

def extract_tests(test_modules):
    tests = []
    for test_file in test_modules:
        module = importlib.import_module(test_file)
        attributes = dir(module)
        for attribute in attributes:
            if attribute[0:5] == 'test_':
                tests.append(getattr(module, attribute))
    return tests

# print(sys.path)
#
# import test_logic
#
# print(dir(test_logic))
