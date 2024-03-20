#!/usr/bin/python3
"""This module defines a favorite model"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Favorite(BaseModel, Base):
    """
    This class defines the favorite songs by various attributes"""
    __tablename__ = "favorite"

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    songId = Column(String(60), nullable=False)
