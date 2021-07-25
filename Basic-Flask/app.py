from distutils.log import debug
from re import template
from unicodedata import name
from django.shortcuts import render
from flask import Flask, render_template, request
from numpy import product
app = Flask(__name__)

@app.route('/')
def index():
    data = {"name":"topl3ack","age":30,"salary":"30000"}
    return render_template("index.html",mydata = data)

@app.route('/about')
def about():
    product = ["Intel i9","Intel i7","Intel i5","Intel i3"]
    return render_template("about.html",myproduct=product)

@app.route('/admin')
def profile():
    username = "topl3ack"
    return render_template("admin.html",username = username)

@app.route('/sendData')
def signupForm():
    fname=request.args.get('fname')
    description=request.args.get('description')
    return render_template("thankyou.html",data={"name":fname,"description":description})

if __name__ == '__main__':
    app.run(debug=True)