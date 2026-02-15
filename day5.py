# A list is collection of different data types which is ordered and modifiable(mutable) 
# It is square

# lsst = list()
# print(len(lsst))

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# print(fruits)
# print(len(fruits))

# Last index
# last_index = len(fruits) - 1 #3
# last_fruit = fruits[last_index]

# unpacking
# a,b,*c = fruits
# print(a)
# print(b)
# print(c)

# Slicing 
# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[0:3] 
# all_fruits = fruits[-4:] 
# print(all_fruits)

# check 
# check = 'mango' in fruits
# print(check)


# Adding 
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.append('apple')
# print(fruits) 

# # inserting item into the list
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.insert(2, 'apple')
# print(fruits)

# Remove item in the list
# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
# fruits.remove('banana')
# print(fruits)

# # POP() Remove list in the python
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop()
# print(fruits) 

# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[0] # use to delete particular item 
# print(fruits) 
# del fruits # use to delete whole list
# print(fruits) 

# # clear is to empty the list
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.clear()
# print(fruits)       # []

# # Copy
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits_copy = fruits.copy()
# print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# Join
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables )

# # Extend
# num1 = [0, 1, 2, 3]
# num2= [4, 5, 6]
# num1.extend(num2)
# print('Numbers:', num1)

# # Count
# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.count('orange'))   # 1
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.count(24))           # 3

# #  Reverse the string
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.reverse()
# print(ages)

# # Sorted 
# # syntax
# lst = ['item1', 'item2']
# lst.sort()                # ascending
# lst.sort(reverse=True)    # descending
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.sort(reverse=True)
# print(ages) 

# Question:
Name = []
print(len(Name))

Name = ['agas','kar','uma','nisha','ajay','arun']
# print(len(Name))

# num = len(Name)
# if num%2 == 0:

# 4,9,19

mixed_data_type = ["agas","16","4inch","single but ready to mingle","Kovial"]

it_company = ['amazon','google','facebook','apple']

# print(it_company)
# print(len(it_company))

# it_company.append('oracle')
# print(it_company)

# it_company.insert(2,'karlashe')
# print(it_company)

# print("#; ".join(it_company))

# print('apple' in it_company)

# it_company.sort()
# print(it_company)

# it_company.sort(reverse=True)
# print(it_company)

# print(it_company[0:3])

# print(it_company[-3:])

# 20,22

# it_company.remove("amazon")
# print(it_company)

# result = it_company[:3]
# print(result)

# it_company.clear()
# print(it_company)

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# jo=front_end +back_end
# print(jo)

# full_stack = jo.copy()
# print(full_stack)

# # find index
# red= full_stack.index('Redux')
# print(red)  #4

# full_stack.insert(red+1 ,"python")
# full_stack.insert(red+2 ,"sql")
# print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
max=ages[-1]
re = min + max
print(re)

