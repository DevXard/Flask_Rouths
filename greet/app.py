from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/<new>')
def new_route(new):
    return f"welcome {new}"