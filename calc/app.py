# Put your app in here.
import operations
from flask import Flask, request

app = Flask(__name__)

@app.route('/<func>')
def math(func):
    a = request.args['a']
    b = request.args['b']
    a = int(a)
    b = int(b)
    call = getattr(operations, func)
    result = call(a,b)
    return f'{result}'

@app.route('/math/<func>')
def math_func(func):
    a = request.args['a']
    b = request.args['b']
    a = int(a)
    b = int(b)
    call = getattr(operations, func)
    result = call(a,b)
    return f'{result}'