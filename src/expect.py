from io import StringIO
import sys

class Expect(object):

    def __init__(self, expectation):
        self.expectation = expectation

    def to_equal(self, comparison):
        if self.expectation == comparison:
            return {"result": True}
        else:
            return {
                "result": False,
                "reason": f"Expected: {comparison}\nGot: {self.expectation}"
                }

    def to_include(self, comparison):
        if type(self.expectation) is not list:
            return {
                "result": False,
                "reason": f"{self.expectation} is not a list"
                }
        elif comparison in self.expectation:
                return {"result": True}
        else:
            return {
                "result": False,
                "reason": f"{self.expectation} does not include {comparison}"
                }

    def to_not_include(self, comparison):
        if type(self.expectation) is not list:
            return {
                "result": False,
                "reason": f"{self.expectation} is not a list"
                }
        elif comparison in self.expectation:
            return {
                "result": False,
                "reason": f"{self.expectation} does not include {comparison}"
                }
        else:
            return {
                "result": True
            }

    def to_output_to_stdout(self, comparison):
        if callable(self.expectation) is not True:
            return {
                "result": False,
                "reason": f"Expected: {self.expectation} to be callable"
                }
        else:
            old_stdout = sys.stdout
            sys.stdout = output = StringIO()
            self.expectation()
            sys.stdout = old_stdout
            output = output.getvalue()[0:-1]
            if output == comparison:
                return {"result": True}
            else:
                return {
                    "result": False,
                    "reason": f"Expected: {comparison}\nGot: {output}"
                    }

    # def to_have_been_called_with_args(*args):
    #     return
