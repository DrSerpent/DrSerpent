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

print("to_include matcher(true)")
print(expect_2.to_include('hello')["result"] == True)

expect_3 = Expect("hello")

print "to_include matcher(not a list)"
print(expect_3.to_include("hello")["result"] == False)

expect_4 = Expect([])

print "to_include matcher(not included)"
print(expect_4.to_include("hello")["result"] == False)
