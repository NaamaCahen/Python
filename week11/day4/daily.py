import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('homepage.html')

@app.route('/color/<bgcolor>')
def colorpage(bgcolor):
    return flask.render_template('color.html',bgcolor=bgcolor)


app.run(debug=True)
