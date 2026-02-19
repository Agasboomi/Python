# Higher order function 
#  In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

# - Higher-order function: A function that takes another function as an argument or returns a function.

# Function as parameter
def sum_numbers(nums):
    return sum(nums)
def higher_order(f,lst):
    summation = f(lst)
    return summation

res = higher_order(sum_numbers,[1,2,3])
print(res)


# function that return value 
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

# python closure 
# A closure is created when:
# - You define a function inside another function (nested function).
# - The inner function references variables from the outer function.
# - The outer function returns the inner function.

# def add_ten():
#     ten = 10
#     def add(num):
#         return num + ten
#     return add

# closure_result = add_ten()
# print(closure_result(5))  # 15
# print(closure_result(10))  # 20

# python decoration 