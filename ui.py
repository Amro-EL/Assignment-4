from resource_manager import ResourceManager

from data_persistence import DataPersistence

class UserInterface:
    def __init__(self):
        self.manager = ResourceManager()
        self.load_resources()
def load_resources(self):

    self.manager.resources = DataPersistence.load_data('books.json')
    def save_resources(self):
     DataPersistence.save_data(self.manager.list_resources(),'books.json')
def display_menu(self):

    print("\n1. Create Resource")

    print("2. Read Resource")

    print("3. Edit Resource")

    print("4. Delete Resource")

    print("5. List Resources")

    print("6. Exit")
    

