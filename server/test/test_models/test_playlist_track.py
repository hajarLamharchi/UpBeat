#!/usr/bin/python3
""" Contains the TestPlaylistTrackDocs class 
"""
from models.playlist_track import PlaylistTrack
from models.baseModel import BaseModel
import unittest


class TestPlaylistTrack(unittest.TestCase):
    """ Test the PlaylistTrack class
    """
    def test_is_subclass(self):
        """ Test that PlaylistTrack is a subclass of BaseModel
        """
        track = PlaylistTrack()
        self.assertIsInstance(track, BaseModel)
        self.assertTrue(hasattr(track, "id"))
        self.assertTrue(hasattr(track, "created_at"))
        self.assertTrue(hasattr(track, "updated_at"))

    def test_playlist_track_attr(self):
        """ Test the presence of playlistTrack attribute
        """
        track = PlaylistTrack()
        attrs = ['spotify_id', 'name', 'uri', 'href', 'release_date', 'uri', 'image_uri', 'duration_ms', 'playlist_id']
        for attr in attrs:
            attr = attr
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(track, attr))
                self.assertIsNone(getattr(track, attr))

    def test_str(self):
        """ test the str rep of PlaylistTrack model
        """
        track = PlaylistTrack()
        string = "[PlaylistTrack] ({}) {}".format(track.id, track.__dict__)
        self.assertEqual(string, str(track))

    def test_playlist_track_to_dict(self):
        """ test to_dict method creates PlaylistTrack to dict properly
        """
        track = PlaylistTrack()
        track_dict = track.to_dict()
        self.assertEqual(type(track_dict), dict)
        self.assertFalse("_sa_instance_state" in track_dict)
        for attr in track.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in track_dict)
        self.assertTrue("__class__" in track_dict)