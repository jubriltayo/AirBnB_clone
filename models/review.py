#!/usr/bin/python3
"""This module contains information on state"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Child class review"""
    place_id = ""
    user_id = ""
    text = ""
