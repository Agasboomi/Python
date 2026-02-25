# File handling 
# File handling is an import part of programming
# which allows us to create, read, update and delete files. 
# In Python to handle data we use open() built-in function

# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Read 
# f = open('./files/reading_file_example.txt')
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()

# # output
# <class 'str'>
# This is an example to show how to open a file and read.
# This is the second line of the text.

# another method 
# with open(file_path)as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)

or
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')