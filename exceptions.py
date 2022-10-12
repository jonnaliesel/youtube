"""
Trying exception handling
"""

try:
    div = 5/0

except Exception as err:
    print('Error: ', err)

try:
    num = int(input("Enter an Integer: "))
except ValueError:
    print(f'Hey, that\'s not an Integer')

try:
    sum = 0
    file = open('numbers.txt', 'r')
    for number in file:
        sum = sum + 1.0/int(number)
    print(sum)
except ZeroDivisionError:
    print('Division by zero is not allowed')
except IOError:
    print('The file does not exist')
finally:
    print('Hope is worked:', sum)
    file.close()

# Raise error
a = 1

def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError("This is not a string")

try:
    RaiseException(a)
    print(a)
except ValueError as err:
    print(err)

# Assertion
def TestCase(a, b):
    assert a < b, f"Error: {a} is not less than {b}"
    return a, b
try:
    TestCase(2, 1)
except AssertionError as err:
    print(err)

try:
    a, b = TestCase(1, 2)
    print(f'Yes that\'s right, {a} is less than {b}!')
except AssertionError as err:
    print(err)