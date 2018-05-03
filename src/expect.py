class Expect(object):

    def __init__(self, expectation):
        self.expectation = expectation

    def to_equal(self, comparison):
        if self.expectation == comparison:
            return {"result": True}
        else:
            return {
                "result": False,
                "reason": f"Expected: {self.expectation}\nGot: {comparison}"
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

    def to_output_to_stdout(self, comparison):
        if callable(self.expectation) is not True:
            return {
                "result": False,
                "reason": f"Expected: {self.expectation} to be callable to output to stdout"
                }
        elif:
            return {
                "result": False,
                "reason": f"Expected: {self.expectation}\nGot: {comparison}"
                }
