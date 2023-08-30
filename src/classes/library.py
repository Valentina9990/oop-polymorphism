import re
from .book import Book

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def searchByTitle(self, title):
        results = []
        for book in self.books:
            if re.search(title, book.title, re.IGNORECASE):
                results.append(book)
        return results
