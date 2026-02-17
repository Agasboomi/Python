# list comperhension 
# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. 

# changing string to list in 2 methods 
# One way
# language = 'Python'
# lst = list(language) # changing the string to list
# print(type(lst))     # list
# print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
# language = "Agastheeswaran"
# lst = [i for i in language]
# print(type(lst)) # list
# print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']


# # Generating numbers
# numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
# print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # It is possible to do mathematical operations during iteration
# squares = [i * i for i in range(11)]
# print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
# numbers = [(i, i) for i in range(11)]
# print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# List comprehension can be combined with if expression
# Generating even numbers
# even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
# print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# # Generating odd numbers
# odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
# print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# # Filter numbers: let's filter out positive even numbers from the list below
# numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
# positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
# print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# # Flattening a two dimensional array
# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened_list = [ number for row in list_of_lists for number in row]
# print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lamda function 
# Lambda function is a small anonymous function without a name. 
# It can take any number of arguments, but can only have one expression.
#To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression.

# arg = lambda a,b: a+b
# print(arg(2,3))

# simple way
# print((lambda a, b: a + b)(2,3))

# Square = lambda a: a**2
# print(Square(5))

# Cube = lambda a: a**3
# print(Cube(5))

# Multiple variables
# multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
# print(multiple_variable(5, 5, 3)) # 22

# def power(x):
#     print(x)
#     return lambda n : x ** n

# cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
# print(cube)          # 8
# two_power_of_five = power(2)(5) 
# print(two_power_of_five)  # 32

# question 
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# neg = [i for i in numbers if i>0]
# print(neg)

# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# num = [numbers for row in list_of_lists for numbers in row]
# print(num)

# it works like this
# num = []
# for row in list_of_lists:       # outer loop
#     for numbers in row:         # inner loop
#         num.append(numbers)

# Tuple Using list comprehension create the following list of tuples: 
# num =[(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
# print(num)

# countries = [
#     [('Finland', 'Helsinki')],
#     [('Sweden', 'Stockholm')],
#     [('Norway', 'Oslo')]
# ]

# output = [
#     [country.upper(), country[:3].upper(), capital.upper()]
#     for row in countries
#     for (country, capital) in row
# ]

# print(output)


# output = [
#     {'country': country.upper(), 'city': capital.upper()}
#     for row in countries
#     for (country, capital) in row
# ]

# print(output)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
out = [f"{first} {last}" for row in names for (first, last) in row]
print(out)
