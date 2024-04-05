#!/usr/bin/python3
""" Contains the TestPlaylistDocs class 
"""
from models.playlist import Playlist
from models.baseModel import BaseModel
import unittest


class TestPlaylist(unittest.TestCase):
    """ Test the Playlist class
    """
    def test_is_subclass(self):
        """ Test that Playlist is a subclass of BaseModel
        """
        playlist = Playlist()
        self.assertIsInstance(playlist, BaseModel)
        self.assertTrue(hasattr(playlist, "id"))
        self.assertTrue(hasattr(playlist, "created_at"))
        self.assertTrue(hasattr(playlist, "updated_at"))

    def test_playlist_attr(self):
        """ Test the presence of playlist attribute
        """
        playlist = Playlist()
        attrs = ['collaborative', 'name', 'description', 'href', 'primary_color', 'user_id']
        for attr in attrs:
            attr = attr
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(playlist, attr))
                self.assertIsNone(getattr(playlist, attr))

    def test_str(self):
        """ test the str rep of playlist model
        """
        playlist = Playlist()
        string = "[Playlist] ({}) {}".format(playlist.id, playlist.__dict__)
        self.assertEqual(string, str(playlist))

    def test_playlist_to_dict(self):
        """ test to_dict method creates playlist to dict properly
        """
        playlist = Playlist()
        playlist_dict = playlist.to_dict()
        self.assertEqual(type(playlist_dict), dict)
        self.assertFalse("_sa_instance_state" in playlist_dict)
        for attr in playlist.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in playlist_dict)
        self.assertTrue("__class__" in playlist_dict)