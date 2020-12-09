from flask import Flask, render_template, request, redirect 
from repositories import author_repository
from repositories import book_repository
from models.author import Author

# import  Blueprint from flask
from flask import Blueprint


books_blueprint = Blueprint("books", __name__)

# INDEX
@books_blueprint.route('/books')
def authors():
    # Get all tasks from the db
    books = book_repository.select_all()
    return render_template("books/index.html", books=books)


# NEW
# GET '/books/new'

# CREATE
# POST '/books'

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'

