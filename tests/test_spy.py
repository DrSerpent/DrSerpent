from context import Expect
from spy import Spy

def test_spy_on_returns_a_callable_object():
    spy = Spy(6)
    return Expect(callable(spy)).to_equal(True)

def test_spy_on_returns_a_callable_object():
    spy = Spy(6)
    spy()
    return Expect(spy.called).to_equal(True)
