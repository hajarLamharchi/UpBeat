#!/usr/bin/python3
""" Contains the TestExpTokenDocs class 
"""
from models.exp_tokens import ExpToken
from models.baseModel import BaseModel
import unittest


class TestPlaylist(unittest.TestCase):
    """ Test the Playlist class
    """
    def test_is_subclass(self):
        """ Test that Favourite is a subclass of BaseModel
        """
        token = ExpToken()
        self.assertIsInstance(token, BaseModel)
        self.assertTrue(hasattr(token, "id"))
        self.assertTrue(hasattr(token, "created_at"))
        self.assertTrue(hasattr(token, "updated_at"))

    def test_ExpToken_attr(self):
        """ Test the presence of Exptoken attribute
        """
        token = ExpToken()
        attrs = ['jti']
        for attr in attrs:
            attr = attr
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(token, attr))
                self.assertIsNone(getattr(token, attr))

    def test_str(self):
        """ test the str rep of Exptoken model
        """
        token = ExpToken()
        string = "[ExpToken] ({}) {}".format(token.id, token.__dict__)
        self.assertEqual(string, str(token))

    def test_Exptoken_to_dict(self):
        """ test to_dict method creates Exptoken to dict properly
        """
        token = ExpToken()
        token_dict = token.to_dict()
        self.assertEqual(type(token_dict), dict)
        self.assertFalse("_sa_instance_state" in token_dict)
        for attr in token.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in token_dict)
        self.assertTrue("__class__" in token_dict)