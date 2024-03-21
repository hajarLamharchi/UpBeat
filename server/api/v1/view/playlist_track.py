#!/usr/bin/env python3
"""User routes"""
from flask import Blueprint, jsonify, request
from models.playlist_track import PlaylistTrack
from models.playlist import Playlist
from models import storage
from flask_login import current_user, login_required
from ..spotify import SpotifyAPI
import os

playlist_track = Blueprint('track', __name__)

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
spotify_api = SpotifyAPI(client_id=client_id, client_secret=client_secret)

@playlist_track.route('playlists/new_track', methods=['GET'], strict_slashes=False)
@login_required
def new_track():
    """ Add a nw playlist
    """
    track_id = request.args.get('track_id')
    playlist_id = request.args.get('playlist_id')
    print(track_id)
    if track_id and playlist_id:
        playlist_exist = storage.get(Playlist, playlist_id)
        if playlist_exist is None:
            return jsonify({'msg': 'playlist not found'}), 404
        track_exist = storage.get(PlaylistTrack, track_id)
        if track_exist:
            return jsonify({'msg': 'track already exist on playlist'}), 409
        track = spotify_api.get_track(track_id)
        if track is None:
            return jsonify({'msg': 'could not fetch track'}), 404
        new = {
            'id': track['id'],
            'name': track['name'],
            'uri': track['uri'],
            'playlist_id': playlist_id
        }  
        if not new['id'] or not new['name'] or not new['uri'] or not new['playlist_id']:
            return jsonify({'error': 'invalid feilds, could not add to playlist'}), 400
        new_track = PlaylistTrack(**new)
        # Save track in database
        new_track.save()
        return jsonify({'message': 'playlist created successfully'})
    

