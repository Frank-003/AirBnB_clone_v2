#!/usr/bin/python3
"""Flask framework"""
from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Set up SQLAlchemy session
@app.teardown_appcontext
def close_db(error):
    storage.close()

# Route to display a list of states
@app.route('/states_list', strict_slashes=False)
def states_list():
    # Get all State objects from DBStorage and sort by name
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

