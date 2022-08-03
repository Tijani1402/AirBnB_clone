#!/usr/bin/python3
"""Defines the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class inherits from BaseModel"""

    state_id = ''
    name = ''

    