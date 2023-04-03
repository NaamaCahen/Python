import flask

from app import app
from app.models import Book
from app import db

@app.route('/')
def index():
    books = ', '.join([book.title for book in Book.query.all()])
    return books

@app.route('/insert')
def insert():
    book=Book(book_id=3, title='thirdbook', author='myself', price=148)
    db.session.add(book)
    db.session.commit()
    return 'book'
