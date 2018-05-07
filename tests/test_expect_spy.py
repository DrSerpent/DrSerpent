from expect import Expect
from spy import Spy

# to_have_been_called

def test_to_have_been_called_knows_when_spy_has_been_called():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    spy()
    return Expect(Expect(spy).to_have_been_called()['result']).to_equal(True)

def test_to_have_been_called_knows_when_spy_has_not_been_called():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    return Expect(Expect(spy).to_have_been_called()['result']).to_equal(False)

def test_to_have_been_called_gives_reason_for_fail():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    return Expect(Expect(spy).to_have_been_called()['reason']).to_equal('Spied upon function was not called')

def test_to_have_been_called_expectation_must_be_spy():
    def hello(name):
        print(f'hello {name}')
    return Expect(Expect(hello).to_have_been_called()['reason']).to_equal('Function must be a spy')

# to_have_been_called_with_args

def test_to_have_been_called_with_args_must_receive_spy_as_expectation():
    def hello(name):
        print(f'hello {name}')
    return Expect(Expect(hello).to_have_been_called_with_args(10)['reason']).to_equal('Function must be a spy')

def test_to_have_been_called_with_args_passes_if_args_match():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    spy('helloworld')
    return Expect(Expect(spy).to_have_been_called_with_args('helloworld')['result']).to_equal(True)

def test_to_have_been_called_with_args_fails_if_args_do_not_match():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    spy(10,'helloworld')
    return Expect(Expect(spy).to_have_been_called_with_args(10)['result']).to_equal(False)

def test_to_have_been_called_with_args_provides_reason_if_args_do_not_match():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    spy(10,'helloworld')
    return Expect(Expect(spy).to_have_been_called_with_args(10,'what')['reason']).to_equal("Expected args: (10, 'what')\nGot args: (10, 'helloworld')")

# to_have_been_called_times()

def test_to_have_been_called_times_expectation_must_be_spy():
    def hello(name):
        print(f'hello {name}')
    return Expect(Expect(hello).to_have_been_called_times(2)['reason']).to_equal('Function must be a spy')

def test_to_have_been_called_times_comparison_must_be_an_integer():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    return Expect(Expect(spy).to_have_been_called_times('hello')['reason']).to_equal('Argument must be an integer')

def test_to_have_been_called_times_passes_when_amount_of_calls_match():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    spy()
    spy()
    return Expect(Expect(spy).to_have_been_called_times(2)['result']).to_equal(True)

def test_to_have_been_called_times_provides_reason_if_amount_of_calls_do_not_match():
    def hello(name):
        print(f'hello {name}')
    spy = Spy(hello)
    spy()
    return Expect(Expect(spy).to_have_been_called_times(3)['reason']).to_equal('Expected calls: 3\nGot calls: 1')
