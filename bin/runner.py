import os

def get_test_directories(top):
    test_directories = []
    for (dirpath, dirnames, filenames) in os.walk(top):
        if dirpath[-6:] == "/tests":
            test_directories.append(dirpath)
    return test_directories
