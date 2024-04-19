#!/usr/bin/python3
""" starts web application"""

from files import Flask
from files import render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """displays hbnb filters Html page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)

@app.teardown_appcontext
def teardown(exc):
    """remove sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
