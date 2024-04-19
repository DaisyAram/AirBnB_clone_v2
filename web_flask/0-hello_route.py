#!/usr/bin/python3
"""starts flask web aplication"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)

def hello_hbnb():
   """prints hello hbn"""
   return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
