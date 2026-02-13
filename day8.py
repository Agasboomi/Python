# Dictionaries is collection of unordered  and mutable , paired (key:value)
# empty = {}
# print(len(empty))

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# print(person['first_name']) #key:value acces by key name
# print(person['country'])

# # Adding in dict
# person['sex'] = 'M'
# person['skills'].append('HTML') # adding in the particular list
# print(person)
# # In the above column it contain many variable eg:list, set, tuple etc

# # Modify
# person['first_name']='Agas'
# print(person['first_name'])

# # Check
# print('age'in person)
# print('command'in person)

# # remove
# # pop(key): removes the item with the specified key name:
# # popitem(): removes the last item
# # del: removes an item with specified key name
# person.pop('first_name')
# # print(person)
# # person.popitem()
# # print(person)

# # # Change dict to list The items() method changes dictionary to a list of tuples.
# # print(person.items())

# # clear
# # print(person.clear())

# # delete
# # del person  #delete completly
# # print(person)

# #copy
# # dict1 = {"a": 1, "b": 2}

# # dict2 = dict1          # just assignment
# # dict3 = dict1.copy()   # actual copy

# # dict2["a"] = 99
# # dict3["b"] = 100

# # print(dict1)  # {'a': 99, 'b': 2} → changed because dict2 points to same object
# # print(dict2)  # {'a': 99, 'b': 2}
# # print(dict3)  # {'a': 1, 'b': 100} → independent copy

# # taking only a key and value
# key=person.keys()
# ke = person.values()
# print(ke)
# print(key)

# question
# dog = {}
# print(len(dog))

# dog = dict(
#     name='agas',
#     color='red',
#     bread='wheat',
#     legs='right',
#     age=24
# )

# print(dog)

student = dict(
    first_name = 'agas',
    last_name = 'boom',
    gender = 'M',
    martial = 'single',
    skill = ['coding',"no","yes"],
    country= 'India',
    address = 'DVK'
)

# print(student)

# print(len(student))

# skills =student['skill']
# print(type(skills))


# student['skill']= ['play','come','walk']
# print(student)

# key = student.keys()
# value = student.values()
# print(key)
# print(value)

# print(student.items())

del student['skill']
print(student)

del student
print(student)