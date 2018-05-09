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

    def to_be_truthy(self):
        if self.expectation != False:
            return {"result": True}
        else:
            return {
                "result": False,
                "reason": f"Expected: not False\nGot: {self.expectation}"
                }

    def to_be_falsey(self):
        if self.expectation == False:
            return {"result": True}
        else:
            return {
                "result": False,
                "reason": f"Expected: False\nGot: {self.expectation}"
                }

    def to_be_none(self):
        if self.expectation == None:
            return {"result": True}
        else:
            return {
                "result": False,
                "reason": f"Expected: None\nGot: {self.expectation}"
                }

    def to_be_greater_than(self, comparison):
        if self.expectation > comparison:
            return {"result": True}
        else:
            return {
                "result": False,
                "reason": f"Expected: {self.expectation} to be greater than {comparison}\nGot: False"
                }

    def to_be_less_than(self, comparison):
        if self.expectation < comparison:
            return {"result": True}
        else:
            return {
                "result": False,
                "reason": f"Expected: {self.expectation} to be less than {comparison}\nGot: False"
                }

    def to_include(self, *args):
        for i in range(len(args)):
            comparison = args[i]
            if type(self.expectation) is str and type(comparison) is not str:
                return {
                    "result": False,
                    "reason": f"{type(self.expectation)} cannot contain {type(comparison)}"
                    }
            elif type(self.expectation) is not list and type(self.expectation) is not str:
                return {
                    "result": False,
                    "reason": f"{self.expectation} is not a list or string"
                    }
            elif comparison not in self.expectation:
                return {
                    "result": False,
                    "reason": f"{self.expectation} does not include {comparison}"
                    }
        return {
            "result": True
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

    def to_throw_error(self, comparison):
        if callable(self.expectation) is not True:
            return {
                "result": False,
                "reason": f"Expected: {self.expectation} to be callable"
                }
        else:
            try:
                self.expectation()
                return {
                    "result": False,
                    "reason": "No Error"
                    }
            except Exception as e:
                if comparison == str(e):
                    return {
                        "result": True
                    }
                else:
                    return {
                        "result": False,
                        "reason": f"Expected: {comparison}\nGot: {str(e)}"
                        }
