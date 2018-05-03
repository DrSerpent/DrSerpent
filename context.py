from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

print('hello')

sys.stdout = old_stdout

print(mystdout.getvalue())
