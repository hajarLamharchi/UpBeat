#!/usr/bin/env python3
"""Main app file where Flask app is defined and configure"""
from flask import Flask, jsonify
from .view.user import user
from .view.spotifyAPI import spotify
from models.user import User
from flask_login import LoginManager
import os
from flask_bcrypt import Bcrypt

# Get env variables
FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']

# Flask app initialization
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

# Flask login configuration
login_manager = LoginManager()
login_manager.init_app(app)

# bcrypt initialization
bcrypt = Bcrypt(app)

# Custom 404 error handler - not found
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 'page not found'}), 404

# Custom 401 error handler - unauthorized
@app.errorhandler(401)
def page_unauthorized(error):
    return jsonify({'error': 'please log in to continue'}), 401

# Creates a user loader for flask-login callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    from models import storage
    return storage.get(User, user_id)


app.register_blueprint(user, url_prefix='/api/v1/user')
app.register_blueprint(spotify, url_prefix='/api/v1/')