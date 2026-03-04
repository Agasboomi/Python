# A regular expression or RegEx is a special text
# string that helps to find patterns in data. #
# A RegEx can be used to check if some pattern exists in a different data type
# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

# syntax
# import re 
# re.match(substring, string, re.I)
# re.search(substring, string, re.I) 

# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore

import re

# # Match 
# txt = 'I love to teach python and javaScript'
# match = re.match('I love to teach', txt, re.I)
# print(match)  # None

# search
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
# # It returns an object with span and match
# match = re.search('first', txt, re.I)
# print(match) 

# findall() 
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
# # It return a list
# matches = re.findall('language', txt, re.I)
# print(matches)  # ['language', 'language']

# Random 
# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
# match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)

# sub
# txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
# T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
# D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
# matches = re.sub('%', '', txt)
# print(matches)

# square
# regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
# Escape character(\) in RegEx
# regex_pattern = r'\d'  # d is a special character which means digits
# One or more times(+)
# regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
# Period(.)
# regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
# Zero or many times. The pattern could may not occur or it can occur many times.
# regex_pattern = r'[a].*'  # . any character, * any character zero or more times
# Zero or one time(?)
# txt = '''I am not sure if there is a convention how to write the word e-mail.
# Some people write it as email others may write it as Email or E-mail.'''
# regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
# Quantifier in RegEx
# txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# regex_pattern = r'\d{4}'  # exactly four times
# Cart ^
# txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# regex_pattern = r'^This'  # ^ means starts with
# matches = re.findall(regex_pattern, txt)