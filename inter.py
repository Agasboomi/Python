# decorative

# def sume(fun):
#     def wrapper():
#         print("korng")
#         c= fun()
#         print("kog")
#         return c
#     return wrapper
# @sume
# def res():
#     print("This is the total")

# res()

# map()
# num = [1,2,3]
# def addi(x):
#     return x*x

# valu = list(map(addi,num))
# print(valu)

# filter
# n = [1,2,3,4]
# def eve(x):
#     if x%2 == 0:
#         return True
#     return False

# v = list(filter(eve,n))
# print(v)

# Reduce
# from functools import reduce
# a = [1,2]
# def add(x,y):
#     z = x+y
#     return z

# v = reduce(add,a)
# print(v)

# function 
# def add(n1,n2):
#     a = n1
#     b = n2
#     c = a+b
#     return c

# print(add(n2=2,n1=3))

# closure
# def outer():
#     number = []
#     def inner(x):
#         number.append(x)
#         print(number)
#     return inner

# num = outer()
# num(3)
# num(4)

# class & object
# class agas:
#     def __init__(self,name,ages):
#         self.name = name
#         self.ages = ages
#     def call(self):
#         print(f"{self.name} and {self.ages}")
    
# ans = agas("agas",2)
# ans.call()

# generator 
# def agas():
#     for i in range(n):
#         yield i
# n = 5
# for var in agas():
#     print(var)
 
    