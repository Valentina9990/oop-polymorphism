from .book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year, urlDownload, format):
        super().__init__(title, author, year)
        self.urlDownload = urlDownload
        self.format = format

    def showInfo(self):
        info = super().showInfo()
        return f"{info}\nURL de descarga: {self.urlDownload}\nFormato: {self.format}"


