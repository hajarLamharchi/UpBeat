#!/usr/bin/python3
"""
Contains class BaseModel where future models will be derived
"""
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid


Base = declarative_base()


class BaseModel():
    """
    BaseModel class from which future classes will be derived"""
    #Base Model columns
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initialize instance variables"""
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        val = datetime.fromisoformat(val)
                    setattr(self, key, val)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of class"""
        cls = self.__class__.__name__
        return ("[{}] ({}) {}".format(cls, self.id, self.__dict__))
    
    def save(self):
        """Updates the updated_at attribute to current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)  # Add a new instance to the session
        models.storage.save()  # Commit changes to the database

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def update(self, **kwargs):
        """Update the instance with the provided keyword arguments."""
        for key, value in kwargs.items():
            if key != '__class__':
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        self.save()