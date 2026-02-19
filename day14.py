# Higher order function 
#  In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable

# - Higher-order function: A function that takes another function as an argument or returns a function.

# Function as parameter
# def sum_numbers(nums):
#     return sum(nums)
# def higher_order(f,lst):
#     summation = f(lst)
#     return summation

# res = higher_order(sum_numbers,[1,2,3])
# print(res)


# function that return value 
# def square(x):          # a square function
#     return x ** 2

# def cube(x):            # a cube function
#     return x ** 3

# def absolute(x):        # an absolute value function
#     if x >= 0:
#         return x
#     else:
#         return -(x)

# def higher_order_function(type): # a higher order function returning a function
#     if type == 'square':
#         return square
#     elif type == 'cube':
#         return cube
#     elif type == 'absolute':
#         return absolute

# result = higher_order_function('square')
# print(result(3))       # 9
# result = higher_order_function('cube')
# print(result(3))       # 27
# result = higher_order_function('absolute')
# print(result(-3))      # 3

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
# that allows a user to add new functionality to an 
# existing object without modifying its structure

# Built in function 
# map(), filter(), reduce()

# Map 
# This function take function and iteration 
# map(function,iterable) 

# number=[1,2,3,4,5]
# def square(x):
#     return x**2

# num = map(square, number)
# print(list(num))

# using lambda function
# numbers = [1,2,3,4,5] 
# number = map(lambda x : x**2,numbers)
# print(list(number))

# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

# def change_to_upper(name):
#     return name.upper()

# names_upper_cased = map(change_to_upper, names)
# print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
# names_upper_cased = map(lambda name: name.upper(), names)
# print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# filter call the boolean value result
#filter(function, iterable)

# numbers = [1, 2, 3, 4, 5]  # iterable

# def is_odd(num):
#     if num % 2 != 0:
#         return True
#     return False

# odd_numbers = filter(is_odd, numbers)
# print(list(odd_numbers))       # [1, 3, 5]

# Filter long name
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
# def is_name_long(name):
#     if len(name) > 7:
#         return True
#     return False

# long_names = filter(is_name_long, names)
# print(list(long_names))         # ['Asabeneh']

# Reduce() it does not return another iterable, instead it returns a single value.
# reduce(function,iteration)

# numbers_str = ['1', '2', '3', '4', '5']  # iterable
# def add_two_nums(x, y):
#     return int(x) + int(y)

# total = reduce(add_two_nums, numbers_str)
# print(total)    # 15

# Question 
