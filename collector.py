import os, sys, importlib

def get_tests(top, directory_naming_convention):
    directory_dictionaries = []
    for (dirpath, dirnames, filenames) in os.walk(top):
        if dirpath.rpartition('/')[-1] == directory_naming_convention:
            test_modules = []
            for filename in filenames:
                if filename[0:5] == "test_" and filename[-3:] == ".py":
                    test_modules.append(filename[0:-3])
            directory_dictionaries.append({"directory":dirpath, "modules":test_modules})
    return directory_dictionaries

def extract_tests(directory_dictionary,tests):
    directory = directory_dictionary['directory']
    modules = directory_dictionary['modules']
    sys.path.append(directory)
    for test_file in modules:
        module = importlib.import_module(test_file)
        attributes = dir(module)
        for attribute in attributes:
            if attribute[0:5] == "test_":
                test = getattr(module, attribute)
                if callable(test):
                    tests.append(test)

def reset_sys_path(original_sys_path):
    to_remove = [path for path in sys.path if path not in original_sys_path]
    for path in to_remove:
        sys.path.remove(path)
