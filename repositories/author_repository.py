from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import repositories.book_repository as book_repository

def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        book = book_repository.select(row['book_id'])
        author = Author(row['first_name'], row['last_name'] , row['id'] )
        authors.append(author)
    return authors

