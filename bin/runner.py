import os, sys

def get_test_directories(top):
    test_directories = []
    for (dirpath, dirnames, filenames) in os.walk(top):
        if dirpath[-6:] == "/tests":
            test_directories.append(dirpath)
    return test_directories

def add_directory_paths(array):
    for path in array:
        sys.path.append(path)

def get_test_files(directory):
    test_filenames = []
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            if filename[0:5] == "test_" and filename[-3:] == ".py":
                test_filenames.append(filename[0:-3])
    return test_filenames
