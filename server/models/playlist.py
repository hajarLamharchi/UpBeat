#!/usr/bin/python3
"""This module defines a playlist model"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Playlist(BaseModel, Base):
    """
    This class defines a user by various attributes"""
    __tablename__ = 'playlists'

    collaborative = Column(String(128), nullable=False, default=False)
    name = Column(String(128), nullable=False)
    description = Column(String(600), nullable=True)
    href = Column(String(128), nullable=True)
    primary_color = Column(String(128), nullable=True, default='#ffffff')
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="playlists")