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
        try:
            client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                                  client_secret=client_secret)
            self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
            self.initialization_successful = True
        except Exception as e:
            print("Error fetching featured playlist:", e)
            self.initialization_successful = False
        
    def fetch_featured_playlist(self):
        """
        Method to fetch featured playlist
        """
        # Check if spoify client is initialized succesfully
        if not self.initialization_successful:
            return {"error": "Spotify client initialization failed"}
        
        try:
            playlist = self.sp.featured_playlists()
            return playlist
        except Exception as e:
            print("Error fetching featured playlist:", e)
            return {"error": "Error fetching playlist"}
        
    def fetch_new_releases(self):
        """ Method to fetch new release
        """
         # Check if spoify client is initialized succesfully
        if not self.initialization_successful:
            return {"error": "Spotify client initialization failed"}
        
        try:
            release = self.sp.new_releases()
            return release
        except Exception as e:
            print("Error fetching featured new release:", e)
            return {"error": "Error fetching new release"}
        
    def get_playlist_tracks(self, playlist_uri):
        """ Comment
        """
        # Check if spoify client is initialized succesfully
        if not self.initialization_successful:
            return {"error": "Spotify client initialization failed"}
        try:
            playlist_id = playlist_uri.split(':')[-1]
            tracks = self.sp.playlist_tracks(playlist_id)
            return tracks['items']
        except Exception as e:
            print("Error fetching tracks", e)
            return {"error": "Error fetching tracks"}
        
    def get_album_tracks(self, album_id):
        """ Gets album tracks
        """
        # Check if spoify client is initialized succesfully
        if not self.initialization_successful:
            return {"error": "Spotify client initialization failed"}
        try:
            tracks = self.sp.album_tracks(album_id)
            return tracks
        except Exception as e:
            print("Error fetching tracks", e)
            return {"error": "Error fetching tracks"}
        
    def get_track(self, track_id):
        """ Get  track
        """
          # Check if spoify client is initialized succesfully
        if not self.initialization_successful:
            return {"error": "Spotify client initialization failed"}
        
        try:
            track = self.sp.track(track_id)
            return track
        except Exception as e:
            print("Error fetching track", e)
            return {"error": "Error fetching track"}
        
        