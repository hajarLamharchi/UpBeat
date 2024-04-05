#!/usr/bin/python3
""" Contains the TestUSerDocs class 
"""
from models.user import User
from models.baseModel import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """ Test the User class
    """
    def test_is_subclass(self):
        """ Test that User is a subclass of BaseModel
        """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_user_attr(self):
        """ Test the presence of user attribute
        """
        user = User()
        attrs = ['email', 'username', 'password', 'first_name', 'last_name']
        for attr in attrs:
            attr = attr
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(user, attr))
                self.assertIsNone(getattr(user, attr))

    def test_str(self):
        """ test the str rep of user model
        """
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))
    
    def test_user_to_dict(self):
        """ test to_dict method creates user to dict properly
        """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertFalse("_sa_instance_state" in user_dict)
        for attr in user.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in user_dict)
        self.assertTrue("__class__" in user_dict)