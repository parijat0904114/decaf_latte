"""
A lambda function is a single liner function without a name.
Note that, we don't name the function, we just assign it to a variable.
We can even call a lambda function without it.
For example, if we consider a function that adds two numbers.
We can define the following way.

def add(a, b):
    return a+b

We can do the similar mathematical operation with lambda function.
add = lambda a, b: a+b
"""
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else 'undefined'  # To handle division by zero
modulus = lambda a, b: a % b
power = lambda a, b: a ** b
greater_than = lambda a, b: a > b
less_than = lambda a, b: a < b
equal = lambda a, b: a == b
not_equal = lambda a, b: a != b
max = lambda a, b: a if a > b else b
min = lambda a, b: a if a < b else b
average = lambda a, b: (a + b) / 2.00
square = lambda a: a ** 2
cube = lambda a: a ** 3
absolute = lambda a: abs(a)

# print(add(55, 22))        # Output: 77
# print(subtract(55, 22))   # Output: 33
# print(multiply(55, 22))   # Output: 1210
# print(divide(55, 22))     # Output: 2.5
# print(modulus(55, 22))    # Output: 11
# print(power(2, 3))        # Output: 8
# print(greater_than(3, 4)) # Output: False
# print(less_than(3, 4))    # Output: True
# print(equal(3, 4))        # Output: False
# print(not_equal(3, 4))    # Output: True
# print(max(3, 4))          # Output: 4
# print(min(3, 4))          # Output: 3
# print(average(3, 4))      # Output: 3.5
# print(square(4))          # Output: 16
# print(cube(2))            # Output: 8
# print(absolute(-5))       # Output: 5


# print((lambda x: x*5)(5)) # anonymous function. Didn't assign a variable at all.