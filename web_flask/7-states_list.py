#!/usr/bin/python3
from flask import Flask
from models import storage, storage.all
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def td_appcontext():
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Return an HTML page showing a list with all state objects"""
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
