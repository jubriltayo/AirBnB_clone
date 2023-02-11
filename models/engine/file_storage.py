#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():
    """Seralizes instances to a JSON file and
        Deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary representation of instance"""
        return self.__objects

    def new(self, obj):
        """Sets each instance in dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes instances in the dictionary to
            the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {key : value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file into dictionary
            representation of the instances
            """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(f"{cls_name}")(**obj))
        except FileNotFoundError:
            return