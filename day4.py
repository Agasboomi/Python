# Text is a string data type. Any data type written as text is a string. 
# create string
# sentence = "agas"
# print(sentence)


# Concatination
# Pra = """Hi I am agas 
# I am from India"""
# print(Pra)

# Escape sequence
# first = "Agas"
# last =  "thees"
# full = first + " "+ last
# print(full)


# print('I hope everyone is enjoying the Python Challenge.\nAre you ?')
# print('No\tday\ttime' )
# print('1\t2\t13:00')

# first_name = 'Asabeneh'    #old method
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# first_name = 'Asabeneh' #new method
# last_name = 'Yetayeh'
# language = 'Python'
# # formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
# formated_string =(f"i am {first_name}{last_name}, I teach {language}")
# print(formated_string)

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# # formated_string = 'The area of circle with a radius {} is {:.2f}.'.format(radius, area)
# formated_string = (f"the are of circle radius {radius} is {area}")
# print(formated_string)

# Unpacking character/
# Name = "karlas"
# a,b,c,d,e,f = Name
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# Index
# language = "Python"
# print(language[1])
# print(len(language) -1 )

# language = "javala"
# last = len(language) - 1     #6 -1 = 5
# last_letter = language[last] #index 5
# print(last_letter)

# Slicing
# first = "agas"
# print(first[0:3], first[-3:]) #it start from 0 index but nat include 3

# Reverse a string easy method
# rev = "Logesk"
# print(rev[::-1])/

# Skipping slicing
# language = 'Python'
# pto = language[0:4:2] #[start:stop:step]
# print(pto) 

# STRING METHODS
# letter = "agas"
# print(letter.capitalize())
# print(letter.count('a'))
# print(letter.endswith('as')) # T Or F
# print(letter.find('a'))
# # Replace
# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding')) # 'thirty days of coding'
# print(challenge.split())

# letter= "agas\tthee"
# print(letter.expandtabs())


# Question
# print("Thirty"+"Days"+"Of"+"Pyhton")
# Company ="Coding"+" "+"for"+" "+"All"
# print(Company)
# print(len(Company))

# print(Company.upper())
# print(Company.lower())
# print(Company.capitalize()) #
# print(Company.title()) #Make the first letter in each word upper case
# print(Company.swapcase()) # Make the lower case letters upper case and the upper case letters lower case
# print(" ".join(Company.split()[1:]))
# print(Company.find("Coding"))
# print(Company.replace("Coding","Python"))
# print(Company.replace("All", "Python for Everyone"))
# print(Company.split(" "))
# print(Company[0])
# print(Company[-1])
# print(Company[10])
# print(Company.index("C"))
# print(Company.index("C"))
# print(Company.index("l"))

# text = "Python For Everyone"
# words = text.split()
# acronym = "".join([w[0].upper() for w in words])
# print(acronym)   # Output: PFE

# text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# result = text.split(",")
# print(result)

# text = "Coding For All"
# result = text.startswith("Coding")
# # print(result)  # Output: True

# Com = " coding for all "
# print(Com.strip())

# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True

# challenge = 'thirty days of python'
# print(challenge.islower()) # True
# challenge = 'Thirty days of python'
# print(challenge.islower()) # False

# challenge = 'thirty days of python'
# print(challenge.isupper()) #  False
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper()) # True

# Lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# print(" ".join(Lib))


# List = "I am enjoying this challenge.\nI just wonder what is next."
# print(List)

# 34,35 karthika




fruite = ['mango','orange','apple','agas','arun']
n = len(fruite)
if n%2 ==1:
    mediun = fruite[(n//2)] #2
else:
    mediun = fruite[(n//2)-1:(n//2)+1]#
print(mediun)