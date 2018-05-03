import os
import sys
sys.path.insert(0, os.path.abspath('.') + "/bin/tests/example/fizzbuzz")
sys.path.insert(0, os.path.abspath('.') + "/src")
print(sys.path)

from expect import Expect
from logic import *
