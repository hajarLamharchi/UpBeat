#!/usr/bin/env python3
"""User routes"""
from flask import Blueprint, jsonify, request
from models.playlist_track import PlaylistTrack
from models.playlist import Playlist
from models import storage
from flask_login import current_user, login_required
from ..controllers.spotify import SpotifyAPI
import os

playlist_track = Blueprint('track', __name__)

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
spotify_api = SpotifyAPI(client_id=client_id, client_secret=client_secret)

@playlist_track.route('playlists/new_track', methods=['GET'], strict_slashes=False)
@login_required
def new_track():
    """ Add a new playlist
    """
    if not current_user.is_authenticated:
        return jsonify({'messasge': 'please login to conitnue'}), 301
    spotify_id = request.args.get('spotify_id')
    playlist_id = request.args.get('playlist_id')
    if spotify_id and playlist_id:
        playlist_exist = storage.get(Playlist, playlist_id)
        if playlist_exist is None:
            return jsonify({'msg': 'playlist not found'}), 404
        track_id = f'{current_user.id[8]-{spotify_id}}'
        track_exist = storage.get(PlaylistTrack, track_id)
        if track_exist and track_exist.playlist_id == playlist_id:
            return jsonify({'msg': 'track already exist on playlist'}), 409
        track = spotify_api.get_track(spotify_id)
        if track is None:
            return jsonify({'msg': 'could not fetch track'}), 404
        new = {
            'id': track_id,
            'spotify_id': track['id'],
            'name': track['name'],
            'uri': track['uri'],
            'image_uri': track['album']['images'][0]['url'],
            'href': track['href'],
            'release_date': track['album']['release_date'],
            'duration_ms': track['duration_ms'],
            'playlist_id': playlist_id
        }
        if not new['spotify_id'] or not new['name'] or not new['uri'] or not new['playlist_id']:
            return jsonify({'error': 'invalid feilds, could not add to playlist'}), 400
        new_track = PlaylistTrack(**new)
        # Save track in database
        new_track.save()
        return jsonify({'message': 'playlist created successfully'})
    return jsonify({'message': 'could not add track to playlist'})
    
@playlist_track.route('playlists/new_track', methods=['DELETE'])
@login_required
def remove_track():
    """ remove a track from playlist
    """
    if not current_user.is_authenticated:
        return jsonify({'messasge': 'please login to conitnue'}), 301
    track_id = request.args.get('track_id')
    playlist_id = request.args.get('playlist_id')
    if track_id and playlist_id:
        playlist = storage.get(Playlist, playlist_id)
        if playlist is None:
            return jsonify({'msg': 'playlist not found'}), 404
        track = storage.get(PlaylistTrack, track_id)
        if track is None:
            return jsonify({'msg': 'track not found'}), 404
        if playlist.user_id != current_user.id:
            return jsonify({'msg': 'you cannot delete from this playlist'}), 301
        storage.delete(track)
        storage.save()
        return jsonify({'message': 'playlist deleted successfully'}), 200
        
@playlist_track.route('playlists/<playlist_id>/tracks', methods=['GET'])
@login_required
def user_tracks(playlist_id):
    """ Get user playlist tracks"""
    if not current_user.is_authenticated:
        return jsonify({'messasge': 'please login to conitnue'}), 301
    if not playlist_id:
        return jsonify({'message': 'playlist not found'}), 404
    db_track = storage.all(PlaylistTrack).values()
    tracks = []
    for item in db_track:
        if item.playlist_id == playlist_id:
            tracks.append({'tracks': item.to_dict()})
    return jsonify(tracks)
