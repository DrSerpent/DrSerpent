class Spy(object):

    def __init__(self, original):
        self.original = original
        self.called = False
        self.count = 0

    def __call__(self, *args):
        self.args = args
        self.called = True
        self.count += 1
