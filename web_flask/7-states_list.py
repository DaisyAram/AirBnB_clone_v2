#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


app = Flask(__name__)


classes = {"Amenity": Amenity, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page inside the tag BODY"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
