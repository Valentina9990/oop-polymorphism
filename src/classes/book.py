class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def showInfo(self):
        return f"Título: {self.title}\nAutor: {self.author}\nAño: {self.year}"

