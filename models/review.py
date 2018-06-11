#!/usr/bin/python3
"""Module: review - Class: Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inheritive from BaseModel
    class Review
    """
    place_id = ""
    user_id = ""
    text = ""
