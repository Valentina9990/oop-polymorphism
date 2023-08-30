import re
from classes.pysical_book import PysicalBook
from classes.digital_book import DigitalBook
from classes.library import Library

# Create a PysicalBook and a DigitalBook instance
pysicalBook = PysicalBook("Libro Físico", "Autor Físico", 2023, "Estante 1", 5)
digitalBook = DigitalBook("Libro Digital", "Autor Digital", 2023, "https://example.com", "PDF")

# Create a Library instance
library = Library()


# Add books to the Library
library.addBook(pysicalBook)
library.addBook(digitalBook)


# Search by title using regular expressions
searchResults = library.searchByTitle("Libro")
for book in searchResults:
    print(book.showInfo())
    print("=" * 40)