#!/usr/bin/env python3
"""
Handles spotify related task
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAPI:
    """
    Spotify related function class
    """
    def __init__(self, client_id, client_secret):
        """Initialize spotify client
        """
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                              client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def fetch_featured_playlist(self):
        """
        Method to fetch playlist
        """
        playlist = self.sp.featured_playlists()
        return playlist
    
    def fetch_single_track(self):
        """
        Method to fetch playlist
        """
        track = self.sp.featured_playlists()
        return track
    
    def fetch_playlist_tracks(self, playlist_uri):
        """
        Fetch playlist uri
        """
        tracks = self.sp.playlist_tracks(playlist_uri)