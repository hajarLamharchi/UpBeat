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
            return None
        
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
            None
        
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
            return None
        
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
            return None
        
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
            return None
        
    def perform_search(self, query, limit=20):
        """ Perform search on spotify
        """
        # Search for tracks
        track_results = self.sp.search(q=query, type='track', limit=limit)
        tracks = [{'type': 'track', 'name': track['name'], 'artist': track['artists'][0]['name'], 'uri': track['uri']} for track in track_results['tracks']['items']]

        # Search for playlists
        playlist_results = self.sp.search(q=query, type='playlist', limit=limit)
        playlists = [{'type': 'playlist', 'name': playlist['name'], 'uri': playlist['uri']} for playlist in playlist_results['playlists']['items']]

        # Search for albums
        album_results = self.sp.search(q=query, type='album', limit=limit)
        albums = [{'type': 'album', 'name': album['name'], 'artist': album['artists'][0]['name'], 'uri': album['uri']} for album in album_results['albums']['items']]

        # Search for artists
        artist_results = self.sp.search(q=query, type='artist', limit=limit)
        artists = [{'type': 'artist', 'name': artist['name'], 'uri': artist['uri']} for artist in artist_results['artists']['items']]

        # Combine all search results
        result_dict = {
            'tracks': tracks,
            'playlist': playlists,
            'albums': albums,
            'artists': artists
        }

        return result_dict
        