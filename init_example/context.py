import os
import sys

# This is based on the assumption the code to be tested is in the parent directory
# For example my_repository/src/tests

# this gets the file path of the parent directory
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = current_directory.rpartition('/')[0]

# this adds the parent directory to a list of accesible directories
sys.path.insert(1, parent_directory)

# import the source code
from fizzbuzz import *
