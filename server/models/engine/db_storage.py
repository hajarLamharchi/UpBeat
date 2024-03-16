#!/usr/bin/python3
"""Definition for database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.baseModel import BaseModel, Base
from models.user import User
import os

classes = {"User": User }

class DBStorage:
    """DB class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('postgresql://{}:{}@{}/upbeat'.
                                      format(
                                          os.environ['DB_USERNAME'],
                                          os.environ['DB_PASSWORD'],
                                          os.environ['DB_HOST']
                                      ))
   
    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dict[key] = elem
        else:
            model_list = [ User ]
            for clase in model_list:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dict[key] = elem
        return (dict)
    
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """add the object to the current database session"""
        if isinstance(obj, User):
        # Ensure that first_name and last_name are not None
            if obj.first_name is not None and obj.last_name is not None:
                self.__session.add(obj)
            else:
            # Handle the case where first_name or last_name is None
                raise ValueError("Both first_name and last_name must be provided for a new User.")
        else:
            self.__session.add(obj)

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
    
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
    
    def get_email(self, cls, email):
        """
        Returns the object based on the email
        None if not found
        """
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.email == email):
                return value
        return None