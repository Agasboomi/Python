# # A tuple is a collection of different data types which is ordered and unchangeable (immutable)
# #  Tuples are written with round brackets, ()

# # syntax
# empty_tuple = ()
# # or using the tuple constructor
# empty_tuple = tuple()

# fruits = ('banana', 'orange', 'mango', 'lemon')

# fruits = ('banana', 'orange', 'mango', 'lemon')
# first_fruit = fruits[0]
# second_fruit = fruits[1]
# last =len(fruits) - 1
# last_fruit = fruits[last]

# # Index 
# fruits = ('banana', 'orange', 'mango', 'lemon')
# first_fruit = fruits[-4]
# second_fruit = fruits[-3]
# last_fruit = fruits[-1]

# # Slicing
# fruits = ('banana', 'orange', 'mango', 'lemon')
# all_fruits = fruits[0:4]    # all items
# all_fruits= fruits[0:]      # all items
# orange_mango = fruits[1:3]  # doesn't include item at index 3
# orange_to_the_rest = fruits[1:]

# # Tuple to List 
# fruits = ('banana', 'orange', 'mango', 'lemon')
# fruits = list(fruits)
# fruits[0] = 'apple'
# print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
# fruits = tuple(fruits)
# print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# # checking the item
# fruits = ('banana', 'orange', 'mango', 'lemon')
# print('orange' in fruits) # True
# print('apple' in fruits) # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# # Join
# fruits = ('banana', 'orange', 'mango', 'lemon')
# vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)

# # delete the tuple 
# fruits = ('banana', 'orange', 'mango', 'lemon')
# del fruits

# Question
# empty = ()
# print(len(empty))

brother = ('agas','arun','nisha')
sister = ('karthi','anu','Sweety')
sister_brother = brother + sister
print(sister_brother)

print(len(sister_brother))

Par = ("navaneethi","Boomadevi")
family = sister_brother + Par
print(family)

a,b,c,d,e,f,g,h = family
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

# 2,3 homework
# 4,5 doubt