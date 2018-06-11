#!/usr/bin/python3
"""
Module with State class
"""
import models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __init__(self):
            super().__init__()
