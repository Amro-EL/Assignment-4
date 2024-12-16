from resource_manager import ResourceManager

from data_persistence import DataPersistence

class UserInterface:
    def __init__(self):
        self.manager = ResourceManager()
        self.load_resources()
def load_resources(self):

    self.manager.resources = DataPersistence.load_data('books.json')
    def save_resources(self):

