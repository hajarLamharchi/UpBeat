#!/usr/bin/env python3
"""Favorite routes"""
from flask import Blueprint, jsonify, request
from models.favorite import Favorite
from models import storage
from flask_login import current_user, login_required

favorite = Blueprint('favorite', __name__)

@favorite.route('/all', methods=['GET'], endpoint='favorite', strict_slashes=False)
@login_required
def all_favorite():
    if not current_user.is_authenticated:
        return jsonify({'message': 'login first'})
    user_id = current_user.id
    favoriteList = storage.all(Favorite).values()
    favorites = []
    for song in favoriteList:
        if song.user_id == user_id:
            favorites.append(song.to_dict())
    return jsonify({'favorites': favorites}), 200

@favorite.route('/add', methods=['POST'], strict_slashes=False)
@login_required
def add_favorite():
    new_favorite_data = {
        'user_id': current_user.id,
        'song_id': request.form.get('songId')
    }
    if not new_favorite_data['song_id']:
        return jsonify({'message': 'Song ID is required'}), 400
    new_favorite = Favorite(**new_favorite_data)
    new_favorite.save()
    return jsonify({'message': 'Favorite list updated successfully'}), 200

@favorite.route('/delete/<string:id>', methods=['POST'], strict_slashes=False)
@login_required
def delete_favorite(id):
    favorite = storage.get(Favorite, id)
    if favorite:
        storage.delete(favorite)
        storage.save()
        return jsonify({'message': 'favorite song deleted successfully'}), 200
    return jsonify({'message': 'favorite list no found'}), 404