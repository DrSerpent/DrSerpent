from context import Expect

expect = Expect(2)

print("expectation")
print(expect.expectation == 2)

print("to_equal matcher")
print(expect.to_equal(2)["result"])

print("to_equal matcher false")
print(expect.to_equal(3)["result"] == False)

print("to_equal matcher false reason")
print(expect.to_equal(3)["reason"] == "Expected: 2\nGot: 3")

expect_2 = Expect(['hello'])

print("to_include matcher - true")
print(expect_2.to_include('hello')["result"] == True)

expect_3 = Expect("hello")

print("to_include matcher - not a list")
print(expect_3.to_include("hello")["result"] == False)

expect_4 = Expect([])

print("to_include matcher - not included")
print(expect_4.to_include("hello")["result"] == False)

def helloworld():
    print('hello')

expect_5 = Expect('hello')

print("to_output_to_stdout must take a callable expect")
print(expect_5.to_output_to_stdout("what")["result"] == False)

print("to_output_to_stdout gives an intelligent failure message if not callable")
print(expect_5.to_output_to_stdout("what")["reason"] == 'Expected: hello to be callable to output to stdout')

expect_5 = Expect(lambda: print("hello"))

print("matches output to stdout")
print(expect_5.to_output_to_stdout("hello")['result'] == True)

expect_5 = Expect(lambda: print("shit"))

print("provides comparison for invalid match to stdout")
print(expect_5.to_output_to_stdout("hello")['reason'] == 'Expected: shit\nGot: hello')
