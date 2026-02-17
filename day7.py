# set is Set is a collection of unordered and un-indexed distinct elements.
# we declare in flower bracket{}

# syntax
# st = set()
# print(len(st))

# syntax
# fruits = {'banana', 'orange', 'mango', 'lemon'}

# length of the set 
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# len(fruits)

# Check
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# print('mango' in fruits ) # True

# Add
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.add('lime')

# Multiple set added using update
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
# fruits.update(vegetables)

# Remove/pop 
# syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove('item2')
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.pop()  # removes a random item from the set

# clear()
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.clear()
# print(fruits) # set()

# delete 
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# del fruits

# syntax change to list to set
# lst = ['item1', 'item2', 'item3', 'item4', 'item1']
# st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

# Joining the set by using union 
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot',"lemon"}
# print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# # or using this : print(fruits | vegetables)

# Update 
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# fruits.update(vegetables)
# print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# intersection
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# inte = whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
# print(inte)

# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# st2.issubset(st1) # True
# st1.issuperset(st2) # True

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8}
# print(even_numbers.issubset(whole_numbers)) # False, because it is a super set
# whole_numbers.issuperset(even_numbers) # True

# differnt between the set
# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# print(python.isdisjoint(dragon) )# False, there are common items {'o', 'n'}

# Symmetric Difference Between Two Sets
# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# # it means (A\B)∪(B\A)
# print(st2.symmetric_difference(st1)) # {'item1', 'item4'} : st2 ^ st1

# Question
# It_company = set()
# print(len(It_company))

# It_company.add("Twitter")
# print(It_company)

# mul = {"IBM","AGAS","Kar"}
# It_company.update(mul)
# print(It_company)

# # It_company.remove("IBM")
# # print(It_company)

# It_company.discard("IBM")
# print(It_company)

# del It_company

# ages = [2,34,67,2,56,90]
# st = set(ages)
# print(len(st))
# print(len(ages))

# sen = "I am a teacher and I love to inspire and teach people."
# sp =set( sen.split())
# print(sp)

