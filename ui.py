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
    title = input("Enter title: ")

    author = input("Enter author: ")

    year = int(input("Enter year: "))

    self.manager.create_resource(id, title, author, year)
    def read_resource(self):

     id = input("Enter the ID of the book to read: ")

    book = self.manager.read_resource(id)

    print(book if book else "Book not found.")
    def edit_resource(self):

     id = input("Enter the ID of the book to edit: ")

    title = input("Cover new title: ")

    author = input("Cover new author: ")

    year = int(input("Cover new year: "))

    self.manager.update_resource(id, title, author, year)


def delete_resource(self):

    id = input("Cover Enter the ID of the book to delete: ")

    self.manager.delete_resource(id)