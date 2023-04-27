import random

import flask_sqlalchemy
import flask_migrate
from flask import Flask

flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = random._urandom(56)
flask_app.config['DEBUG'] = True


db_info = {'host': 'localhost',
           'database': 'cards',
           'psw': 'naamacahen',
           'user': 'postgres',
           'port': '5432'}

flask_app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import models, routes