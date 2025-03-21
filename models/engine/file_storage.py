import json
import models
from models.base_model import BaseModel
from models.course import Course
from models.user import User
from os import path

classes = {
    "BaseModel": BaseModel,
    "Course": Course,
    "User": User
}


class FileStorage:
    """Handles storage and retrieval of object in JSON format"""

    __file_path = "file.json"
    __objects = {}
    
    def all(self, cls=None):
        """Returns all objects, optionally filtered by class"""
        if cls is not None:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects
    
    def new(self, obj):
        """Adds an object to storage"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes objects to write them to a JSON file"""
        json_objects = {}
        for key, obj in self.__objects.items():
            obj_dict = obj.to_dict()
            # Remove password if it exists
            obj_dict.pop("password", None)
            json_objects[key] = obj_dict
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file into objects"""
        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    obj_dict = json.load(f)
                for key, obj_data in obj_dict.items():
                    cls_name = obj_data.get("__class__")
                    if cls_name in classes:
                        self.__objects[key] = classes[cls_name] (**obj_data)
            except Exception as e:
                print(f"Error loading storage file:{e}")

    def delete(self, obj=None):
        """Delete an object from storage if present"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()