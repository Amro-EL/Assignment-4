import json

from resource import Book

class DataPersistence:
    @staticmethod
def save_data(resources, filename : str):
    with open(filename, 'w') as file:
        json.dump([book.__dict__ for book in resources], file)

@staticmethod
def load_data(filename : str):
    try:
        with open(filename, 'r') as file:
            return [Book(**data) for data in json.load(file)]
    except FileNotFoundError:
        return []
Copy
