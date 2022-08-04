#!/usr/bin/python3
"""Defines the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """State class inherits from BaseModel"""

    place_id = ''
    user_id = ''
    text = ''
   