import flask

from app import flask_app


@flask_app.route('/<int:age_in_future>')
def main_page(age_in_future):
    return flask.render_template("main.html", name="bob", age=5, age_in_future=age_in_future)


@flask_app.route('/<string:username>')
def username_email(username):
   return flask.render_template("main.html", name="bob", age=5,age_in_future=5, username=username)
