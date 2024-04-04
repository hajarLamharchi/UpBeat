#!/usr/bin/env python3
"""Favorite routes"""
from flask import Blueprint, jsonify, request
from models.favorite import Favorite
from models import storage
from flask_jwt_extended import jwt_required, current_user

favorite = Blueprint('favorite', __name__)

@favorite.route('/all', methods=['GET'], endpoint='favorite', strict_slashes=False)
@jwt_required()
def all_favorite():
    user_id = current_user.id
    favoriteList = storage.all(Favorite).values()
    favorites = []
    for song in favoriteList:
        if song.user_id == user_id:
            favorites.append(song.to_dict())
    return jsonify({'favorites': favorites}), 200


@favorite.route('/add', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_favorite(): 
    if not request.is_json:
        return jsonify({'error': 'invalid content type, please use json'})
    
    new_favorite_data = {
        'user_id': current_user.id,
        'song_id': request.json.get('songId')
    }
    if not new_favorite_data['song_id']:
        return jsonify({'message': 'Song ID is required'}), 400
    new_favorite = Favorite(**new_favorite_data)
    new_favorite.save()
    return jsonify({'message': 'Favorite list updated successfully'}), 200


@favorite.route('/delete/<string:id>', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_favorite(id):
    favorite = storage.get(Favorite, id)
    if favorite:
        storage.delete(favorite)
        storage.save()
        return jsonify({'message': 'favorite song deleted successfully'}), 200
    return jsonify({'message': 'favorite list no found'}), 404