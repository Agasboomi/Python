# API
# API stands for Application Programming Interface.
# Every application which has CRUD(Create, Read, Update, Delete) operation has an API to create data, to get data, to update data or to delete data from a database.

# To build an API, it is good to understand HTTP protocol and HTTP request and response cycle.
# HTTP is an established communication protocol between a client and a server
# 200 - OK
# 404 - Error 

# day 29 
# Builting apis

# day 30
# Conculations

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/about')
def about():
    return "This is the About Page"

@app.route('/contact')
def contact():
    return "Contact us at example@email.com"

@app.route('/services')
def services():
    return "These are our Services"

@app.route('/help')
def help_page():
    return "This is the Help Page"

if __name__ == '__main__':
    app.run(debug=True)