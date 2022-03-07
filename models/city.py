#!/usr/bin/python3
"""
inherits from Base Model.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City info holding.
    """
    state_id = ""
    name = ""
