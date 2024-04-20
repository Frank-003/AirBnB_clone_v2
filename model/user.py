#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = 'oyiengofrankline49@gmail.com'
    password = 'oyiengo03'
    first_name = 'Frankline'
    last_name = 'Oyiengo'
