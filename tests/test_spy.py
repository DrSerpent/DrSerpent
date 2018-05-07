from context import Expect
from spy import Spy

def test_spy_on_returns_a_callable_object():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    return Expect(callable(spy)).to_equal(True)

def test_spy_stores_original_function():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    return Expect(spy.original).to_equal(hello)

# Throw Error Test
#
# def test_spy_can_only_be_used_on_a_function():
#     def hello(name):
#         print(f'hello {name}')
#     spy = Spy(hello)
#     return Expect(callable(spy)).to_equal(True)

def test_spy_knows_if_it_has_not_been_called():
    spy = Spy(6)
    return Expect(spy.called).to_equal(False)

def test_spy_knows_if_it_has_been_called():
    spy = Spy(6)
    spy()
    return Expect(spy.called).to_equal(True)

def test_spy_stores_arguments_when_called():
    spy = Spy(6)
    spy([10,20],'yes')
    return Expect(spy.args).to_equal(([10,20],'yes'))

# def test_spy_counts_number_of_calls():
#     spy = Spy(6)
#     spy()
#     return Expect(spy.called).to_equal(True)
