import flask

from app import flask_app
from .models import User_model

@flask_app.route('/')
def home():
    return 'home page'
@flask_app.route('/add_user/<username>')
def add_user(username):
    user = User_model(username=username)
    user.add_user()
    return flask.redirect('/')
