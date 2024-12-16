class BookResource:
    def __init__(self, title: str, author: str, isbn: str, quantity: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __dict__(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'quantity': self.quantity
        }