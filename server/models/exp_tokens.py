"""This module defines expired token"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String


class ExpToken(BaseModel, Base):
    """
    This class defines expired tokens for logout purpose
    """
    __tablename__ = "exptoken"

    jti = Column(String(128), nullable=False)
