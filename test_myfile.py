def test_sum():
    assert sum(5,6)==11
def test_multiply():
    assert multiply(5,6) == 30
def test_subtract():
    assert subtract(6,5) ==1

def test_divide():
    assert divide(10,2) == 5

def test_stringPlusNumber():
    assert  stringPlusNumber('abcd',str(5)) == 'abcd5'

def sum(a,b):
    return a+b
def multiply(a,b):
    return a*b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def stringPlusNumber(a,b):
    return a+str(b)

# print(sum(5,6))
# # print(multiply(5,6))
# # print(subtract(6,5))
# # print(divide(10,2))
# print(stringPlusNumber('abcd',5))
