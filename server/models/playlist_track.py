#!/usr/bin/python3
"""This module defines a track model"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class PlaylistTrack(BaseModel, Base):
    """
    This class defines a user by various attributes"""
    __tablename__ = 'ptracks'

    spotify_id = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    uri = Column(String(128), nullable=False)
    href = Column(String(128), nullable=True)
    release_date = Column(String(128), nullable=True)
    image_uri = Column(String(128), nullable=True)
    duration_ms = Column(Integer(), nullable=True)
    playlist_id = Column(String(60), ForeignKey('playlists.id'), nullable=False)