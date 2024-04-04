#!/usr/bin/env python3
"""User controller"""
from api.v1 import mail, serializer
import os
import re

salt = os.environ['MAIL_USERNAME']

def validate_email(email):
    """ Basic email regex pattern
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def generate_reset_token(email):
    """ Generate a token for password reset
    """
    return serializer.dumps(email, salt=salt)


def verify_reset_token(token, expiration=3600):
    """  Verify the reset token
    """
    try:
        email = serializer.loads(token, salt=salt, max_age=expiration)
        return email
    except:
        return None

def send_reset_email(email, token):
    """ send reset token
    """
    from flask_mail import Message
    
    host = os.environ['SERVER_HOST']
    reset_link = f'{host}/api/v1/user/reset-password/{token}'
    msg = Message('Password Reset Request', recipients=[email])
    msg.body = f'Click the following link to reset your password: {reset_link}'
    mail.send(msg) 