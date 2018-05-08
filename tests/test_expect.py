from context_src import Expect

# to_equal

def test_expectation_stored_in_state():
    return Expect(Expect(2).expectation).to_equal(2)

def test_to_equal_matcher_returns_result_true():
    return Expect(Expect(2).to_equal(2)["result"]).to_equal(True)

def test_to_equal_matcher_returns_result_false():
    return Expect(Expect(2).to_equal(3)["result"]).to_equal(False)

def test_to_equal_matcher_gives_fail_reason():
    return Expect(Expect(2).to_equal(3)["reason"]).to_equal("Expected: 3\nGot: 2")

# to_be

def test_to_be_truthy_returns_true():
    return Expect(Expect('foo').to_be_truthy()['result']).to_equal(True)

def test_to_be_truthy_returns_false():
    return Expect(Expect(False).to_be_truthy()['result']).to_equal(False)

def test_to_be_falsey_returns_true():
    return Expect(Expect(False).to_be_falsey()['result']).to_equal(True)

def test_to_be_falsey_returns_false():
    return Expect(Expect("foo").to_be_falsey()['result']).to_equal(False)

def test_to_be_none_returns_true():
    return Expect(Expect(None).to_be_none()['result']).to_equal(True)

def test_to_be_none_returns_false():
    return Expect(Expect("foo").to_be_none()['result']).to_equal(False)

# to_be_compared

def test_to_be_greater_than_returns_result_true():
    return Expect(Expect(3).to_be_greater_than(2)["result"]).to_equal(True)

def test_to_be_greater_than_returns_result_false():
    return Expect(Expect(2).to_be_greater_than(3)["result"]).to_equal(False)

def test_to_be_less_than_returns_result_true():
    return Expect(Expect(3).to_be_less_than(4)["result"]).to_equal(True)

def test_to_be_less_than_returns_result_false():
    return Expect(Expect(4).to_be_less_than(3)["result"]).to_equal(False)

# to_include

def test_to_include_returns_true_if_in_list():
    return Expect(Expect(['yes','no']).to_include('yes')["result"]).to_equal(True)

def test_to_include_returns_true_if_in_string():
    return Expect(Expect('hellworld').to_include('ell')["result"]).to_equal(True)

def test_to_include_returns_false_if_not_in_list():
    return Expect(Expect(['yes','no']).to_include('maybe')["result"]).to_equal(False)

def test_to_include_returns_false_if_not_in_string():
    return Expect(Expect('hellworld').to_include('e.ll')["result"]).to_equal(False)

def test_to_include_returns_reason_if_expectation_is_not_a_list_or_string():
    return Expect(Expect(12).to_include('maybe')["reason"]).to_equal('12 is not a list or string')

def test_to_include_returns_reason_if_searching_for_something_other_than_string_in_string():
    return Expect(Expect('yes').to_include([])["reason"]).to_equal("<class 'str'> cannot contain <class 'list'>")


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

#throw_error

def test_to_throw_error_method_works():
    def raise_(ex):
        raise ex
    return Expect(Expect(lambda: raise_(Exception('foobar'))).to_throw_error('foobar')['result']).to_equal(True)

def test_to_throw_error_no_error():
    def raise_(ex):
        raise ex
    return Expect(Expect(lambda: raise_(Exception('foobar'))).to_throw_error('foo')['result']).to_equal(False)

def test_to_throw_error_not_callable():
    def raise_(ex):
        raise ex
    return Expect(Expect('foobar').to_throw_error('foobar')['result']).to_equal(False)
