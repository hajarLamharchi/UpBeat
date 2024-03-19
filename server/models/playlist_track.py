#!/usr/bin/python3
"""This module defines a track model"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class PlaylistTrack(BaseModel, Base):
    """
    This class defines playlist track
    """
    __tablename__ = 'ptracks'

    name = Column(String(128), nullable=False)
    uri = Column(String(128), nullable=False)
    playlist_id = Column(String(60), ForeignKey('playlists.id'), nullable=False)