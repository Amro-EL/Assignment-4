import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library_resource import Resource

class ResourceManager:
 def __init__(self):
        self.resources = []

        def create_resource(self, id: str, title: str, author: str, year: int) -> Resource:
         resource = Resource(id, title, author, year)
        self.resources.append(Resource)
        return Resource

        def read_resource(self, id: str) -> Resource:
         for resource in self.resources:
            if resource.id == id:
                return resource
        return None

        def update_resource(self, id: str, title: str, author: str, year: int) -> None:
         resource = self.read_resource(id)
        if resource:
            resource.title = title
            resource.author = author
            resource.year = year

        def delete_resource(self, id: str) -> None:
         self.resources = [resource for resource in self.resources if resource.id != id]

        def list_resources(self) -> list[Resource]:
         return self.resources