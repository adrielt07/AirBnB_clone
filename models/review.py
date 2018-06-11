#!/usr/bin/python3
"""Module: review - Class: Review"""
import models


class Review(models.BaseModel):
    """
    Inherting from BaseModel
    Setting class attribute
    """
    place_id = ""
    user_id = ""
    text = ""
