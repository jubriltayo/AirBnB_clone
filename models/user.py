#!/usr/bin/python3
"""This module contains user information"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """Class inherits from Basemodel and contains
        public class attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
