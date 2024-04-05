#!/usr/bin/python3
""" Contains the TestFavouriteDocs class 
"""
from models.favorite import Favorite
from models.baseModel import BaseModel
import unittest


class TestPlaylist(unittest.TestCase):
    """ Test the Playlist class
    """
    def test_is_subclass(self):
        """ Test that Favourite is a subclass of BaseModel
        """
        fav = Favorite()
        self.assertIsInstance(fav, BaseModel)
        self.assertTrue(hasattr(fav, "id"))
        self.assertTrue(hasattr(fav, "created_at"))
        self.assertTrue(hasattr(fav, "updated_at"))

    def test_favourite_attr(self):
        """ Test the presence of playlist attribute
        """
        fav = Favorite()
        attrs = ['user_id', 'song_id']
        for attr in attrs:
            attr = attr
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(fav, attr))
                self.assertIsNone(getattr(fav, attr))

    def test_str(self):
        """ test the str rep of playlist model
        """
        fav = Favorite()
        string = "[Favorite] ({}) {}".format(fav.id, fav.__dict__)
        self.assertEqual(string, str(fav))

    def test_favourite_to_dict(self):
        """ test to_dict method creates favourite to dict properly
        """
        fav = Favorite()
        fav_dict = fav.to_dict()
        self.assertEqual(type(fav_dict), dict)
        self.assertFalse("_sa_instance_state" in fav_dict)
        for attr in fav.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in fav_dict)
        self.assertTrue("__class__" in fav_dict)