#!/usr/bin/env python3
"""Spotify controller"""
from flask import Blueprint, jsonify, request
from ..controllers.spotify import SpotifyAPI
import os


spotify = Blueprint('spotifyAPI', __name__)

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
spotify_api = SpotifyAPI(client_id=client_id, client_secret=client_secret)


@spotify.route('/featured_playlist/', methods=['GET'], endpoint='featured_playlist', strict_slashes=False)
def featured_playlist():
    """ Gets featured playlist
    """
    playlist = spotify_api.fetch_featured_playlist()
    return jsonify(playlist)

@spotify.route('/new_release/', methods=['GET'], endpoint='new_release', strict_slashes=False)
def new_release():
    """ Gets new release
    """
    release = spotify_api.fetch_new_releases()
    if release is None:
        return jsonify({'msg': 'could not fetch new release'}), 404
    return jsonify(release)


@spotify.route('/playlist/<playlist_id>/tracks', methods=['GET'], strict_slashes=False)
def playlist_tracks(playlist_id):
    """ Gets new release
    """
    tracks = spotify_api.get_playlist_tracks(playlist_id)
    if tracks is None:
        return jsonify({'msg': 'could not fetch tracks'}), 404
    return jsonify(tracks)

@spotify.route('/album/<album_id>/tracks', methods=['GET'], strict_slashes=False)
def album_tracks(album_id):
    """ Gets album tracks
    """
    tracks = spotify_api.get_album_tracks(album_id)
    if tracks is None:
        return jsonify({'msg': 'could not fetch tracks'}), 404
    return jsonify(tracks)

@spotify.route('/track/<track_id>', methods=['GET'], strict_slashes=False)
def tracks(track_id):
    """ Gets new release
    """
    track = spotify_api.get_track(track_id)
    if track is None:
        return jsonify({'msg': 'could not fetch track'}), 404
    return jsonify(track)

@spotify.route('/popular_tracks', methods=['GET'], strict_slashes=False)
def top_tracks():
    """Get top 50 popular tracks"""
    popular_tracks = spotify_api.get_popular_tracks()
    if popular_tracks is None:
        return jsonify({'msg': 'could not fetch track'}), 404
    return jsonify(popular_tracks)

@spotify.route('/popular_artists', methods=['GET'], strict_slashes=False)
def top_artists():
    """get top artist"""
    limit = 50
    popular_artist = spotify_api.get_popular_artist(limit)
    if popular_artist is None:
        return jsonify({'msg': 'could not fetch track'}), 404
    return jsonify(popular_artist)

@spotify.route('/search', methods=['GET'])
def search():
    """ Search
    """
    query = request.args.get('query')
    if query:
        results = spotify_api.perform_search(query)
        return jsonify({'results': results})
    else:
        return jsonify({'error': 'No search query provided'})