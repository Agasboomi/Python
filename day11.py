# Function task. To define or declare a function, Python provides the def keyword.
# The function block of code is executed only if the function is called or invoked.

# declare a funtion without a parameter
# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     print(total)
# add_two_numbers()

# def Name():
#     first_name = "Agas"
#     Second_name = "karthi"
#     full = first_name + Second_name
#     print(full)
# Name()

# # Function with parameter
# # the return keyword is used inside a function to send a value back to the place where the function was called. 
# # Without return, a function will finish running but won’t give anything back (it will default to returning None).


# def add (num):
#     ten = 10
#     return(num+ten)
# print(add(10))

# # with two argument 
# def mult(first,second):
#     here = first * second
#     return here
# print(mult(10,20))

# def generate_full_name (first_name, last_name):
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

# Passing Arguments with Key and Value
# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(num2 = 3, num1 = 2))

# Function Returning a Value is none
# def print_name(firstname):
#     return firstname
# print_name('Asabeneh') # Asabeneh
 
# Retrun string
# def print_full_name(firstname, lastname):
#     space = ' '
#     full = firstname  + space + lastname
#     return full
# print(print_full_name(firstname='Asabeneh', lastname='Yetayeh'))

# Return num
# def add_two_numbers (num1, num2):
#     total = num1 + num2
#     return total
# print(add_two_numbers(2, 3))

# Return Boolean
# def is_even (n):
#     if n % 2 == 0:
#         return True    # return stops further execution of the function, similar to break 
#     return False
# print(is_even(10)) # True
# print(is_even(7)) # False

# Return list
# def numb(n):
#     even=[]
#     for i in range (n+1):
#        if  i%2 == 0:
#            even.append(i)
#            i=i+1
#     return even
# print(numb(10))
    
# Function with Default Parameters    
# def calculate_age (birth_year,current_year = 2021):
#     age = current_year - birth_year
#     return age 
# print('Age: ', calculate_age(1821))

# Arbitrary Number of Arguments
# def sum_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total += num     # same as total = total + num 
#     return total
# print(sum_all_nums(2, 3, 5)) # 10

# def generate_groups (team,*args):
#     print(team)
#     for i in args:
#         print(i) 
# generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

# print in horixanal
# def generate_groups(team, *args):
#     print(team)
#     print(" ".join(args))

# generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob')


# def greet(name, location):
#     # Print a greeting message using the provided arguments
#     print("Hi there", name, "how is the weather in", location)
# my_dict = {"name": "Alice", "location": "New York"}

# # Call the function using dictionary unpacking
# greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York


#You can pass functions around as parameters
# def square_number (n):
#     return n ** n
# def do_something(f, x):
#     return f(x)
# print(do_something(square_number, 3)) # 9

# question
# def add_two_number(one,two):
#     sum = one+two
#     return sum
# print(add_two_number(2,3))

# def area (pi,r):
#     result = pi*r*r
#     return result
# print(area(3.14,2))

# def check_season(month):
#     month = month.strip().capitalize()
#     if month in ["March","April","May"]:
#         print("Spring")
#     elif month in ["June","July","August"]:
#         print("Summer")
#     elif month in ["September","October","November"]:
#         print("Autumn")
#     else:
#         print("Winter")

# season = input("Enter the month")
# check_season(season)

# Checking temp
# def convert_celsius_to_fahrenheit(celsius):
#     """
#     Convert temperature from Celsius to Fahrenheit.
    
#     Formula: °F = (°C × 9/5) + 32
#     """
#     if isinstance(celsius, (int, float)):
#         fahrenheit = (celsius * 9/5) + 32
#         return fahrenheit
#     else:
#         return "Error: Please provide a numeric value for Celsius temperature."

# # Example usage
# print(convert_celsius_to_fahrenheit(0))     # Output: 32.0
# print(convert_celsius_to_fahrenheit(37))    # Output: 98.6
# print(convert_celsius_to_fahrenheit("abc")) # Output: Error message

# Print each element
# def print_list(items):
#     """
#     Prints each element of the list on a new line.
    
#     Parameters:
#         items (list): The list whose elements will be printed
#     """
#     if isinstance(items, list):
#         for element in items:
#             print(element)
#     else:
#         print("Error: Please provide a list as input.")


# def reverse_list(lst):
#     reverse = []
#     for i in range (len(lst)-1,-1,-1):
#         reverse.append(lst[i])
#     return reverse
# print(reverse_list([1,2,3]))

# def capitalize_list(cap):
#     capt= []
#     for i in range (len(cap)):
#         capt.append(cap[i].capitalize())
#     return capt
# print(capitalize_list(["ahajfs","karthika"]))


# adding iteam at the end
# def add_item(iteams,iteam):
#     iteams.append(iteam)
#     return iteams
# iteams = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(iteams,"Meat"))

# Remove iteam in the function
# def remove_iteam(iteam,rem):
#     if rem in iteam:
#        iteam.remove(rem)
#     return iteam
# iteam = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_iteam(iteam,"Mango")) 

# sum of [present numbers]
# def sum_of_numbers(n):
#     sum=0
#     for i in range(n+1):
#         sum = sum+i
#     return sum
# print(sum_of_numbers(100))

# sum of odd numbers
# def sum_of_numbers(n):
#     sum=0
#     for i in range(n+1):
#         if i%2 == 1:
#             sum = sum+i
#     return sum
# print(sum_of_numbers(10))

# sum of even numbers
# def sum_of_numbers(n):
#     sum=0
#     for i in range(n+1):
#         if i%2 == 0:
#             sum = sum+i
#     return sum
# print(sum_of_numbers(10))

# count the value of odd and even 
# def even_and_odds(num):
#     even = 0
#     odd = 0
#     for i in range (num+1):
#         if i%2 == 0:
#             even=even+1
#         else:
#             odd = odd+1
#     return f"{even} & {odd}"
# print(even_and_odds(100))

# def greet(name="guest"):
#         return(f"hello,{name}")
# print(greet())


# check the value is empty or not 
# def is_empty(value):
#     if not value:
#         return("Empty")
#     else:
#         return(f"Not Empty the value is {value}")
# print(is_empty("agas"))

# def show_args(name,age,city):
#     return(f"name: {name}, age:{age}, city{city}")
# print(show_args(name="Alice", age=30, city="New York"))

# Factorial
# n=4
# fact = 1
# for i in range (1,n+1):
#     fact=fact*i
#     i+1
# print(fact)

# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact*i 
#         i= i+1
#     return fact

# numb = int(input("enter the number :"))
# print(factorial(numb))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# Example usage
# n = 20
# if is_prime(n):
#     print("Prime number")
# else:
#     print("Not a prime number")


# def che(name):
#     if len(name) == len(set(name)):
#         return "unique"
#     else:
#         return "Not"

# print(che(["agas","arun","agas"]))  # Output: Not

# Check same data type or not 
def che(name):
    one_index = type(name[0])
    for i in name:
        if type(i) != one_index:
            return " Not Same"
    return "Same"
print(che(["agas","arun","agas"]))  

import keyword

def is_valid_variable(var_name):
    if not isinstance(var_name, str):
        return "Not a string"
    if var_name.isidentifier() and not keyword.iskeyword(var_name):
        return "Valid Python variable"
    else:
        return "Invalid Python variable"

# Tests
print(is_valid_variable("my_var"))   # Valid
print(is_valid_variable("2ndVar"))   # Invalid
print(is_valid_variable("var-name")) # Invalid
print(is_valid_variable("_hidden"))  # Valid
print(is_valid_variable("class"))    # Invalid (keyword)