# If condition is to check the statement using operator

# a=3
# if a > 7:
#     print("a is bigger")
# else:
#     print("a is small")

# b=3
# if b == 0:
#     print("equal")
# elif(b>2):
#     print("greater")
# else:
#     print("none") 

# # Nested condition
# a = 2
# if a > 0:
#     if a % 2 == 0:
#         print('A is a positive and even integer')
#     else:
#         print('A is a positive number')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is a negative number')

# if with logical operator
# a = 3
# if a > 0 and a % 2 == 0:
#         print('A is an even and positive integer')
# elif a > 0 and a % 2 !=  0:
#      print('A is a positive integer')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is negative')


# Or operator
# user = 'James'
# access_level = 4
# if user == 'admin' or access_level >= 4:
#         print('Access granted!')
# else:
#     print('Access denied!')


# Queation
# Age = int(input("Enter your ages"))
# if Age >= 18:
#       print("drive")
# else:
#       print("Not allowed")
      

# my_age = int(input("enter your age :"))
# your_age = int(input("enter your age :"))

# if my_age>your_age:
#     diff = my_age - your_age
#     if diff == 1:
#         print("my age is greater then one ")
#     else:
#         print(f"My age is greater than {diff} yours ")
# elif  your_age>my_age:
#     diff =your_age - my_age
#     if diff == 1:
#         print("your age is greater then one ")
#     else:
#         print(f"your age is greater than {diff}")
# else:
#      print("both ages are same")


# a = int(input("enter number"))
# b = int(input("enter number"))
# if a>b:
#    print(f"{a} greater than {b}")
# elif b>a:
#     print(f"{b} is grater then {a}")
# else:
#     print(f"{a} is equal {b}") 

# User = input("Enter the season :")
# if (User == "Sep" or User == "Oct" or User == "Nov"):
#     print("Autum")
# elif (User == "Dec" or User == "Jan" or User == "Feb"):
#     print("Winter")
# elif (User == "Mar" or User == "Apr" or User == "May"):
#     print("Spring")
# if (User == "Jun" or User == "Jul" or User == "Aug"):
#     print("Sum")
# else:
#     print("Enter Correct Season")

# # other Method
# month = input("Enter the month: ").strip().capitalize()

# # Check the season
# if month in ["September", "October", "November"]:
#     season = "Autumn"
# elif month in ["December", "January", "February"]:
#     season = "Winter"
# elif month in ["March", "April", "May"]:
#     season = "Spring"
# elif month in ["June", "July", "August"]:
#     season = "Summer"
# else:
#     season = "Invalid month"

# print(f"The season is {season}.")

# fruits = ['banana', 'orange', 'mango', 'lemon']

# fruit = input("Enter a fruit :").strip().lower()
# if fruit in fruits:
#     print("All are there")
# else:
#     fruits.append(fruit)
#     print("Added",fruits)

# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }

# if 'skills' in person:
#     print("Yes")
# else:
#     print("No")

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if person has 'skills' key and print middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

    # 2. Check if person has 'Python' skill
    if 'Python' in skills:
        print("Person has Python skill")
    else:
        print("Person does not have Python skill")

    # 3. Determine developer type
    if skills == ['JavaScript', 'React']:
        print("He is a front end developer")
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print("He is a backend developer")
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# 4. If married and lives in Finland, print formatted info
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. "
          f"He is married.")