#!/usr/bin/python3
"""This module defines a class User"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    """
    This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False)