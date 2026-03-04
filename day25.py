# Pandas 
# Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language

# Pandas provides tools for data manipulation:
# reshaping
# merging
# sorting
# slicing
# aggregation
# imputation. If you are using anaconda, you do not have install pandas.  

# Panda series
import pandas as pd
import numpy as np

# num = [1,2,3,4,5]
# s = pd.Series(num)
# print(s)

# custome index
# num = [1,2,3,4,5]
# s = pd.Series(num, index=[1,2,3,4,5])
# print(s)

# fruits = ['Orange','Banana','Mango']
# fruits = pd.Series(fruits, index=[1, 2, 3])
# print(fruits)

# Dict 
# dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}

# s = pd.Series(dct)
# print(s)

# linespace (start,stop,iteam)
# s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
# print(s)

# Dataframes list of list
# data = [
#     ['Asabeneh', 'Finland', 'Helsink'],
#     ['David', 'UK', 'London'],
#     ['John', 'Sweden', 'Stockholm']
# ]
# df = pd.DataFrame(data, columns=['Names','Country','City'])
# print(df)

# Dataframe in dict 
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# head()
# print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

# tail()
# print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method

# shape()
# print(df.shape) # as you can see 10000 rows and three columns

# describe()
# print(heights.describe()) # give statistical information about height data 

