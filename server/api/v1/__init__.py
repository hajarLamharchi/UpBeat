#!/usr/bin/env python3
"""Main app file where Flask app is defined and configure"""
from datetime import timedelta
from flask import Flask, jsonify, session
from .view.user import user
from .view.spotifyAPI import spotify
from .view.playlist import playlist
from .view.playlist_track import playlist_track
from .view.favorite import favorite
from models.user import User
from flask_login import LoginManager, logout_user
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

# Get env variables
FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']

# Flask app initialization
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
cors = CORS(app, supports_credentials=True)

# Flas mail comfig
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = ('no-reply', os.environ['MAIL_USERNAME'])
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
mail = Mail(app)
serializer = URLSafeTimedSerializer(app.secret_key)

# Flask login configuration
login_manager = LoginManager()
login_manager.init_app(app)

# bcrypt initialization
bcrypt = Bcrypt(app)

@app.before_request
def before_request():
    session.modified = True
    if 'permanent' not in session:
        logout_user()


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
app.register_blueprint(playlist, url_prefix='/api/v1/user')
app.register_blueprint(playlist_track, url_prefix='/api/v1/user')
app.register_blueprint(favorite, url_prefix='/api/v1/favorite')