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
