from flask import Blueprint, jsonify, request
from ..spotify import SpotifyAPI
import os


spotify = Blueprint('spotifyAPI', __name__)

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_ID']
spotify_api = SpotifyAPI(client_id=client_id, client_secret=client_secret)


@spotify.route('/featured_playlist/')
def featured_playlist():
    """ Gets featured playlist
    """
    playlist = spotify_api.fetch_featured_playlist()
    return jsonify(playlist)

@spotify.route('/featured_playlist/<playlist_uri>/')
def playlist_tracks(playlist_uri):
    """ Gets Playlist tracks
    """
    if playlist_uri:
        tracks = spotify_api.fetch_playlist_tracks(playlist_uri)
        return jsonify(tracks)