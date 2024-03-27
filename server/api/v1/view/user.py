#!/usr/bin/env python3
"""User routes"""
from flask import Blueprint, jsonify, request, session
from functools import wraps
from models.user import User
from models import storage
from flask_login import login_user, current_user, login_required, logout_user


user = Blueprint('user', __name__)

def prevent_access_if_logged_in(route):
    """ A custom wrap that a direct an already loggedin user
    """
    @wraps(route)
    def decorated_route(*args, **kwargs):
        if current_user.is_authenticated:
            # return an error response if there is a current user
            return jsonify({'error': 'a user is already looged in'}), 400
        else:
            # Allow access to the route
            return route(*args, **kwargs)
    return decorated_route

@user.route('/login', methods=['POST'], endpoint='login', strict_slashes=False)
@prevent_access_if_logged_in
def login():
    """Login route"""
    from api.v1 import bcrypt

    if current_user.is_authenticated:
        return jsonify({'messasge': 'already logged in'})
    
    if not request.is_json:
        return jsonify({'error': 'invalid content type, please use json'})
        
    email  = request.json.get('email')
    password = request.json.get('password')
    if not email or not password:
        return jsonify({'error': 'email and password is required'})
    user = storage.get_email(User, email.lower())
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user, remember=True)
        session['permanent'] = True
        return jsonify({'message': 'user logged in successfully'}), 200
    return jsonify({'error': 'invalid email or password'}), 400


@user.route('/register', methods=['GET', 'POST'], endpoint='register', strict_slashes=False)
@prevent_access_if_logged_in
def register():
    """Register route"""
    from api.v1 import bcrypt
    from api.v1.controllers.user import validate_email

    if current_user.is_authenticated:
        return jsonify({'messasge': 'already logged in'})
    
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
@login_required
def logout():
    """Log out a user"""
    logout_user()
    session.pop('permanent', None)
    return jsonify({'message': 'user logged out successfully'})

@user.route('/<user_id>', methods=['GET'], strict_slashes=False)
@login_required
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
@prevent_access_if_logged_in
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

@user.route('/reset-password/<token>', methods=['POST'])
@prevent_access_if_logged_in
def reset_password(token):
    """ Reset password
    """
    from api.v1 import bcrypt
    from api.v1.controllers.user import verify_reset_token

    if not request.is_json:
        return jsonify({'error': 'invalid content type, please use json'})
    
    email = verify_reset_token(token)
    if email:
        new_pwd = request.json.get('new_password')
        user = storage.get_email(User, email.lower())
        if user:
            user.password = bcrypt.generate_password_hash(new_pwd).decode('utf-8')
            user.save()
            return jsonify({'message': 'Password reset successful!'})
        return jsonify({'error': 'error finding email'}), 400
    return jsonify({'error': 'Invalid or expired token'}), 400