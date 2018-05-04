from context import Expect

# to_equal

def test_expectation_stored_in_state():
    return Expect(Expect(2).expectation).to_equal(2)

def test_to_equal_matcher_returns_result_true():
    return Expect(Expect(2).to_equal(2)["result"]).to_equal(True)

def test_to_equal_matcher_returns_result_false():
    return Expect(Expect(2).to_equal(3)["result"]).to_equal(False)

def test_to_equal_matcher_gives_fail_reason():
    return Expect(Expect(2).to_equal(3)["reason"]).to_equal("Expected: 3\nGot: 2")

# to_include

def test_to_include_returns_true_if_in_list():
    return Expect(Expect(['yes','no']).to_include('yes')["result"]).to_equal(True)

def test_to_include_returns_false_if_not_in_list():
    return Expect(Expect(['yes','no']).to_include('maybe')["result"]).to_equal(False)

def test_to_include_returns_reason_if_expectation_is_not_a_list():
    return Expect(Expect('yes').to_include('maybe')["reason"]).to_equal('yes is not a list')

# to_not_include

def test_to_not_include_returns_true_if_not_in_list():
    return Expect(Expect(['yes','no']).to_not_include('maybe')["result"]).to_equal(True)

def test_to_not_include_returns_false_if_in_list():
    return Expect(Expect(['yes','no']).to_not_include('yes')["result"]).to_equal(False)

def test_to_not_include_returns_reason_if_expectation_is_not_a_list():
    return Expect(Expect('yes').to_not_include('maybe')["reason"]).to_equal('yes is not a list')

# to_output_to_stdout

def test_to_output_to_stdout_requires_expectation_to_be_callable():
    return Expect(Expect('hello').to_output_to_stdout('hello')['reason']).to_equal('Expected: hello to be callable')

def test_to_output_to_stdout_passes_correctly_matched_output():
    return Expect(Expect(lambda: print('hello')).to_output_to_stdout("hello")['result']).to_equal(True)

def test_to_output_to_stdout_fails_incorrectly_matched_output():
    return Expect(Expect(lambda: print('hello')).to_output_to_stdout("goodbye")['reason']).to_equal('Expected: goodbye\nGot: hello')

# to_have_been_called_with_args
