# Modulas
# - Definition: A module is a .py file with reusable code.
# - Contents: It can include functions, classes, and variables.
# - Purpose: Helps break large programs into smaller, manageable pieces.
# - Importing: You use the import keyword to bring a module into another script.

# calc.py
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# another file 
# import calc

# print(calc.add(5, 3))       # Output: 8
# print(calc.subtract(10, 4)) # Output: 6

# import math
# print(math.pi)           # 3.141592653589793, pi constant
# print(math.sqrt(2))      # 1.4142135623730951, square root
# print(math.pow(2, 3))    # 8.0, exponential function
# print(math.floor(9.81))  # 9, rounding to the lowest
# print(math.ceil(9.81))   # 10, rounding to the highest
# print(math.log10(100))   # 2, logarithm with 10 as base


# import string
# print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)        # 0123456789
# print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# checking random number 
# from random import random, randint
# print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
# print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

# Question
# from random import random, randint
# print(randint(0,10)) 