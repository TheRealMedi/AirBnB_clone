#!/usr/bin/python3
"""
inherits from Base Model.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review info holding.
    """
    place_id = ""
    user_id = ""
    text = ""
