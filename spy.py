class Spy(object):

    def __init__(self, original):
        self.original = original
        self.called = False

    def __call__(self, *args):
        self.args = args
        self.called = True
