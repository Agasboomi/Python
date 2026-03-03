# OOPS concept is used to organized the code and security propose 
# class - class is the blue print of the abject 
#         _init_ to create a new object
#         self to initiate a current object 

# object - instance of the class 

# creating class 
# class classname:
#     code goes here

# class person:
#     pass
# print(person)

# # creating object 
# p = person()
# print(p)

# class constructor
# In Python, a constructor is a special method __init__() that automatically runs when an object of a class is created.
# __init__ & self 

# class Person:
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country

# p= Person("Agas","India")
# print(p.name)
# print(p.country)
# # print(p)

# object methods 
# Objects can have methods. The methods are functions which belong to the object.

# class Person:
#       def __init__(self, firstname, lastname, age, country, city):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city
#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

# p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
# print(p.person_info())

# object default methods 
# class Person:
#       def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city

#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

# p1 = Person()
# print(p1.person_info())
# p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
# print(p2.person_info())

# # Method to Modify Class Default Values
# class Person:
#       def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city
#           self.skills = []

#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
#       def add_skill(self, skill):
#           self.skills.append(skill)

# # p1 = Person()
# # print(p1.person_info())
# # p1.add_skill('HTML')
# # p1.add_skill('CSS')
# # p1.add_skill('JavaScript')
# # p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
# # print(p2.person_info())
# # print(p1.skills)
# # print(p2.skills)

# # Inhertiance 
# class Student(Person):
#     pass


# s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
# s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)

# # overriding parent method
# class Student(Person):
#     def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
#         self.gender = gender
#         super().__init__(firstname, lastname,age, country, city)
#     def person_info(self):
#         gender = 'He' if self.gender =='male' else 'She'
#         return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

# s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
# s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)

# Question
# class Statistics:
#     def __init__(self,ages,ages1):
#         self.ages = ages
#         self.ages = ages1
#         self.add = ages1 + ages

# data = Statistics(2,2)
# print(data.add)

# class Statistics:
#     def __init__(self,count):
#         self.count = count.count()

# data = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
# print('Count:', data.count)


class personaccount:
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

info = personaccount("agas","boominathan")
print(info.firstname)
print(info.lastname)