# python package manager 
# PIP = Preferred installer package 
# Package is a Python module that can contain one or more modules or other packages.
# numpy- Let us try to install numpy, called numeric python. It is one of the most 
# popular packages in machine learning and data science community.

# NUMPY
# terminal 
# asabeneh@Asabeneh:~$ pip install numpy

# # shell 
# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import numpy
# >>> numpy.version.version
# '1.20.1'
# >>> lst = [1, 2, 3,4, 5]
# >>> np_arr = numpy.array(lst)
# >>> np_arr
# array([1, 2, 3, 4, 5])
# >>> len(np_arr)
# 5
# >>> np_arr * 2
# array([ 2,  4,  6,  8, 10])
# >>> np_arr  + 2
# array([3, 4, 5, 6, 7])
# >>>

# PANDAS
# Terminal 
# pip install pandas

# shell
# >>> import pandas


# WEB BROWER
# Let us import a web browser module, which can help us to open any website. We do not need to install this module, it is already installed by default with Python 3.


# import webbrowser # web browser module to open websites

# # list of urls: python
# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]

# # opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

# uninstalled 
# pip uninstall packagename 

# list of package 
# pip list

# show package 
# pip show packagename 
# If we want even more details, just add --verbose
# pip show --verbose pandas

# Further Information About Packages
# Database

# SQLAlchemy or SQLObject - Object oriented access to several different database systems
# pip install SQLAlchemy
# Web Development

# Django - High-level web framework.
# pip install django
# Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
# pip install flask
# HTML Parser

# Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
# pip install beautifulsoup4
# PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.
# XML Processing

# ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
# GUI

# PyQt - Bindings for the cross-platform Qt framework.
# TkInter - The traditional Python user interface toolkit.
# Data Analysis, Data Science and Machine learning

# Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
# Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
# SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
# Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
# TensorFlow: is a machine learning library built by Google.
# Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
# Network:

# requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
# pip install requests