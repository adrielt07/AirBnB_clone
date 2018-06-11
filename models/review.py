#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """Inherit from base class"""
        super().__init__()
