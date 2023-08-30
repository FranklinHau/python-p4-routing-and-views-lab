#!/usr/bin/env python3

from flask import Flask, request # request is a global object that holds all incoming request data for the current request being processed 
import sys # this module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter  

app = Flask(__name__) # this line creates an instance of the Flask class for the application 

# Route Handlers 
# Each of the functions defined below is a route handler that does something when a user accesses
# the associated route in the web browser. 

# This function returns a simple HTML string that will be displayed when
# we accesses the home('/')URL of the application. 
@app.route('/')
def home(): 
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# This function prints the 'parameter' to the console and returns it as a response.
# The 'parameter' is a dynamic part of the URL, so visiting '/print/hello' will
# print 'hello to the console and return 'hello' as the response
@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return parameter

# This function returns a newline_separated string of numbers from 0 to 'parameter - 1'. 
# The 'parameter' is expected to be an integer. So, visiting '/count/5' will return the string
# "0\n1\n2\n3\n4\n".
@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(map(str, range(parameter))) + '\n'

# This function performs a mathematical operations on two parameters, 'param1'
# and 'param2', based on the 'operation' specified in the URL, and returns the result as a string. 
# The 'param1' and 'param2' are expected to be integers, and 'operation' is expected to be one of 
# following: '+', '-', '*', 'div', '%'. Visiting '/math/5/+/5' will return the string '10'
@app.route('/math/<int:param1>/<operation>/<int:param2>')
def math(param1, operation, param2):
    if operation == '+':
        result = param1 + param2
    elif operation == '-':
        result = param1 - param2
    elif operation == '*':
        result = param1 * param2
    elif operation == 'div':
        result = param1 / param2
    elif operation == '%':
        result = param1 % param2
    else: 
        return 'Invalid operation'
    return str(result)

# This block of code checks if the script is being run directly(and not being imported as a module)
# and then runs the applicaion on the port 5555 with debug mode enabled. 
# Debug mode allows the application to automatically reload when changes are made to the code
# and provides detail error messages in the browser when an error occurs. 
if __name__ == '__main__':
    app.run(port=5555, debug=True)
