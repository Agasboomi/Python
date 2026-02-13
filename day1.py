# Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, object-oriented programming language
# Why Python ?
# It is a programming language which is very close to human language and because of that, it is easy to learn and use. Python is used by various industries and companies (including Google). 
# It has been used to develop web applications, desktop applications, system administration, and machine learning libraries. Python is a highly embraced language in the data science and machine learning community. 



# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# Question
print(3+1)
print(3-1)
print(3*1)
print(3%1)
print(3/1)
print(3**1)
print(3//1)

print("your name")
print("your family name")
print("your country")
print("I am enjoying 30days of python")


print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['agas','python',24]))
print(type('name'))

import math # with import
x1, y1 =2,3
x2,y2 = 10,8
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(d)


#without import
x1, y1 = 2, 3
x2, y2 = 10, 8
d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(d)