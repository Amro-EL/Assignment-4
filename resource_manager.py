class ResourceManager:

 def __init__(self):
  self.resources = []

def create_resource(self, id: str, title: str, author: str, year: int):
   book = Book(id, title, author, year)

self.resources.append(book)
def read_resource(self, id: str):

    return next((book for book in self.resources if book.id == id), None)
def update_resource(self, id: str, title: str, author: str, year: int):

    book = self.read_resource(id)
    if book:

        book.title = title

        book.author = author

        book.year = year

