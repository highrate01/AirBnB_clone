#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class to inherit from BaseModel
       Attributes:
       state_id: state.id
       name: name
    """
    def __init__(self):
        self.state_id = ""
        self.name = ""
