from flask import Flask

flask_app = Flask(__name__)

from app.filters import add_5_to_age,email

flask_app.jinja_env.filters['add_5'] = add_5_to_age
flask_app.jinja_env.filters['email']=email

from app import routes
