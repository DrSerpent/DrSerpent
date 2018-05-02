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
