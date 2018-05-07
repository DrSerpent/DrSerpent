import os
import sys

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = current_directory.rpartition('/')[0]

sys.path.insert(1, parent_directory)

from expect import Expect
from logic import *
