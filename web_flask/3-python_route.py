#!/usr/bin/python3
"""starts flask web aplication"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """prints hello hbn"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """c is fun"""
    return 'C, {}'.format(text.replace('_', ' '))


app.route('/python/<text>', strict_slashes=False)
def Pythoniscool(text='is cool'):
    """pythonismagic"""
    return 'Python, {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
