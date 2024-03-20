#!/usr/bin/python3
"""
Defines a class user that inherit from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    handles user's information
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
