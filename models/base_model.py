#!/usr/bin/python3
"""Module to create a base class: Base_Model"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initializes class with instance attributes:
            id, created_at, updated_at
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string of the instance"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the instance attribute: updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary of the all instance attributes and
            __class__ key added to the dictionary
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
