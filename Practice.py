# odd or even 
# n = int(input("Enter your number : "))
# if n%2 == 0:
#     print("It is even")
# else:
#     print("It is odd")

# function
# def num(n1):
#     if n1%2 == 0:
#         return("It's even")
#     return ("It's odd")
# print(num(7))

# List of compercation 
# n1 = [3,4,5,6,6,7,8] # we can late eilther range or in list
# num = [i for i in n1 if i%2 == 0]
# print(num)

# factorial 
# fact = 1 
# for i in range (1,6):
#     fact = i*fact
# print(fact)

# function 
# def factorial(num):
#     Fact = 1
#     for i in range(1,num+1):
#         Fact = Fact*i
#     return Fact
# print(factorial(5))

# list of compercation doesn't work in factorial

# import math 
# print(math.factorial(5))

# Prime number
# num = 2
# if num%2 == 0:
#     print("not a prime")
# else:
#     print("prime")

# function 
# return is used to store a value in function and it reuse
# print is used to display the value in terminal

# def check(num):
#     if num%2 == 0:
#         return("It's not a prime")
#     return("It's a prime")
# print(check(2))

# list of compecation
# nums = [2, 3, 4, 5]
# check = ["Not prime" if n % 2 == 0  else "Prime" for n in nums]
# print(check)

# Fibinocies 
# 011235813
# a =0
# b =1
# print(a)
# print(b)
# for i in range(6):
#     fab = a + b
#     a=b
#     b=fab
#     print(fab)

# function 
# def fib(n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a+b
#         a = b
#         b = c
#         print(c)

# fib(5)


# leap year
y = 1600
if (y%4 ==0 and y%100 != 100) and y%400 == 0:
    print("Leap year")
else:
    print("Not a leap year")