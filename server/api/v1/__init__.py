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
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from flask_jwt_extended import JWTManager
from datetime import timedelta

# Get env variables
FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']

# Flask app initialization
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
app.config["JWT_SECRET_KEY"] = FLASK_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=14)
jwt = JWTManager(app)
cors = CORS(app, supports_credentials=True, expose_headers=['Set-Cookie'], origins='*')

# Flask mail comfig
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


# FLASK_JWT LOAD USER
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_headers, jwt_data):
    from models import storage

    user_id = jwt_data["sub"]
    user = storage.get(User, user_id)
    return user

# FLASK_JWT ERROR HANDLING
@jwt.expired_token_loader
def expired_token(jwt_header, jwt_data):
    return jsonify({"error": "expired token"}), 401

@jwt.invalid_token_loader
def invalid_token(error):
    return jsonify({"error": "Verification failed, invalid token"}), 401
    
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"error": "Request does not contain any token"}), 401,

# FLASK_JWT BLOCKLIST FOR LOGOUT
@jwt.token_in_blocklist_loader
def exp_token(jwt_header, jwt_data):
    from models.exp_tokens import ExpToken
    from models import storage

    jti = jwt_data['jti']

    token = storage.get_jti(ExpToken, jti)

    return token is not None
    


app.register_blueprint(user, url_prefix='/api/v1/user')
app.register_blueprint(spotify, url_prefix='/api/v1/')
app.register_blueprint(playlist, url_prefix='/api/v1/user')
app.register_blueprint(playlist_track, url_prefix='/api/v1/user')
app.register_blueprint(favorite, url_prefix='/api/v1/favorite')