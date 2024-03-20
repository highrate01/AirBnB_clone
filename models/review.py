#!/usr/bin/python3
"""Rreview module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class to inherit from BaseModel
       Attributes:
       place_id: empty string
       user_id: empty string
       text: empty string
    """
    place_id = ""
    user_id = ""
    text = ""
