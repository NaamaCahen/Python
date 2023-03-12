import flask

app = flask.Flask(__name__)


@app.route('/blog')
def homepage():
    with open('./homepage.html') as homep:
        file = homep.read()
        return flask.render_template_string(file)


@app.route('/blog/articles')
def display_articles():
    articles_list = [
        {
            "name": "article1",
            "title": "article1 title"
        },
        {
            "name": "article2",
            "title": "article2 title"
        },
        {
            "name": "article3",
            "title": "article3 title"
        },
    ]
    with open('./articles.html') as file:
        articlespage = file.read()
        return flask.render_template_string(articlespage, articles=articles_list)


@app.route('/profile')
def profile():
    return flask.redirect(flask.url_for('homepage'))



app.run()
