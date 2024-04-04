#!/usr/bin/env python3
"""User routes"""
from flask import Blueprint, jsonify, request
from models.playlist import Playlist
from models import storage
from flask_jwt_extended import jwt_required, current_user

playlist = Blueprint('playlist', __name__)

@playlist.route('/playlists', methods=['GET'], endpoint='playlists', strict_slashes=False)
@jwt_required()
def all_playlists():
    """ Get all playlist
    """
    db_playlist = storage.all(Playlist).values()
    playlist = []
    for item in db_playlist:
        playlist.append(item.to_dict())
    return jsonify({'playlist': playlist}), 200


@playlist.route('/playlists/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required()
def all_user_playlist(user_id):
    """ Get a user playlist
    """
    if not user_id:
        return jsonify({'message': 'playlist no found'}), 404
    db_playlist = storage.all(Playlist).values()
    playlist = []
    for item in db_playlist:
        if item.user_id == user_id:
            playlist.append(item.to_dict())
    return jsonify({'playlist': playlist}), 200


@playlist.route('playlist/new_playlist', methods=['POST'], strict_slashes=False)
@jwt_required()
def new_playlist():
    """ Add a nw playlist
    """
    if not request.is_json:
        return jsonify({'error': 'invalid content type, please use json'})
    new_playlist_data = {
        'name': request.json.get('name'),
        'user_id': current_user.id,
        'description': request.json.get('description'),
        'primary_color': request.json.get('primary_color'),
    }
    if not new_playlist_data['name'] or not new_playlist_data['user_id']:
        return jsonify({'error': 'all fields are required'}), 400
    
    new_playlist = Playlist(**new_playlist_data)
    # Save playlist in database
    new_playlist.save()
    return jsonify({'message': 'playlist created successfully'})


@playlist.route('playlist/<playlist_id>', methods=['GET'], strict_slashes=False)
def single_playlist(playlist_id):
    """ Get single playlist
    """
    playlist = storage.get(Playlist, playlist_id)
    print(playlist)
    if playlist:
        return jsonify(playlist.to_dict()), 200
    else:
        return jsonify({'message': 'playlist not found'}), 404

    
@playlist.route('playlist/update_playlist/<playlist_id>', methods=['POST'], strict_slashes=False)
@jwt_required()
def update_playlist(playlist_id):
    """ Add a nw playlist
    """
    if not request.is_json:
        return jsonify({'error': 'invalid content type, please use json'})
    playlist = storage.get(Playlist, playlist_id)
    if playlist.user_id != current_user.id:
        return jsonify({'message': 'you cannot not update this playlist'}), 301
    playlist.name = request.json.get('name')
    playlist.description = request.json.get('description')
    playlist.primary_color = request.json.get('primary_color')
    if not playlist.name  or playlist.name == '':
        return jsonify({'error': 'all fields are required'}), 400
    playlist.save()
    return jsonify({'message': 'playlist updated successfully'})

    
@playlist.route('playlist/<playlist_id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_playlist(playlist_id):
    """ Delete single playlist
    """
    playlist = storage.get(Playlist, playlist_id)
    if playlist:
        if playlist.user_id != current_user.id:
            return jsonify({'msg': 'you cannot delete this playlist'}), 301
        storage.delete(playlist)
        storage.save()
        return jsonify({'message': 'playlist deleted successfully'}), 200
    else:
        return jsonify({'message': 'playlist does not exist'}), 404
