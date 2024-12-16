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
def run(self):

    while True:

        self.display_menu()
        choice = int(input("Choose an option: "))

        if choice == 1:

            self.create_resource()

        elif choice == 2:

            self.read_resource()
        elif choice == 3:

            self.edit_resource()

        elif choice == 4:

            self.delete_resource()

        elif choice == 5:

            self.list_resources()

        elif choice == 6:

            self.save_resources()

            break
def create_resource(self):

    id = input("Enter ID: ")


        



