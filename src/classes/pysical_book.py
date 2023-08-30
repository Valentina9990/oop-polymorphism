from .book import Book

class PysicalBook(Book):
    def __init__(self, title, author, year, ubication, copiesAvailable):
        super().__init__(title, author, year)
        self.ubication = ubication
        self.copiesAvailable = copiesAvailable

    def showInfo(self):
        info = super().showInfo()
        return f"{info}\nUbicación: {self.ubication}\nEjemplares disponibles: {self.copiesAvailable}"
