#!/usr/bin/env python3
"""User routes"""
from flask import Blueprint, jsonify, request
from models.user import User
from models.exp_tokens import ExpToken
from models import storage
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    current_user,
    get_jwt
)


user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'], endpoint='login', strict_slashes=False)
def login():
    """Login route"""
    from api.v1 import bcrypt

    if not request.is_json:
        return jsonify({'error': 'invalid content type, please use json'}), 415
        
    email  = request.json.get('email', None)
    password = request.json.get('password', None)
    if email is None or password is None:
        return jsonify({'error': 'email and password is required'}), 400
    user = storage.get_email(User, email.lower())
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify(
            {
                'message': 'user loggedin successfully',
                'tokens': {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            }
        ), 200
    return jsonify({'error': 'invalid email or password'}), 400


@user.route('/current_user', methods=['GET'], endpoint='current_user', strict_slashes=False)
@jwt_required()
def get_current_user():
    """ Gets current user
    """
    user = {
        'id': current_user.id,
        'email': current_user.email,
        'firstname': current_user.first_name,
        'lastname': current_user.last_name
    }
    return jsonify({'user': user}), 200


@user.route('/register', methods=['POST'], endpoint='register', strict_slashes=False)
def register():
    """Register route"""
    from api.v1 import bcrypt
    from api.v1.controllers.user import validate_email

    if not request.is_json:
        return jsonify({'error': 'invalid content type, please use json'})
    
    new_user_data = {
        'username': request.json.get('username'),
        'email': request.json.get('email').lower(),
        'password': bcrypt.generate_password_hash(request.json.get('password')).decode('utf-8'),
        'first_name': request.json.get('firstname'),
        'last_name': request.json.get('lastname')
    }
    # Validate form data
    if not new_user_data['username'] or not new_user_data['email'] or not new_user_data['password'] or not new_user_data['first_name'] or not new_user_data['last_name']:
        return jsonify({'error': 'all fields are required'}), 400
    
    # Email validation
    if not validate_email(new_user_data['email']):
        return jsonify({'error': 'invalid email address'}), 400
    
    # Check if user already exist
    existing_email = storage.get_email(User, new_user_data['email'])
    if existing_email:
        return jsonify({'error': 'user already exist'}), 400
    
    # Create new User
    new_user = User(**new_user_data)
    # Save User in database
    new_user.save()
    return jsonify({'message': 'user created successfully'})


@user.route("/logout", strict_slashes=False)
@jwt_required()
def logout():
    """Log out a user"""
    jwt = get_jwt()

    jti = jwt['jti']

    jti_data = {
        'jti': jti
    }
    exp_jti = ExpToken(**jti_data)
    exp_jti.save()
    return jsonify({'message': 'user logged out successfully'})


@user.route('/<user_id>', methods=['GET'], strict_slashes=False)
@jwt_required
def single_user(user_id):
    """ Get single user
    """
    user = storage.get(User, user_id)
    if user:
        playlists = []
        for item in user.playlists:
            playlists.append(item.to_dict())
        user = user.to_dict()
        user['playlists'] = playlists
        return jsonify(user), 200
    return jsonify({'message': 'user not found'}), 404
    

@user.route('/forgot_password', methods=['POST'])
def forgot_password():
    """ Forget password route
    """
    from api.v1.controllers.user import generate_reset_token, send_reset_email

    if not request.is_json:
        return jsonify({'error': 'invalid content type, please use json'})
    email  = request.json.get('email')
    if not email:
        return jsonify({'error': 'email is required'})
    user = storage.get_email(User, email.lower())
    if not user:
        return jsonify({'error': 'email not associated with a user'})
    token = generate_reset_token(email)
    send_reset_email(email, token)
    return jsonify({'message': 'Reset password email sent!'})


# @user.route('/reset-password/<token>', methods=['POST'])
# def reset_password(token):
#     """ Reset password
#     """
#     from api.v1 import bcrypt
#     from api.v1.controllers.user import verify_reset_token

#     if not request.is_json:
#         return jsonify({'error': 'invalid content type, please use json'})
    
#     email = verify_reset_token(token)
#     if email:
#         new_pwd = request.json.get('new_password')
#         user = storage.get_email(User, email.lower())
#         if user:
#             user.password = bcrypt.generate_password_hash(new_pwd).decode('utf-8')
#             user.save()
#             return jsonify({'message': 'Password reset successful!'})
#         return jsonify({'error': 'error finding email'}), 400
#     return jsonify({'error': 'Invalid or expired token'}), 400