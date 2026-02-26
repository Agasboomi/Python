# Exception Handling 
# python uses try and except o handle error gracefully 
# An example of exceptions could be an incorrect input, 
# wrong file name, unable to find a file, a malfunctioning IO device.

# try:
#     print(2+"9")
# except:
#     print("something wrong in this code") 

# try:
#     name = input("enter your name")
#     age = input("enter your Age")
#     age = 2019 + age
#     print(f"{name} & {age}")
# except:
#     print("Error")

# show the exact error 
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')

# Even thought error occurs its runs 
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')

# or shorten 
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as a:
#     print(a)

# unpacking list buy two methods(*for tuple & **for dic)
# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# # print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# print(sum_of_five_nums(*lst))  # 15

# numbers = range(2, 7)  # normal call with separate arguments
# print(list(numbers)) # [2, 3, 4, 5, 6]
# args = [2, 7]
# numbers = range(*args)  # call with arguments unpacked from a list
# print(numbers)      # [2, 3, 4, 5,6]

# Packing
# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum_all(1, 2, 3))             # 6
# print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# spreading 
# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
# country_lst_one = ['Finland', 'Sweden', 'Norway']
# country_lst_two = ['Denmark', 'Iceland']
# nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# enumerate use enumerate built-in function to get the index of each item in the list
for index, item in enumerate([20, 30, 40]):
    print(index, item)

# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# for index, i in enumerate(countries):
#     if i == 'Finland':
#         print(f'The country {i} has been found at index {index}')

# # Zip combine lists when looping through them
# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# fruits_and_veges = []
# for f, v in zip(fruits, vegetables):
#     fruits_and_veges.append({'fruit':f, 'veg':v})

# print(fruits_and_veges)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_coutntries, es, ru = names
print(nordic_coutntries)
print(es)
print(ru)
