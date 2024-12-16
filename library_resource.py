class Resource:
    def __init__(self, id: str, title: str, author: str, year: int):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author} ({self.year})"