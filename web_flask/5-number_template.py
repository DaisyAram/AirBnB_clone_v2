#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
   """ root route"""
   return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hnbn():
   """ hbnb route"""
   return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
   """c is fun"""
   return 'C, {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def Pythoniscool(text='is cool'):
   """pythonismagic"""
   return 'Python, {}'.format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
   """integer number"""
   return '{} is a number'.format(n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def integer(n):
   """display a HTML page only if n is an integer"""
   return render_template('5-number.html', number=n)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
