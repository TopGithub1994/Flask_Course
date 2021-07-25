from distutils.log import debug
from unicodedata import name
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Top<h1>"

@app.route('/about')
def about():
    return "<h1>My name is Flask<h1>"

@app.route('/admin')
def profile():
    return "<h1>Admin<h1>"

@app.route('/user/<name>/<age>')
def member(name,age):
    return "<h1>Hello Member : {} <h1> <h1> Age : {} <h1>".format(name,age)

if __name__ == '__main__':
    app.run(debug=True)