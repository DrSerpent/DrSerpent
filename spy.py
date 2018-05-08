# def spy_on(named_function):
#     exec(f"nonlocal {named_function}; {named_function} = Spy({named_function})")

class Spy(object):

    # def on(named_function):
    #     exec(f"nonlocal {named_function}; {named_function} = self({named_function})")

    def __init__(self, original):
        # print(original.__name__)
        # self.__name__ = original.__name__
        self.original = original
        self.called = False
        self.count = 0

    def __call__(self, *args):
        self.args = args
        self.called = True
        self.count += 1

    def recover(self):
        return self.original
