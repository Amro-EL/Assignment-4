import json
from book_resource import BookResource

class DataPersistence:
    def __init__(self, filename: str):
        self.filename = filename

@staticmethod
def save_data(resources, filename: str):
        with open(filename, 'w') as file:
            json.dump([resource.__dict__ for resource in resources], file)

        def load_data(self):
         try:
            with open(self.filename, 'r') as file:
                return [BookResource(**data) for data in json.load(file)]
         except FileNotFoundError:
          return []
