#!/usr/bin/python3
"""
inherits from Base Model.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User info holding.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
