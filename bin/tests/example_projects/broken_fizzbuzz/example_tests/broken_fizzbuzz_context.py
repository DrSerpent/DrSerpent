import os
import sys

sys.path.insert(0, os.path.abspath('.') + "/bin/tests/example_projects/broken_fizzbuzz")
sys.path.insert(0, os.path.abspath('.') + "/src")

from expect import Expect
from broken_logic import *
