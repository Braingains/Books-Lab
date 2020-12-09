from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_1 = Author("Dr Amanda", "Brown")
author_repository.save(author_1)

author_2 = Author("A.A", "Milne")
author_repository.save(author_2)

book_repository.select_all()

book_1 = Book("The Prison Doctor", "depression", "Prisons", author_1)
book_repository.save(book_1)

book_2 = Book("Winnie the Pooh", "Childrens", "Methuen and Co", author_2)
book_repository.save(book_2)
